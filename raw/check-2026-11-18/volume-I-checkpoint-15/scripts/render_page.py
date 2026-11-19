"""Render one authority page at 400 dpi, with navigation images and exact crops.

This tool never records a page as checked. The reviewer must inspect the images.
All input/output locations are supplied by the caller.
"""
import argparse
from pathlib import Path
import fitz
from PIL import Image

p = argparse.ArgumentParser()
p.add_argument("pdf", type=Path)
p.add_argument("page", type=int, help="one-based PDF page")
p.add_argument("output", type=Path)
p.add_argument("--crop", nargs=4, type=float, metavar=("X0", "Y0", "X1", "Y1"))
args = p.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
with fitz.open(args.pdf) as doc:
    page = doc[args.page - 1]
    rect = fitz.Rect(args.crop) if args.crop else page.rect
    pix = page.get_pixmap(dpi=400, clip=rect, alpha=False)
    image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    image.save(args.output / "render400.png", dpi=(400, 400))
    overview = image.copy()
    overview.thumbnail((1400, 2200))
    overview.save(args.output / "overview.jpg", quality=95)
    h = image.height
    for n, (y0, y1) in enumerate(((0, h//2+80), (h//2-80, h)), 1):
        image.crop((0, y0, image.width, y1)).save(args.output / f"half{n}.jpg", quality=98, dpi=(400, 400))
    print(f"Rendered PDF page {args.page} at 400 dpi: {image.width} x {image.height} pixels.")
