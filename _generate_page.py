"""Render content.yaml + templates/ into docs/. Every run replaces docs/, nothing else."""
import shutil
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent
# GitHub Pages can only publish from the repository root or a folder named "docs".
GENERATED = ROOT / "docs"

pages = yaml.safe_load((ROOT / "content.yaml").read_text(encoding="utf-8"))["pages"]

for page in pages:
    folder = page["folder"]
    if not (ROOT / "assets" / folder).is_dir():
        raise SystemExit(f"Folder not found: assets/{folder} (docs/ was not changed)")
    page["filename"] = f"{folder}.html"

# Render everything first, so a template error leaves the old docs/ intact.
env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True)
html = {"index.html": env.get_template("index.template.html").render(pages=pages)}
for page in pages:
    html[page["filename"]] = env.get_template("subpage.template.html").render(page=page)

if GENERATED.exists():
    shutil.rmtree(GENERATED)
shutil.copytree(ROOT / "assets", GENERATED / "assets")
for filename, text in html.items():
    (GENERATED / filename).write_text(text, encoding="utf-8")

print(f"Generated {len(pages)} page(s) in {GENERATED}")
