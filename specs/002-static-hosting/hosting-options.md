# Hosting decision: GitHub Pages or Cloudflare Pages

**Status:** Decision pending, 2026-10-08.

| Concern | GitHub Pages | Cloudflare Pages |
| --- | --- | --- |
| Current state | Already building successfully from this public repository. | No Cloudflare project or account connection configured. |
| Temporary URL | Inherits `blog.midu.com.au/midu-site/` from the user Pages site's custom domain; the default `github.io` URL redirects there. | A separate `<project>.pages.dev` URL independent of `midu.com.au` DNS. |
| Repository visibility | Public repository works on GitHub Free. Private repository Pages requires an eligible paid GitHub plan; the Pages website remains public. | Git integration supports public or private GitHub repositories. The website is public unless separately protected. |
| Apex `midu.com.au` | Can use GitHub Pages A/AAAA records at the current DNS provider after its zone is repaired. | Cloudflare Pages requires the apex zone to use Cloudflare nameservers. Moving DNS requires an audit and migration of every record, including the blog and any mail records. |
| Ongoing workflow | Push static files to `main`; Pages rebuilds. | Git integration builds on push and provides branch/PR previews, after granting Cloudflare access to the repository. |

## Recommendation

Keep **this portfolio repository** public: the site is public, and a scan of tracked files found no email addresses or credential-like strings. Keep the proposed learning library in a **different private repository** and deploy it behind managed authentication. See `../003-private-learning/spec.md`.

The new private requirement makes Cloudflare Pages plus Access useful even if the public portfolio remains on GitHub Pages. It can provide an independent `pages.dev` address for the learning library without changing domain DNS first. A custom `learn.midu.com.au` address can follow once DNS and Access configuration are verified. If Song wants one hosting provider for both sites, Cloudflare Pages is preferable after a careful DNS migration; GitHub Pages remains a simple public-portfolio host in the meantime.

Do not make the GitHub repository private while it is the active Pages source without checking the account plan: GitHub says changing a Pages repository to private on GitHub Free unpublishes the site. Do not move domain nameservers until all DNS records have been inventoried and the blog is ready to be retested.

Sources: [GitHub Pages availability](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages), [GitHub custom-domain inheritance](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [GitHub repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility), [Cloudflare Pages Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/), [Cloudflare Pages custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/), and [Cloudflare Pages limits](https://developers.cloudflare.com/pages/platform/limits/).
