# Smithsonian Viewer

A static demo site that shows 3D models in the Smithsonian Voyager viewer. A small Python script generates the site from one content file. There is no backend.

## Layout

```text
SmithsonianViewer/
├── _generate_page.py           Generates the site into docs/
├── content.yaml                Pages, titles, descriptions and thumbnails: edit this
├── templates/
│   ├── index.template.html     Layout of the overview page
│   └── subpage.template.html   Layout of a viewer page
├── assets/                     Everything the pages load, copied as a whole
│   ├── style.css               Stylesheet for all pages
│   ├── favicon-hdpi.png        Icon linked from every page
│   ├── favicon.ico
│   └── <folder>/               One folder per viewer page
│       ├── scene.svx.json      Voyager scene
│       ├── scene-image-*.jpg   Scene images, usable as thumbnails
│       ├── *.glb               Models
│       └── articles/           Articles and their images
└── docs/                       The finished site, created by the script: do not edit
    ├── index.html
    ├── <folder>.html           One per page in content.yaml
    └── assets/                 Copy of assets/
```

Every run deletes and rebuilds `docs/`, so any changes made there are lost. Change the files outside it instead.

## Update the site

You need Python with the packages PyYAML and Jinja2.

1. To add a model, copy its folder into `assets/`. It needs a scene file named `scene.svx.json`.
2. Add or change the entry in `content.yaml`. The field descriptions are at the top of that file.
3. Run `python _generate_page.py`.
4. Right-click `docs/index.html` in VS Code and choose **Open with Live Server** to check the result.

The `docs/` folder is self-contained, so it can be deployed on its own.

## Deploy on GitHub Pages

GitHub Pages can publish a branch from only two places: the repository root or a folder named `docs`. That is why the script writes the site to `docs/`. Do not rename the folder, or GitHub Pages cannot find the site.

1. Run the script, then commit and push the `docs/` folder.
2. On GitHub, open the repository's **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose the branch (for example `main`) and the folder **/docs**, and save.

After a minute or two the site is online at the address shown on that page. Every push that changes `docs/` updates it.

## Good to know

- **Assets:** everything in `assets/` is copied to `docs/` and becomes public when deployed, even if `content.yaml` does not list it.
- **External scripts:** the viewer script and fonts load from the internet, so viewing a page requires an internet connection. Their URLs are in the templates.
