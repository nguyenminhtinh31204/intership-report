# Internship Report

Hugo static site generated from `https://workshop-sample.awsfcaj.com/`.

## Structure

- `content/`: Markdown pages for English and Vietnamese.
- `static/`: Images, CSS, JavaScript, fonts, and downloaded assets.
- `layouts/`: Project-level Hugo overrides.
- `themes/hugo-theme-learn/`: Local Hugo Learn theme.
- `config/_default/hugo.toml`: Site configuration.
- `scripts/import_sample_site.py`: Import script used to regenerate Markdown from the sample site.

## Local Development

```powershell
hugo server -D
```

## Build

```powershell
hugo --minify
```

## Deploy To GitHub Pages

1. Update `baseURL` in `config/_default/hugo.toml` to your GitHub Pages URL.
2. Push this repository to GitHub.
3. In GitHub, open `Settings` > `Pages` and choose `GitHub Actions`.
4. Push to `main`; the workflow in `.github/workflows/deploy-pages.yml` publishes the site.
