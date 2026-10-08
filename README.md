# Midu personal site

A dependency-free static site draft for Song Jin. Project descriptions are grounded in already public repositories and writing. Song should review the positioning and project copy and provide an approved contact route before launch.

## Preview

From the repository root, run `python3 -m http.server 8766`, then open `http://127.0.0.1:8766/`.

## Hosting

This repository is published from `main` through GitHub Pages at [the temporary preview](https://blog.midu.com.au/midu-site/). It lives in a separate repository from the older blog. GitHub Pages inherits the blog's custom domain for project sites, so `songgithub.github.io/midu-site/` redirects to the blog hostname. DNS for `midu.com.au` still needs repair before the apex can be connected. See [DEPLOYMENT.md](DEPLOYMENT.md) and the [hosting comparison](specs/002-static-hosting/hosting-options.md).

The site contains no JavaScript, forms, analytics, or third-party font requests.
