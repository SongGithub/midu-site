# Keep analytics separate from the DNS-only adoption workflow and credentials.
resource "cloudflare_web_analytics_site" "public_site" {
  account_id   = var.account_id
  host         = "www.midu.com.au"
  auto_install = false

  lifecycle {
    prevent_destroy = true
  }
}

# Adopt the existing manually provisioned site; do not create a second beacon.
import {
  to = cloudflare_web_analytics_site.public_site
  id = "${var.account_id}/${var.existing_site_id}"
}
