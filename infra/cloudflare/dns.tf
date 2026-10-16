locals {
  public_hosts = toset(["www", "blog"])
}

resource "cloudflare_dns_record" "public_site" {
  for_each = local.public_hosts
  zone_id  = var.zone_id
  name     = "${each.key}.midu.com.au"
  type     = "CNAME"
  content  = "songgithub.github.io"
  proxied  = false
  ttl      = 1

  lifecycle {
    prevent_destroy = true
  }
}
