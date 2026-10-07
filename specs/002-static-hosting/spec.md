# Feature Specification: Static Site Hosting

**Created**: 2026-10-07  
**Status**: Draft for review  
**Scope**: Hosting and domain setup for the new personal site in this repository.

## Context

The older Pelican blog uses two repositories: `SongGithub/songgithub.github.io-src` for source and `SongGithub/songgithub.github.io` for the published GitHub Pages site. The blog's custom hostname is `blog.midu.com.au`. The new personal site is a separate product and must not replace the blog's files or domain configuration.

`midu.com.au` has been purchased. Its delegated nameservers are `ns1`, `ns2`, and `ns3.nameserver.net.au`. On 2026-10-07, direct authoritative queries returned inconsistent zone data: `ns1` refused the zone; `ns2` returned the older apex A record (`103.42.108.46`) but refused the blog CNAME; `ns3` returned the blog CNAME but refused the apex A query. The provider needs to make all three servers authoritative for the same zone before any apex cutover. This repository has no Git remote yet, so the new site is currently local only.

## User Scenarios

### 1. Song previews a change before publication

Song can run the site locally with a standard HTTP server and check the landing page and project page without DNS, account credentials, or a paid hosting service.

### 2. A visitor opens the public site

After publication, a visitor can open the site at its GitHub Pages address. When `midu.com.au` is connected, the same visitor reaches the site over HTTPS at the custom domain.

### 3. Song keeps the old blog available

Publishing or updating the new site does not alter the old blog repositories, the `blog.midu.com.au` CNAME, or the existing blog archive.

## Functional Requirements

- **INF-001**: Publish the new site from a separate repository; keep the old blog repositories intact.
- **INF-002**: Use a static, dependency-free build for the first release. The checked-in HTML and CSS are the deployable files.
- **INF-003**: Support a local HTTP preview and a temporary GitHub Pages project URL before the apex domain is connected.
- **INF-004**: Use relative internal URLs so navigation works both at a project URL and at a custom domain root.
- **INF-005**: Connect `midu.com.au` only after all delegated nameservers serve one consistent zone and its DNS records, GitHub Pages custom-domain setting, and HTTPS certificate can be verified together.
- **INF-006**: Preserve the `blog.midu.com.au` CNAME and verify the blog after apex DNS changes.
- **INF-007**: Document publishing, domain setup, validation, and rollback steps. No credential or token may be committed.
- **INF-008**: Do not add analytics, forms, server code, or a new paid hosting service for the first release.

## Proposed Architecture

1. Create a new public GitHub repository for this site under `SongGithub` and push this repository's files.
2. Enable GitHub Pages from its default branch root. The project URL gives an immediate public preview.
3. Review and approve public copy, project evidence, contact details, and external links.
4. In that repository's Pages settings, set `midu.com.au` as the custom domain. At the DNS provider, replace the apex's existing web-hosting record with GitHub Pages apex records. Keep the blog CNAME unchanged.
5. Enable enforced HTTPS when GitHub's certificate is ready and validate both domains and key page paths.

GitHub's [custom-domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) is the source of record for the DNS values and setup sequence at deployment time.

## Acceptance Criteria

- The landing page and case study load from a local HTTP server without broken internal assets or links.
- The separate Pages deployment succeeds and those pages load from the temporary project URL on desktop and mobile.
- After domain cutover, `https://midu.com.au/` loads with a valid certificate, the project page loads, and `https://blog.midu.com.au/` still serves the old blog.
- Before domain cutover, `ns1`, `ns2`, and `ns3.nameserver.net.au` all answer authoritatively with the same SOA serial and the expected apex and blog records.
- A single-page change can be published by a commit and undone by reverting that commit.

## Decisions Needed Before Public Launch

- Confirm the GitHub repository name and whether it should be public.
- Approve the site's public copy, first featured project, external profiles, and contact route.
- Choose when to move the apex DNS records to GitHub Pages.
