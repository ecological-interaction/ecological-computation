"""Export the authoritative README and scoped CSS to the existing EI MkDocs site."""
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]

def export(site):
    site = Path(site).resolve()
    if not (site / "mkdocs.yml").is_file():
        raise SystemExit("Expected an existing MkDocs website")
    pages = site / "docs/computation"
    pages.mkdir(parents=True, exist_ok=True)
    for source, target in [("README.md", "index.md"), ("SUITE.md", "SUITE.md"), ("BACKGROUND.md", "BACKGROUND.md"), ("LANDING.md", "LANDING.md")]:
        text = (ROOT / source).read_text()
        (pages / target).write_text("<!-- Generated from ecological-computation/" + source + "; edit the source and rerun scripts/export_website.py. -->\n\n" + text)
    (site / "docs/stylesheets/computation.css").write_text((ROOT / "web/computation.css").read_text())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    export(parser.parse_args().site)
