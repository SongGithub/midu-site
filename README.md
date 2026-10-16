# Midu personal site

A dependency-free static site draft for Song Jin. Project descriptions are grounded in already public repositories and writing. Song should review the positioning and project copy and provide an approved contact route before launch.

## Preview

From the repository root, run `python3 -m http.server 8766`, then open `http://127.0.0.1:8766/`.

## Hosting

This repository is published from `main` through GitHub Pages at [www.midu.com.au](https://www.midu.com.au/). The older blog remains at [blog.midu.com.au](https://blog.midu.com.au/). The private learning library uses [learn.midu.com.au](https://learn.midu.com.au/) on Cloudflare Pages with Cloudflare Access and Google sign-in.

Domain registration remains at VentraIP. Cloudflare manages DNS; the public website and blog use DNS-only records and continue to be served by GitHub Pages. See [DEPLOYMENT.md](DEPLOYMENT.md) for the current setup and rollback procedure.

The site uses a small browser-exclusion loader for Cloudflare Web Analytics. It contains no forms or third-party font requests.

## Visitor counts

Cloudflare Web Analytics measures visits and page views on `www.midu.com.au` from deployment onward. It does not identify unique people or recover past traffic. In Cloudflare, open Observability → Analytics → Web analytics, select `www.midu.com.au`, and read **Visits** for the desired date range with **Exclude bots** enabled.

To exclude your own visits, open [this browser-exclusion link](https://www.midu.com.au/?analytics=off) once in each browser/profile and device you use. The page confirms that this browser is excluded, and the analytics beacon never loads in that browser. A local-storage flag saves only this choice, not a visitor identifier. To reverse it, open [the inclusion link](https://www.midu.com.au/?analytics=on); counting resumes on the next visit.

Clearing site data or using a new/private browser session requires excluding that browser again. Blocked scripts or unavailable browser storage can also reduce the count. Blog, private learning pages, previews and localhost are not included by this loader. The collection token in HTML is public by design; it is not the Cloudflare API token stored in GitHub secrets.

## Infrastructure

The public site's DNS configuration lives in [infra/cloudflare/](infra/cloudflare/README.md). The shared DNS zone belongs to `personal-infra`; the private learning service owns its DNS, Pages and Access configuration in `midu-learning`. Each resource belongs to one Terraform state. Credentials and state stay outside Git, and infrastructure changes require a reviewed manual plan/apply.

GitHub Pages publishes an artifact containing only website files through `scripts/build_site.py`. The live read-only Cloudflare workflow uses this repository's Actions secrets; its first verification passed on 16 October 2026. See the infrastructure runbook for state adoption and apply prerequisites.
