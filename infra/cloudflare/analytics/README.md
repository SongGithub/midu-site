# Public visitor analytics

This independent Terraform root describes the existing Cloudflare Web Analytics site for `www.midu.com.au`. It uses manual installation because `www` is DNS-only and the browser exclusion in `assets/analytics.js` must run before the beacon loads. It has no DNS, learning, Access or hosting resources.

The site was provisioned through the authenticated dashboard on 16 October 2026. **Terraform state adoption has not run.** CI validates this configuration with a mock provider; it does not verify live drift or apply changes. The DNS read-only plan workflow remains separate and still checks exactly two DNS records.

Before state adoption, configure durable encrypted Terraform state with locking, provide the real `account_id` and `existing_site_id` through ignored inputs or approved secrets, and use a separately scoped token with **Account Settings Read** for planning. Keep the existing DNS token unchanged. Follow the [provider's import documentation](https://github.com/cloudflare/terraform-provider-cloudflare/blob/v5.28.0/docs/resources/web_analytics_site.md#import), review a plan that only imports this existing site, and stop if it proposes creating, replacing or changing a resource. Applying a future analytics change needs **Account Settings Write**, a reviewed plan and the protected deployment process; this repository has no analytics apply workflow.

The collection token embedded in HTML is deliberately public and is not an API credential. Do not commit account IDs, site IDs, API credentials, raw plans or state. Do not enable automatic beacon installation: it would bypass the local browser exclusion. See the [site README](../../../README.md#visitor-counts) for counting and exclusion behaviour.
