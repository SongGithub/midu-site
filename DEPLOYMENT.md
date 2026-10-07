# Deployment runbook

The new site is currently local only. The older blog is published separately from `SongGithub/songgithub.github.io`; leave that repository and its `blog.midu.com.au` CNAME in place.

## 1. Repair DNS before changing the apex

Ask the DNS provider to synchronize the `midu.com.au` zone across all three delegated nameservers. On 2026-10-07, `ns1.nameserver.net.au` returned `REFUSED` for the zone, `ns2` served only an older apex A record, and `ns3` served the new blog CNAME. The provider should confirm identical SOA serials and both records on all three servers.

Check each server with:

```sh
for ns in ns1.nameserver.net.au ns2.nameserver.net.au ns3.nameserver.net.au; do
  dig "@$ns" +norecurse +noall +comments +answer SOA midu.com.au
  dig "@$ns" +norecurse +noall +comments +answer A midu.com.au
  dig "@$ns" +norecurse +noall +comments +answer CNAME blog.midu.com.au
done
```

Until this is fixed, different visitors can receive different DNS answers. Do not remove the existing blog CNAME during the repair.

## 2. Publish a temporary Pages address

After Song reviews the public copy and confirms a contact route, create a **separate** public GitHub repository under `SongGithub` for this site's files. Push the `main` branch, then set **Settings → Pages → Deploy from a branch → main → /(root)**. Open both the homepage and each case-study page at the project URL. Internal paths are relative so they work under a repository path.

The repository name is still to be chosen. No remote is configured here yet. No build command, package install, secret, or GitHub Actions workflow is needed for this static version.

## 3. Connect `midu.com.au`

In the new repository's Pages settings, add `midu.com.au` as the custom domain. At the DNS provider, replace the apex's previous web-hosting A record with the current GitHub Pages apex values from [GitHub's documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). Preserve `blog.midu.com.au → songgithub.github.io`. Add the domain's `CNAME` file to this repository if GitHub does not create it automatically for branch publishing.

When the certificate is ready, enable **Enforce HTTPS**. Check the apex homepage, both case studies, the temporary Pages URL's redirect, and the old blog from more than one network.

## 4. Update and roll back

For a normal site update, edit the checked-in HTML and CSS, preview locally, and push a commit to `main`. To undo a bad update, revert that commit and push the revert. To undo a domain cutover, first remove the custom domain in Pages settings, then restore the DNS records recorded before the cutover. Keep a copy of the old DNS record set before changing it.
