# Deployment runbook

Verified on 16 October 2026.

## Hosting and domain ownership

| Hostname | Hosting | DNS routing | Access |
| --- | --- | --- | --- |
| `www.midu.com.au` | GitHub Pages, a website-only artifact built from `main` by GitHub Actions | DNS only | Public |
| `blog.midu.com.au` | Existing GitHub Pages blog | DNS only | Public |
| `learn.midu.com.au` | Separate private Cloudflare Pages project | Proxied | Cloudflare Access with Google sign-in and an exact-email allow rule |

Registration remains at VentraIP. Cloudflare's Free plan manages the DNS zone through `annabel.ns.cloudflare.com` and `chase.ns.cloudflare.com`. The website and blog CNAME records point to `songgithub.github.io`; the learning CNAME points to `midu-learning.pages.dev`.

The bare `midu.com.au` hostname had no address record in the original VentraIP zone. This migration preserved that state; `www.midu.com.au` is the public site's configured hostname.

Keep private learning material in its separate private repository. This public repository contains only a login link. Both sites remain ordinary static files in Git; no Worker or reverse proxy was added.

## Protected learning hostname

The custom domain must be registered in the Cloudflare Pages project as well as present in DNS. A CNAME alone does not complete the setup. Wait for Pages to show **Active / SSL enabled** before directing visitors there.

The custom hostname has its own Access application. The original `midu-learning.pages.dev` production hostname and wildcard preview hostnames retain their existing protection.

Certificate issuance and renewal require public access only to `learn.midu.com.au/.well-known/acme-challenge/*`. A dedicated Access application permits that path. All learning pages and assets remain protected. The private site's top-level `404.html` prevents unknown validation paths from falling back to private homepage content. Do not put private files under the certificate-validation path or remove that 404 safeguard.

During the cutover, Access redirected the certificate-validation endpoint to login, leaving Pages verification pending and producing 522 responses on some authenticated requests. Allowing only the validation path resolved this setup issue. It does not establish the cause of the earlier reported intermittent failure on the original `pages.dev` address.

## Verify a change

1. Confirm `www.midu.com.au` and `blog.midu.com.au` still return HTTP 200 from GitHub Pages.
2. Confirm signed-out requests to the learning homepage, guides, and CSS redirect to Cloudflare Access rather than return private content. Repeat for the original production hostname and an immutable preview URL.
3. Confirm an unknown URL under the certificate-validation path returns the generic 404 page without private content. Similar paths outside that exact prefix must still require login.
4. In an approved Google session, open the learning homepage, Interview prep, Running, and a guide. Check styling and links, not just the login page.

## Update and roll back

Terraform configuration for the public `www` and `blog` records is in [infra/cloudflare/](infra/cloudflare/README.md). The shared zone is owned by `personal-infra`; the private learning repository owns `learn` DNS, Pages and Access. Import the existing resources and obtain a no-change plan before treating the stacks as authoritative. A code revert does not itself revert infrastructure.

Pages Source is **GitHub Actions**, verified on 16 October 2026. The workflow packages `index.html`, `CNAME`, `.nojekyll`, `assets/` and reviewed pages under `work/`; it must not upload the repository root, specs, infrastructure or build tooling. The [first artifact deployment](https://github.com/SongGithub/midu-site/actions/runs/38883931917) succeeded. Live HTML and CSS matched source, the blog returned 200, the learning homepage redirected to Access, and infrastructure/README URLs returned 404.

The [live Cloudflare adoption check](https://github.com/SongGithub/midu-site/actions/runs/38883973346) also passed using repository-held secrets: both public DNS records were import-only or unchanged, with no live mutations planned. This was a read-only plan, not an apply or durable state adoption. The zone and learning stacks remain separate draft changes awaiting their own credentials and verification.

For public-site updates, preview the HTML/CSS locally, review the exact diff, and push the intended files to `main`. Revert a bad commit and push the revert to roll it back.

Export the DNS zone before changing providers. The original VentraIP zone and the Cloudflare BIND export were saved privately during this migration. To move away from Cloudflare, recreate the required records at the replacement DNS provider before switching nameservers at VentraIP. Replace the private site's Access protection before sending its traffic to a new host. DNS export does not include Access applications or policies.

VentraIP warns that old hosted DNS records become inactive after a nameserver switch and are removed after 72 hours. Restore them from the backup before using the former nameservers for rollback; do not assume the old zone remains available.

References: [Pages custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/), [Pages verification troubleshooting](https://developers.cloudflare.com/pages/configuration/debugging-pages/), [DNS import and export](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/).
