# AGENTS.md

Guidance for coding agents working in this repository.

## Project Overview

This is Andy Kong's personal website source. It is a custom Python static site generator built around Flask, Flask-FlatPages, Flask-Frozen, FeedGen, and BeautifulSoup.

The source content lives mostly in Markdown under `pages/`. `sitebuilder.py` defines the Flask routes, renders Markdown through Jinja first, and can freeze the site into static HTML.

## Repository Map

- `sitebuilder.py` - main Flask app, Markdown renderer, route definitions, RSS, sitemap, and build/deploy entry point.
- `pages/blog/` - served blog/log Markdown posts.
- `pages/projects/` - served project Markdown pages.
- `pages/now.md` - manually parsed Now page data; this is not normal FlatPages front matter.
- `templates/` - Jinja templates used by `sitebuilder.py`.
- `static/` - images, videos, CSS, JS, fonts, and other served assets.
- `andykong.org/public/` - frozen static output used for deployment and tracked in git.
- `bloggui/` - local CKEditor-based draft helper app, not part of the public site routes.
- `archive/` and `junk/` - old, unused, or scratch content; do not treat these as served pages.
- `blogtemplate.md` and `projecttemplate.md` - starter front matter examples.
- `newblogpost.sh` - local helper for creating a new blog post from `blogtemplate.md`.

## Python Environment

Use the virtualenvwrapper environment:

```bash
~/.virtualenvs/personalwebsite/bin/python sitebuilder.py
```

The in-repo `personalwebsite/` directory is an old broken Python 2.7 virtualenv and should not be used. There is no `requirements.txt` in this repo. Existing imports indicate these runtime packages: `flask`, `flask-flatpages`, `flask-frozen`, `feedgen`, `beautifulsoup4`, `lxml`, and `pytz`. The `bloggui/` helper additionally uses `flask-ckeditor`.

## Commands

```bash
# Run the website locally on http://localhost:8001
~/.virtualenvs/personalwebsite/bin/python sitebuilder.py

# Freeze with Flask-Frozen's default destination unless configured
~/.virtualenvs/personalwebsite/bin/python sitebuilder.py build

# Deploy path used by Andy's local machine: downloads iCloud static stubs,
# freezes into andykong.org/public/, commits, pushes master, and pings Google.
~/.virtualenvs/personalwebsite/bin/python sitebuilder.py build local
```

Do not run `~/.virtualenvs/personalwebsite/bin/python sitebuilder.py build local` unless the user explicitly asks for a deploy. It mutates git state and pushes to `origin master`.

There are no automated tests. For code/template changes, at minimum run the dev server or freeze command and check the affected routes.

## Content Rules

Blog/log posts in `pages/blog/*.md` use YAML-style FlatPages metadata:

```yaml
title: Post Title
date: 2024-01-15
label: blog
tags: [tag1, tag2]
snippet: One-sentence summary for listings and RSS
```

Use `label: blog` for less technical posts and `label: log` for technical posts. The `/blog/` index currently selects labels containing `log`, which includes both `blog` and `log`.

Project pages in `pages/projects/*.md` use:

```yaml
title: Project Name
date: 2024-01-15
label: project
timespan: Jan 2024 - ongoing
pic: filename.png
description: Short homepage/project-card description
```

Important content gotchas:

- Keep `label` correct. A blog post marked `project` can crash homepage/project rendering because project templates expect `pic`, `timespan`, and `description`.
- Posts tagged `wip` are intentionally hidden from blog listings, RSS, and sitemap.
- Future-dated projects are hidden from project listings/homepage.
- `pages/now.md` is double-newline-delimited custom data. Each entry begins with `image:`, `place:`, `start:`, and `endat:`, followed by content lines prefixed with `- `.
- Markdown body content is pre-rendered as Jinja before Markdown conversion, so helpers like `url_for`, `add_pic`, `add_vid`, and `tableofcontents` are valid inside Markdown files.

Common Markdown helpers:

```jinja
{{ add_pic("filename.png", "Caption text") }}
{{ add_vid("filename.mp4", width="75%", speed=0.5, autoplay=False) }}
{{ tableofcontents("blog/filename.md") }}
{{ url_for("static", filename="file.png") }}
```

## Rendering Behavior

- `prerender_jinja()` in `sitebuilder.py` runs Jinja first, converts Markdown, then uses BeautifulSoup to add `id` attributes to `h1` and `h2` elements.
- Blog and project route handlers inject `loading="lazy"` into rendered images.
- Single blog pages load MathJax from a CDN.
- RSS is generated at `/rss.xml`; sitemap is generated at `/sitemap.xml`.
- Route paths generally keep trailing slashes in Flask routes, while the sitemap template handles canonical-looking output.

## Template Notes

- `templates/base.html` owns the global dark theme, nav, Bootstrap 4, font loading, Font Awesome, instantpage, Google Analytics, and GoatCounter.
- `templates/main.html` is the homepage and project grid.
- `templates/blogmain.html` is the blog/log listing.
- `templates/blog.html` renders single blog posts.
- `templates/projects.html` renders single project pages.
- `templates/projectsmain.html` renders the older project grid view.
- Keep CSS changes consistent with the existing simple dark theme: background `#202222`, text `#FAEADB`, cyan links, squared media, minimal rounding.

## Working Guidelines

- Prefer small, localized edits. This is a hand-rolled site generator with many content assumptions.
- Do not make broad formatting passes over Markdown posts; preserve the author's voice and hand-written HTML/Jinja.
- Do not edit generated files under `andykong.org/public/` unless the user asked for a build/deploy or explicitly wants generated output updated.
- Do not treat `bloggui/`, `archive/`, or `junk/` as live site content unless the user specifically references them.
- When adding assets, put them in `static/` and reference them through `url_for("static", filename="...")` or the existing helpers.
- Avoid introducing new frameworks or build tools unless explicitly requested.
- If changing routes, metadata expectations, RSS, sitemap, or build behavior, verify with a local run or freeze because errors often surface only during page rendering.
