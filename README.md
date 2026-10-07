# Midu personal site

A dependency-free static site draft for Song Jin. Project descriptions are grounded in already public repositories and writing. Song should review the positioning and project copy and provide an approved contact route before launch.

## Preview

From the repository root, run `python3 -m http.server 8766`, then open `http://127.0.0.1:8766/`.

## Hosting

The files can be published directly from the repository root with GitHub Pages. This repository currently has no remote. Keep the older blog in its existing `songgithub.github.io` repository; a separate repository and Pages site is needed for this site. If the new site uses `midu.com.au`, configure that custom domain on its own Pages site and add the GitHub Pages apex DNS records at the domain provider. Do not point the apex at the blog CNAME.

The site contains no JavaScript, forms, analytics, or third-party font requests.
