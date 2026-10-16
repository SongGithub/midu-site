mock_provider "cloudflare" {}
override_resource {
  target = cloudflare_web_analytics_site.public_site
}
run "manual_public_site_only" {
  command = plan
  assert {
    condition = (
      cloudflare_web_analytics_site.public_site.host == "www.midu.com.au" &&
      cloudflare_web_analytics_site.public_site.account_id == var.account_id &&
      !cloudflare_web_analytics_site.public_site.auto_install
    )
    error_message = "Use a manual beacon only for the public www site, so browser exclusions run first."
  }
}
