# Midu personal site

A dependency-free static site draft for Song Jin. Project descriptions are grounded in already public repositories and writing. Song should review the positioning and project copy and provide an approved contact route before launch.

## Preview

From the repository root, run `python3 -m http.server 8766`, then open `http://127.0.0.1:8766/`.

## Hosting

This repository is published from `main` through GitHub Pages at [www.midu.com.au](https://www.midu.com.au/). The older blog remains at [blog.midu.com.au](https://blog.midu.com.au/). The private learning library uses [learn.midu.com.au](https://learn.midu.com.au/) on Cloudflare Pages with Cloudflare Access and Google sign-in.

Domain registration remains at VentraIP. Cloudflare manages DNS; the public website and blog use DNS-only records and continue to be served by GitHub Pages. See [DEPLOYMENT.md](DEPLOYMENT.md) for the current setup and rollback procedure.

The site contains no JavaScript, forms, analytics, or third-party font requests.

## Infrastructure

The public site's DNS configuration lives in [infra/cloudflare/](infra/cloudflare/README.md). The shared DNS zone belongs to `personal-infra`; the private learning service owns its DNS, Pages and Access configuration in `midu-learning`. Each resource belongs to one Terraform state. Credentials and state stay outside Git, and infrastructure changes require a reviewed manual plan/apply.

The proposed GitHub Pages workflow packages only website files through `scripts/build_site.py`. See the infrastructure runbook for the one-time switch from branch/root publishing to GitHub Actions.
