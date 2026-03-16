# How to Update This Site

## Project Structure

- `content/` — Your page content written in Markdown
- `static/` — Static assets (images, CSS)
- `template.html` — The HTML wrapper for all pages
- `src/` — The site generator code (don't touch unless extending)
- `public/` — The generated site output (don't edit directly, it gets wiped on each build)

## To Update Content

1. Edit or add Markdown files in `content/`
2. Each file needs an h1 header (e.g. `# My Page Title`)
3. Run `./main.sh` to rebuild the site

## To Update Styling

1. Edit `static/index.css`
2. Run `./main.sh`

## To Update the Page Layout

1. Edit `template.html`
2. Keep `{{ Title }}` and `{{ Content }}` placeholders in place
3. Run `./main.sh`

## To Add Images

1. Drop images into `static/images/`
2. Reference them in Markdown like: `![alt text](/images/filename.png)`
3. Run `./main.sh`

## Running the Site Locally

```sh
./main.sh

Then visit http://localhost:8888 in your browser.
```
