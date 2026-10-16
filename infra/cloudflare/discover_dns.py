"""Prepare site inputs inside the Actions runner without exposing credentials."""

import json
import os
from pathlib import Path
import re
import sys
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

HOSTS = ("www", "blog")


def prepare_inputs(values, token):
    if not isinstance(values, dict) or not re.fullmatch(r"[a-f0-9]{32}", str(values.get("zone_id", ""))):
        raise ValueError("Provide the actual 32-character zone_id in CLOUDFLARE_TFVARS_JSON.")
    ids = values.get("existing_dns")
    if ids is None:
        ids = {}
        for host in HOSTS:
            name = f"{host}.midu.com.au"
            query = urlencode({"name": name, "type": "CNAME", "match": "all"})
            url = f"https://api.cloudflare.com/client/v4/zones/{values['zone_id']}/dns_records?{query}"
            request = Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
            try:
                with urlopen(request, timeout=30) as response:
                    data = json.load(response)
            except (URLError, ValueError, TimeoutError):
                raise ValueError("DNS discovery failed. Check the token's DNS Read permission and zone scope.") from None
            if not isinstance(data, dict):
                raise ValueError("DNS discovery returned an unexpected response; refusing adoption.")
            records = data.get("result", [])
            if not data.get("success") or not isinstance(records, list) or len(records) != 1:
                raise ValueError(f"DNS discovery requires exactly one existing CNAME for {name}.")
            record = records[0]
            if not isinstance(record, dict) or record.get("name") != name or record.get("type") != "CNAME":
                raise ValueError("DNS discovery returned an unexpected record; refusing adoption.")
            ids[host] = record.get("id")
    if not isinstance(ids, dict) or set(ids) != set(HOSTS) or not all(
        re.fullmatch(r"[a-f0-9]{32}", str(value)) for value in ids.values()
    ):
        raise ValueError("Provide exactly the two valid existing DNS record IDs, or omit existing_dns to discover them.")
    return values | {"existing_dns": ids}


if __name__ == "__main__":
    try:
        token = os.environ.get("CLOUDFLARE_API_TOKEN", "")
        if not token:
            raise ValueError("Set this repository's CLOUDFLARE_API_TOKEN Actions secret.")
        values = prepare_inputs(json.loads(os.environ.get("CLOUDFLARE_TFVARS_JSON", "")), token)
        with open(Path(sys.argv[1]), "x", opener=lambda path, flags: os.open(path, flags, 0o600)) as output:
            json.dump(values, output)
    except (ValueError, IndexError):
        sys.exit("Input preparation failed. Check the zone ID, token scope and existing public CNAME records. No credentials or API response were printed.")
