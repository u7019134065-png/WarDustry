#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path("/home/ubuntu/wardustry")

STEEL_DARK = (32, 36, 38, 255)
STEEL = (58, 64, 68, 255)
STEEL_LIGHT = (94, 103, 108, 255)
OLIVE = (78, 88, 52, 255)
OLIVE_LIGHT = (118, 132, 78, 255)
SCARLET = (184, 52, 46, 255)
SCARLET_DARK = (102, 24, 22, 255)
WHITE = (228, 232, 226, 255)
BLACK = (16, 18, 19, 255)


def save(img, rel):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, format="PNG")


def base_canvas(size):
    return Image.new("RGBA", (size, size), (0, 0, 0, 0))


def make_unit_body(size):
    img = base_canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    pad = 8
    body = [
        (c, pad),
        (size - pad - 4, c - 6),
        (c + 8, size - pad - 10),
        (c, size - pad - 4),
        (c - 8, size - pad - 10),
        (pad + 4, c - 6),
    ]
    d.polygon(body, fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, pad + 5), (size - pad - 11, c - 6), (c + 6, size - pad - 15), (c, size - pad - 10), (c - 6, size - pad - 15), (pad + 11, c - 6)], fill=STEEL)
    d.line((c, pad + 2, c, size - pad - 5), fill=STEEL_LIGHT, width=2)
    d.polygon([(c - 1, pad), (c + 1, pad), (c + 5, pad + 9), (c - 5, pad + 9)], fill=SCARLET)
    d.polygon([(c - 2, size - pad - 4), (c + 2, size - pad - 4), (c + 4, size - pad + 2), (c - 4, size - pad + 2)], fill=SCARLET_DARK)
    d.polygon([(c - 13, c - 5), (c - 30, c - 15), (c - 34, c - 7), (c - 17, c + 2)], fill=OLIVE, outline=BLACK)
    d.polygon([(c + 13, c - 5), (c + 30, c - 15), (c + 34, c - 7), (c + 17, c + 2)], fill=OLIVE, outline=BLACK)
    d.ellipse((c - 4, c - 4, c + 4, c + 4), fill=SCARLET, outline=BLACK)
    return img


def make_unit_cell(size):
    img = base_canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    d.rounded_rectangle((c - 7, c - 5, c + 7, c + 6), radius=3, fill=WHITE, outline=(220, 198, 198, 255), width=2)
    d.rounded_rectangle((c - 4, c - 2, c + 4, c + 3), radius=2, fill=(220, 198, 198, 255))
    return img


def make_weapon(size=24):
    img = base_canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 2), (size - 4, c), (c, size - 4), (4, c)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 5), (size - 8, c), (c, size - 8), (8, c)], fill=STEEL, outline=STEEL_LIGHT)
    d.ellipse((c - 3, c - 3, c + 3, c + 3), fill=SCARLET, outline=BLACK)
    return img


def make_factory_base(size):
    img = base_canvas(size)
    d = ImageDraw.Draw(img)
    m = 8
    d.rounded_rectangle((m, m + 4, size - m, size - m), radius=10, fill=STEEL_DARK, outline=BLACK, width=3)
    d.rectangle((m + 8, m + 12, size - m - 8, size - m - 10), fill=STEEL)
    d.polygon([(m + 10, size - m - 8), (size // 2, m + 18), (size - m - 10, size - m - 8)], fill=OLIVE, outline=BLACK)
    d.line((m + 12, size - m - 16, size - m - 12, size - m - 16), fill=SCARLET, width=3)
    for x in range(m + 12, size - m - 10, 18):
        for y in range(m + 12, size - m - 10, 18):
            d.ellipse((x, y, x + 3, y + 3), fill=BLACK)
    return img


def make_factory_top(size):
    img = base_canvas(size)
    d = ImageDraw.Draw(img)
    m = 10
    d.rounded_rectangle((m + 8, m, size - m - 8, size - m - 4), radius=6, fill=STEEL_LIGHT, outline=BLACK, width=2)
    d.polygon([(size // 2, m + 4), (size // 2 + 20, size // 2), (size // 2, size - m - 4), (size // 2 - 20, size // 2)], fill=OLIVE_LIGHT, outline=BLACK)
    d.rectangle((size // 2 - 3, size // 2 - 18, size // 2 + 3, size // 2 + 10), fill=SCARLET)
    d.polygon([(size // 2 - 10, size // 2 + 10), (size // 2 + 10, size // 2 + 10), (size // 2, size // 2 + 24)], fill=SCARLET_DARK)
    return img


def main():
    save(make_unit_body(64), "sprites/units/shahed.png")
    save(make_unit_cell(64), "sprites/units/shahed-cell.png")
    save(make_weapon(24), "sprites/units/weapons/wardustry-shahed-warhead.png")
    save(make_factory_base(96), "sprites/blocks/drone-factory.png")
    save(make_factory_top(96), "sprites/blocks/drone-factory-top.png")


if __name__ == "__main__":
    main()
