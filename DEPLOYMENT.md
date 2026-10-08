# Deployment runbook

The new site is published from the separate public repository `SongGithub/midu-site`. GitHub Pages reports a successful build at `https://blog.midu.com.au/midu-site/`. Because the older `SongGithub/songgithub.github.io` user site uses `blog.midu.com.au`, GitHub Pages applies that hostname to project sites too. The `songgithub.github.io/midu-site/` URL redirects to it. Keep the old blog repository and its CNAME in place.

## 1. Repair DNS before changing the apex

Ask the DNS provider to synchronize the `midu.com.au` zone across all three delegated nameservers. On 2026-10-07, authoritative queries were inconsistent: `ns1` refused the zone's SOA and apex A queries, `ns2` refused the SOA query while serving the older apex A record, and `ns3` served the SOA and apex A record. All three returned the blog CNAME in the latest check. Earlier checks also showed intermittent refusal for the blog record. The provider should confirm identical SOA serials and both expected records on all three servers.

Suggested support request:

> The delegated nameservers for midu.com.au are ns1/ns2/ns3.nameserver.net.au, but they do not consistently serve the same authoritative zone. Please restore/synchronize DNS hosting for the domain on all three servers. Confirm that each server answers authoritatively with the same SOA serial, the current apex A record, and `blog.midu.com.au CNAME songgithub.github.io`. Some direct queries currently return REFUSED, causing visitors on different resolvers to get different results.

Check each server with:

```sh
for ns in ns1.nameserver.net.au ns2.nameserver.net.au ns3.nameserver.net.au; do
  dig "@$ns" +norecurse +noall +comments +answer SOA midu.com.au
  dig "@$ns" +norecurse +noall +comments +answer A midu.com.au
  dig "@$ns" +norecurse +noall +comments +answer CNAME blog.midu.com.au
done
```

Until this is fixed, different visitors can receive different DNS answers. Do not remove the existing blog CNAME during the repair.

## 2. Current GitHub Pages preview

The `main` branch is connected to `https://github.com/SongGithub/midu-site.git`; Pages publishes from the repository root. The homepage and both case-study paths returned HTTP 200 on 2026-10-08. Both the blog and project Pages settings have HTTPS enforcement enabled. Public copy and contact details still need Song's review before calling this the finished site.

The preview inherits the blog hostname. If a visitor's resolver reaches one of the inconsistent nameservers, this preview may fail despite the successful Pages build. A Cloudflare Pages deployment would provide a separate `<project>.pages.dev` preview; see `specs/002-static-hosting/hosting-options.md`.

## 3. Connect `midu.com.au`

If GitHub Pages remains the host, add `midu.com.au` as the custom domain in the new repository's Pages settings. At the DNS provider, replace the apex's previous web-hosting A record with the current GitHub Pages apex values from [GitHub's documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). Preserve `blog.midu.com.au → songgithub.github.io`. Add the domain's `CNAME` file to this repository if GitHub does not create it automatically for branch publishing.

When the certificate is ready, enable **Enforce HTTPS**. Check the apex homepage, both case studies, the temporary Pages URL's redirect, and the old blog from more than one network.

## 4. Update and roll back

For a normal site update, edit the checked-in HTML and CSS, preview locally, and push a commit to `main`. To undo a bad update, revert that commit and push the revert. To undo a domain cutover, first remove the custom domain in Pages settings, then restore the DNS records recorded before the cutover. Keep a copy of the old DNS record set before changing it.
