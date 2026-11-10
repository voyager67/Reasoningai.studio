# ReasoningAI website

Static public website for [reasoningai.tech](https://reasoningai.tech).

## Cloudflare Pages deployment

This website lives in the `website/` directory so it can be deployed independently from the ReasoningAI Studio source code in the repository root.

Create a new Cloudflare Pages project connected to `voyager67/Reasoningai.studio` and configure:

| Setting | Value |
| --- | --- |
| Production branch | `main` |
| Root directory | `website` |
| Framework preset | None |
| Build command | Leave blank |
| Build output directory | `.` |

After the first successful deployment, open **Workers & Pages → project → Custom domains** and add `reasoningai.tech`. Add `www.reasoningai.tech` as a redirect or an additional domain if you intend to serve both hostnames.

## Local preview

From this directory, run:

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

No package installation, API key, backend, build step, analytics beacon, or third-party runtime is required. The stylesheet uses a system fallback stack if the optional Google Fonts import is blocked; remove the import at the top of `styles.css` for a fully self-hosted font setup.

## Content accuracy

The site describes ReasoningAI as an early-stage research and engineering initiative. Research themes are presented as areas of exploration, not validated breakthroughs. Project counts and capabilities refer to the public ReasoningAI Studio repository and should be reviewed against its README when that project changes.