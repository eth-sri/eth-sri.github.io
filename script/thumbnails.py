# /// script
# requires-python = ">=3.11"
# dependencies = ["Pillow==12.3.0", "tabulate==0.9.0"]
# ///
"""Generate committed image variants for GitHub Pages: uv run script/thumbnails.py."""

import hashlib
import json
import re
from pathlib import Path

from PIL import Image, ImageOps
from tabulate import tabulate

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "_data/thumbnails.json"
OUTPUT = ROOT / "assets/generated/thumbnails"
DIRECTORIES = ("images", "projects", "media", "blog")
WIDTHS = (320, 640, 1280)
QUALITY = 85


def main():
    previous = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    manifest = {}
    generated = 0
    original_bytes = 0
    thumbnail_bytes = 0
    for directory in DIRECTORIES:
        for source in sorted((ROOT / "assets" / directory).rglob("*")):
            if source.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
                continue
            url = "/" + source.relative_to(ROOT).as_posix()
            widths = (*WIDTHS, 1920) if "/group-2023/" in url else WIDTHS
            digest = hashlib.sha256(
                source.read_bytes() + f"{url}:{widths}:{QUALITY}:v1".encode()
            ).hexdigest()[:16]
            cached = previous.get(url)
            if cached and cached["digest"] == digest and all(
                (ROOT / variant["url"].lstrip("/")).exists()
                for variant in cached["variants"]
            ):
                entry = cached
            else:
                with Image.open(source) as image:
                    # Preserve animations by serving their originals.
                    if getattr(image, "is_animated", False):
                        continue
                    image = ImageOps.exif_transpose(image)
                    image = image.convert("RGBA" if image.has_transparency_data else "RGB")
                    variants = []
                    OUTPUT.mkdir(parents=True, exist_ok=True)
                    for width in sorted({min(width, image.width) for width in widths}):
                        height = max(1, round(image.height * width / image.width))
                        resized = image.resize((width, height), Image.Resampling.LANCZOS)
                        destination = OUTPUT / f"{digest}-{width}.webp"
                        resized.save(destination, quality=QUALITY, method=6)
                        variants.append({
                            "url": "/" + destination.relative_to(ROOT).as_posix(),
                            "width": width,
                        })
                        generated += 1
                    entry = {
                        "digest": digest,
                        "width": image.width,
                        "height": image.height,
                        "src": next((v["url"] for v in variants if v["width"] >= 640), variants[-1]["url"]),
                        "variants": variants,
                    }
            manifest[url] = entry
            original_bytes += source.stat().st_size
            thumbnail_bytes += (ROOT / entry["src"].lstrip("/")).stat().st_size
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    needed = {
        ROOT / variant["url"].lstrip("/")
        for entry in manifest.values()
        for variant in entry["variants"]
    }
    removed = 0
    for path in OUTPUT.glob("*.webp"):
        if re.fullmatch(r"[0-9a-f]{16}-\d+\.webp", path.name) and path not in needed:
            path.unlink()
            removed += 1
    print(tabulate([
        ["Images", len(manifest)],
        ["New variants", generated],
        ["Obsolete variants removed", removed],
        ["Originals (MiB)", f"{original_bytes / 1024**2:.2f}"],
        ["Default thumbnails (MiB)", f"{thumbnail_bytes / 1024**2:.2f}"],
    ], headers=["Metric", "Value"]))


if __name__ == "__main__":
    main()
