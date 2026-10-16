# https://github.com/cloudflare/terraform-provider-cloudflare/blob/v5.28.0/docs/resources/dns_record.md#import
import {
  for_each = local.public_hosts
  to       = cloudflare_dns_record.public_site[each.key]
  id       = "${var.zone_id}/${var.existing_dns[each.key]}"
}
