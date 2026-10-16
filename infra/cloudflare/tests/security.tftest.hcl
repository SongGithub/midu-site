mock_provider "cloudflare" {}
override_resource {
  target = cloudflare_dns_record.public_site
}
run "preserve_public_site_routing" {
  command = plan
  assert {
    condition = length(cloudflare_dns_record.public_site) == 2 && alltrue([for key, record in cloudflare_dns_record.public_site : (
      !record.proxied && record.content == "songgithub.github.io" && record.type == "CNAME" &&
      record.name == "${key}.midu.com.au" && record.ttl == 1 && record.zone_id == var.zone_id
    )])
    error_message = "Both public endpoints must remain on GitHub Pages through DNS-only CNAMEs."
  }
}
