# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Custom Python static site generator for [andykong.org](https://andykong.org). Uses **Flask + flask-flatpages + flask-frozen**: Flask defines routes, flatpages reads Markdown content from `pages/`, and Freezer crawls all routes to produce static HTML in `andykong.org/public/`.

## Python Environment

In-repo virtualenv at `personalwebsite/` (the subdirectory). No `requirements.txt`; packages: `flask`, `flask-flatpages`, `flask-frozen`, `feedgen`, `beautifulsoup4`, `lxml`, `pytz`.

## Commands

| Command | What it does |
|---------|-------------|
| `personalwebsite/bin/python sitebuilder.py` | Dev server at http://localhost:8001 with live reload |
| `personalwebsite/bin/python sitebuilder.py build` | Freeze site to `andykong.org/public/` (no deploy) |
| `personalwebsite/bin/python sitebuilder.py build local` | Full deploy: freeze → git commit → push → ping Google sitemap |

There are no automated tests.

## Directory Structure

- `sitebuilder.py` — Flask app + build script (the only entry point)
- `pages/blog/` — Blog post Markdown files (label: `blog` or `log`)
- `pages/projects/` — Project write-up Markdown files (label: `project`)
- `pages/now.md` — Custom-format "Now" page data (NOT standard FlatPages YAML)
- `templates/` — Jinja2 HTML templates
- `static/` — All images, videos, JS, CSS assets
- `andykong.org/public/` — Frozen static output (committed to git, deployed via push)
- `bloggui/` — Draft/staging area, NOT served
- `archive/` — Retired posts, NOT served
- `newblogpost.sh` — Helper script to create a new blog post from `blogtemplate.md`

## Content Front Matter

Blog posts (`pages/blog/*.md`):
```yaml
title: Post Title
date: 2024-01-15
label: blog          # or "log" for technical posts
tags: [tag1, tag2]   # "wip" tag hides from listings/RSS/sitemap
snippet: One-sentence summary for the blog index
```

Projects (`pages/projects/*.md`):
```yaml
title: Project Name
date: 2024-01-15
label: project
timespan: Jan 2024 - ongoing
pic: filename.png     # hero image for homepage grid (can be .mp4/.mov)
description: Short description shown on the homepage
```

**Critical**: `label` must match content type. A blog post labeled `project` crashes with a `pic` attribute error.

## Jinja2 Helpers in Markdown

Content is pre-rendered as Jinja2 before Markdown conversion, so these work inside `.md` files:

```
{{ add_pic("filename.png", "Caption text") }}
{{ add_vid("filename.mp4", width="75%", speed=0.5, autoplay=False) }}
{{ tableofcontents("blog/filename.md") }}
{{ url_for("static", filename="file.png") }}
```

## Template Hierarchy

```
base.html                  ← navbar, Bootstrap 4, Atkinson Hyperlegible font, analytics
├── main.html              ← homepage: hero + project grid
├── aboutsidebar.html      ← two-column layout with sticky sidebar + social icons
│   └── blogmain.html      ← blog index
├── noaboutsidebar.html    ← full-width centered content (max-width: 50em)
│   └── blog.html          ← single blog post (loads MathJax)
└── projects.html          ← single project page
```

## Key Behaviors / Gotchas

1. **`wip` tag**: Posts tagged `wip` are excluded from blog index, sitemap, and RSS feed. Use for drafts.
2. **Future-dated projects**: Automatically hidden from homepage and projects index.
3. **`now.md` custom format**: Double-newline-delimited entries with `image:`, `place:`, `start:`, `endat:` keys and `- ` prefixed content lines. Parsed manually in the `now()` route handler.
4. **Lazy loading**: `<img loading="lazy">` is injected automatically in blog/project route handlers.
5. **H1/H2 anchors**: BeautifulSoup adds `id` attributes to `h1`/`h2` tags for TOC anchor links.
6. **iCloud static files**: `sitebuilder.py build local` auto-downloads `.icloud` stubs before freezing.

## Deployment

- Output goes to `andykong.org/public/` (frozen static files tracked in git)
- Deployed via `git push origin master`
- `.gitignore` ignores `andykong.org/*` except `andykong.org/public/`
- Firebase config exists but is unused (dropped Oct 2022)
- Analytics: Google Analytics (`G-YNX5JQZWHT`) + GoatCounter (`kong.goatcounter.com`) in `base.html`
