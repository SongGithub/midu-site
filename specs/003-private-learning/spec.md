# Feature Specification: Private Learning Library

**Created**: 2026-10-08  
**Status**: Draft for discussion  
**Input**: Song wants to host AI-generated HTML self-learning material online and access it after login, with no access for other visitors.

## Objective

Provide Song with a convenient private website for static learning pages while keeping the public personal site open to everyone. Authentication must happen before the private files are served. A password form inside a static page, hidden links, and `robots.txt` are not access controls.

## Proposed First Release

- Keep the public portfolio in `SongGithub/midu-site` as a separate site.
- Store learning pages in a **separate private repository**. Do not commit them to the public site, including its history or build artifacts.
- Deploy that repository to a separate Cloudflare Pages project with a `pages.dev` address. Protect the production `pages.dev` hostname and every preview/deployment hostname with Cloudflare Access.
- Allow only Song's specified Google or Microsoft account. Song chose an existing account over email one-time PIN. Require multifactor authentication on the chosen account; record the exact allowlisted address during setup, outside this public repository.
- Add `learn.midu.com.au` only after the DNS zone is repaired and the custom hostname is protected by its own Access application. The first release does not depend on the domain.

## User Scenarios

### 1. Song opens a learning page

Song opens the private library on desktop or mobile, signs in using the chosen identity, and can browse an index and open an individual HTML learning page with its local assets.

### 2. Song adds a generated page

Song reviews an AI-generated HTML file and its assets, adds them to the private repository, and publishes the update through a repeatable Git workflow. The public portfolio is unaffected.

### 3. Another visitor tries a direct link

Someone without the allowlisted identity cannot fetch the library index, an HTML page, its assets, a branch preview, or an immutable deployment URL by guessing or receiving a link.

## Functional Requirements

- **PRV-001**: The learning repository and its full Git history MUST be private. Learning content MUST NOT be copied into the public portfolio repository or deployment.
- **PRV-002**: Every HTTP route serving private content or assets MUST be gated at the hosting edge before bytes are returned. Client-side login checks are insufficient.
- **PRV-003**: An Access policy MUST allow only Song's explicitly chosen identity. A broad email-domain or “any authenticated user” rule is prohibited.
- **PRV-004**: The production `pages.dev` hostname, preview aliases, immutable deployment URLs, and any later custom domain MUST all be protected. A new deployment must not create a public bypass.
- **PRV-005**: The private site MUST provide an index and working links to individual HTML files and their relative assets on common desktop and mobile browsers.
- **PRV-006**: Publishing a new file MUST have a documented preview and rollback path. It MUST NOT require writing a custom password database or exposing a long-lived deployment token in the repository.
- **PRV-007**: Generated HTML and linked resources MUST be reviewed for external network requests, embedded secrets, and unexpected scripts before publishing. Private pages should use a separate origin from the public portfolio.
- **PRV-008**: The private site MUST not depend on `midu.com.au` DNS until the authoritative nameservers are consistent and the custom hostname has its own tested Access policy.
- **PRV-009**: Sign-in MUST use Song's existing Google or Microsoft account. The exact provider and account address MUST be confirmed during setup and MUST NOT be published in this public specification.

## Acceptance Tests

1. From a signed-out browser, direct requests for the index, a private HTML file, an asset, and a preview URL are redirected to authentication or denied; none returns the file body.
2. Song's chosen identity can sign in and open the index and a sample learning page on desktop and mobile.
3. A different identity is denied after attempting to sign in.
4. A new preview deployment and its immutable URL pass the same unauthenticated checks before any real learning material is uploaded.
5. A search of the public repository and deployed public site finds no private learning content or private repository references that reveal file contents.

## Success Criteria

- Signed-out checks of the index, a page, an asset, a preview, and a permanent deployment URL return zero private file bodies.
- Song's approved account opens an index and sample page with working local assets on desktop and mobile; a different account is denied.
- Song publishes a new learning page and restores the prior version using documented steps, without editing authentication settings.
- A search of the public repository and deployed portfolio finds zero private learning file contents.

## Assumptions

- The first release serves one person. Search, tags, collaboration, and an online editor can wait.
- Song will create a Cloudflare account; none exists yet.
- The initial library uses its own provider address so the current `midu.com.au` DNS issue cannot prevent access.

## Decisions Needed

- Choose Google or Microsoft as the sign-in provider and confirm the exact allowlisted account at setup time.
- Create a Cloudflare account and Zero Trust organisation; then verify the selected sign-in method before uploading real learning pages.
- Decide whether the first release needs a simple file index only or search and tagging.
- Decide whether generated pages may execute their own JavaScript or load third-party assets; this affects content review and security headers.

## Source Notes

Cloudflare documents [Pages preview protection](https://developers.cloudflare.com/pages/configuration/preview-deployments/) and warns that enabling it alone does **not** protect the production `pages.dev` or custom domain. Its [known-issues guide](https://developers.cloudflare.com/pages/platform/known-issues/) explains how to protect those hostnames separately. Access supports [single-email allowlists and identity-provider login](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) as well as [one-time PIN](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/). GitHub states that [Pages websites remain public even when the source repository is private](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site), so a private GitHub repository alone does not satisfy this feature.
