import importlib.util
import io
import json
from pathlib import Path
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

spec = importlib.util.spec_from_file_location("discovery", Path(__file__).parents[1] / "discover_dns.py")
discovery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(discovery)


class DiscoveryTest(unittest.TestCase):
    def setUp(self):
        self.values = {"zone_id": "1" * 32}

    def response(self, name, count=1):
        return io.BytesIO(json.dumps({"success": True, "result": [
            {"name": name, "type": "CNAME", "id": "2" * 32}
        ] * count}).encode())

    def test_discovers_exact_public_records_with_read_requests(self):
        with patch.object(discovery, "urlopen", side_effect=[
            self.response("www.midu.com.au"), self.response("blog.midu.com.au")
        ]) as call:
            values = discovery.prepare_inputs(self.values, "PRIVATE_TOKEN")
        self.assertEqual(set(values["existing_dns"]), {"www", "blog"})
        for args in call.call_args_list:
            request = args.args[0]
            self.assertEqual(request.get_method(), "GET")
            self.assertEqual(request.get_header("Authorization"), "Bearer PRIVATE_TOKEN")
            self.assertIn("type=CNAME", request.full_url)

    def test_missing_or_ambiguous_records_are_rejected(self):
        for count in (0, 2):
            with self.subTest(count=count), patch.object(discovery, "urlopen", return_value=self.response("www.midu.com.au", count)):
                with self.assertRaises(ValueError):
                    discovery.prepare_inputs(self.values, "PRIVATE_TOKEN")

    def test_unexpected_record_is_rejected(self):
        with patch.object(discovery, "urlopen", return_value=self.response("other.midu.com.au")):
            with self.assertRaises(ValueError):
                discovery.prepare_inputs(self.values, "PRIVATE_TOKEN")

    def test_api_failure_does_not_expose_response_or_token(self):
        error = HTTPError("https://api.cloudflare.com/", 403, "PRIVATE_RESPONSE", {}, None)
        with patch.object(discovery, "urlopen", side_effect=error):
            with self.assertRaises(ValueError) as result:
                discovery.prepare_inputs(self.values, "PRIVATE_TOKEN")
        self.assertNotIn("PRIVATE", str(result.exception))

    def test_explicit_ids_do_not_need_discovery(self):
        values = self.values | {"existing_dns": {"www": "2" * 32, "blog": "3" * 32}}
        with patch.object(discovery, "urlopen") as call:
            self.assertEqual(discovery.prepare_inputs(values, "PRIVATE_TOKEN"), values)
            call.assert_not_called()

    def test_invalid_inputs_are_rejected(self):
        for values in ([], {}, {"zone_id": "invalid"}, self.values | {"existing_dns": {"www": "bad"}}):
            with self.subTest(values=values), self.assertRaises(ValueError):
                discovery.prepare_inputs(values, "PRIVATE_TOKEN")


if __name__ == "__main__":
    unittest.main()
