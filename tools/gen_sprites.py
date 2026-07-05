#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path('/home/ubuntu/wardustry')

STEEL_DARK = (32, 36, 38, 255)
STEEL = (58, 64, 68, 255)
STEEL_LIGHT = (94, 103, 108, 255)
OLIVE = (78, 88, 52, 255)
OLIVE_LIGHT = (118, 132, 78, 255)
SCARLET = (184, 52, 46, 255)
SCARLET_DARK = (102, 24, 22, 255)
WHITE = (228, 232, 226, 255)
BLACK = (16, 18, 19, 255)
DARK_GREEN = (46, 58, 40, 255)
SAND = (102, 96, 72, 255)

def save(img, rel):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, format='PNG')

def canvas(size):
    return Image.new('RGBA', (size, size), (0, 0, 0, 0))

def layer_glow(size, box, color, blur=6):
    lay = canvas(size)
    d = ImageDraw.Draw(lay)
    d.ellipse(box, fill=color)
    return lay.filter(ImageFilter.GaussianBlur(blur))

def overlay(base, over):
    return Image.alpha_composite(base, over)

def body_drone(size, points, inner=None, accents=None):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    d.polygon(points, fill=STEEL_DARK, outline=BLACK)
    if inner:
        d.polygon(inner, fill=STEEL)
    if accents:
        for shape, fill in accents:
            d.polygon(shape, fill=fill)
    return img

def cell_drone(size, w=16, h=10):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    d.rounded_rectangle((c - w//2, c - h//2, c + w//2, c + h//2), radius=max(2, h//3), fill=WHITE, outline=(220, 198, 198, 255), width=2)
    d.rounded_rectangle((c - w//4, c - h//4, c + w//4, c + h//4), radius=max(1, h//4), fill=(220, 198, 198, 255))
    return img

def weapon_icon(size, kind='default'):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    if kind == 'bomb':
        d.ellipse((c - 5, c - 5, c + 5, c + 5), fill=STEEL_DARK, outline=BLACK)
        d.polygon([(c, 4), (c + 4, 10), (c, 16), (c - 4, 10)], fill=SCARLET)
    elif kind == 'missile':
        d.polygon([(c, 2), (size - 5, c), (c, size - 5), (5, c)], fill=STEEL_DARK, outline=BLACK)
        d.polygon([(c, 5), (size - 8, c), (c, size - 8), (8, c)], fill=STEEL)
        d.ellipse((c - 2, c - 2, c + 2, c + 2), fill=SCARLET)
    elif kind == 'autocannon':
        d.rounded_rectangle((5, 7, size - 5, size - 7), radius=4, fill=STEEL_DARK, outline=BLACK)
        d.rectangle((size - 8, c - 2, size - 3, c + 2), fill=SCARLET)
        d.rectangle((3, c - 1, 8, c + 1), fill=OLIVE_LIGHT)
    elif kind == 'antiair':
        d.polygon([(c, 2), (size - 4, c), (c, size - 4), (4, c)], fill=STEEL_DARK, outline=BLACK)
        d.line((c, 5, c, size - 5), fill=SCARLET, width=2)
        d.line((5, c, size - 5, c), fill=OLIVE_LIGHT, width=2)
    elif kind == 'warhead':
        d.polygon([(c, 2), (size - 4, c), (c, size - 4), (4, c)], fill=STEEL_DARK, outline=BLACK)
        d.polygon([(c, 6), (size - 8, c), (c, size - 8), (8, c)], fill=STEEL)
        d.ellipse((c - 3, c - 3, c + 3, c + 3), fill=SCARLET, outline=BLACK)
    else:
        d.polygon([(c, 2), (size - 4, c), (c, size - 4), (4, c)], fill=STEEL_DARK, outline=BLACK)
        d.ellipse((c - 3, c - 3, c + 3, c + 3), fill=SCARLET, outline=BLACK)
    return img

def make_kamikaze_body(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (14, 10, 50, 42), (184, 52, 46, 70), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (48, 18), (40, 50), (c, 56), (24, 50), (16, 18)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 13), (45, 20), (38, 46), (c, 50), (26, 46), (19, 20)], fill=STEEL)
    d.polygon([(c, 8), (c + 4, 15), (c - 4, 15)], fill=SCARLET)
    d.polygon([(18, 24), (10, 30), (12, 34), (20, 28)], fill=OLIVE, outline=BLACK)
    d.polygon([(46, 24), (54, 30), (52, 34), (44, 28)], fill=OLIVE, outline=BLACK)
    d.rectangle((c - 2, 50, c + 2, 58), fill=SCARLET_DARK)
    return img

def make_recon_body(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (12, 12, 52, 38), (118, 132, 78, 60), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 10), (50, 22), (44, 34), (c, 46), (20, 34), (14, 22)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 14), (46, 23), (41, 32), (c, 42), (23, 32), (18, 23)], fill=STEEL)
    d.rectangle((c - 2, 8, c + 2, 12), fill=OLIVE_LIGHT)
    d.line((c, 8, c, 2), fill=OLIVE_LIGHT, width=2)
    d.ellipse((c - 3, 6, c + 3, 12), fill=SCARLET, outline=BLACK)
    d.polygon([(18, 26), (10, 30), (12, 33), (20, 29)], fill=OLIVE, outline=BLACK)
    d.polygon([(46, 26), (54, 30), (52, 33), (44, 29)], fill=OLIVE, outline=BLACK)
    return img

def make_bomber_body(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (10, 10, 54, 50), (184, 52, 46, 60), 8))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (52, 20), (44, 46), (c, 56), (20, 46), (12, 20)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 13), (47, 22), (40, 42), (c, 50), (24, 42), (17, 22)], fill=STEEL)
    d.polygon([(c - 3, 18), (c + 3, 18), (c + 6, 30), (c - 6, 30)], fill=SCARLET)
    d.polygon([(14, 28), (7, 34), (11, 37), (18, 31)], fill=OLIVE, outline=BLACK)
    d.polygon([(50, 28), (57, 34), (53, 37), (46, 31)], fill=OLIVE, outline=BLACK)
    d.ellipse((c - 5, 39, c + 5, 49), fill=SAND, outline=BLACK)
    return img

def make_missile_body(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (12, 12, 52, 40), (58, 64, 68, 60), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (50, 20), (42, 44), (c, 54), (22, 44), (14, 20)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 13), (46, 22), (39, 40), (c, 48), (25, 40), (18, 22)], fill=STEEL)
    d.polygon([(c, 8), (c + 6, 18), (c - 6, 18)], fill=SCARLET)
    d.polygon([(16, 26), (8, 30), (14, 35), (20, 31)], fill=OLIVE_LIGHT, outline=BLACK)
    d.polygon([(48, 26), (56, 30), (50, 35), (44, 31)], fill=OLIVE_LIGHT, outline=BLACK)
    d.line((c, 20, c, 46), fill=SCARLET, width=2)
    return img

def make_gunship_body(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (10, 10, 54, 44), (32, 36, 38, 60), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (50, 18), (48, 40), (c, 56), (16, 40), (14, 18)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 12), (46, 20), (44, 36), (c, 50), (20, 36), (18, 20)], fill=STEEL)
    d.rectangle((c - 10, 24, c + 10, 30), fill=OLIVE, outline=BLACK)
    d.rectangle((c - 2, 14, c + 2, 44), fill=SCARLET)
    d.polygon([(12, 24), (8, 32), (12, 36), (18, 28)], fill=OLIVE, outline=BLACK)
    d.polygon([(52, 24), (56, 32), (52, 36), (46, 28)], fill=OLIVE, outline=BLACK)
    d.ellipse((c - 4, 38, c + 4, 46), fill=SCARLET_DARK, outline=BLACK)
    return img

def make_interceptor_body(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (14, 10, 50, 38), (118, 132, 78, 60), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (48, 18), (42, 30), (c, 50), (22, 30), (16, 18)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 13), (45, 20), (40, 28), (c, 44), (24, 28), (19, 20)], fill=STEEL)
    d.polygon([(c - 3, 10), (c + 3, 10), (c + 7, 17), (c - 7, 17)], fill=SCARLET)
    d.polygon([(16, 20), (8, 24), (12, 28), (20, 24)], fill=OLIVE_LIGHT, outline=BLACK)
    d.polygon([(48, 20), (56, 24), (52, 28), (44, 24)], fill=OLIVE_LIGHT, outline=BLACK)
    d.line((c, 18, c, 40), fill=WHITE, width=2)
    return img

def make_jeep_body(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (10, 18, 54, 46), (58, 64, 68, 50), 6))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((14, 20, 50, 42), radius=5, fill=STEEL_DARK, outline=BLACK, width=2)
    d.polygon([(18, 20), (28, 12), (42, 12), (46, 20)], fill=OLIVE, outline=BLACK)
    d.rectangle((22, 23, 42, 32), fill=STEEL)
    d.rectangle((20, 32, 44, 36), fill=STEEL_LIGHT)
    d.rectangle((26, 25, 29, 30), fill=SCARLET)
    d.rectangle((35, 25, 38, 30), fill=SCARLET)
    for x in (16, 48):
        d.ellipse((x - 5, 36, x + 5, 46), fill=BLACK)
        d.ellipse((x - 3, 38, x + 3, 44), fill=STEEL)
    d.rectangle((10, 29, 54, 31), fill=OLIVE_LIGHT)
    d.rectangle((29, 17, 35, 20), fill=SCARLET)
    return img

def make_bus_body(size=96):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (10, 22, 86, 66), (58, 64, 68, 50), 7))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((12, 22, 84, 62), radius=8, fill=STEEL_DARK, outline=BLACK, width=3)
    d.rectangle((18, 28, 78, 34), fill=OLIVE)
    d.rectangle((18, 36, 78, 52), fill=STEEL)
    for x in range(20, 76, 12):
        d.rectangle((x, 30, x + 6, 46), fill=STEEL_LIGHT)
    d.rectangle((24, 40, 72, 44), fill=SCARLET)
    d.rectangle((15, 24, 81, 27), fill=OLIVE_LIGHT)
    for x in (24, 72):
        d.ellipse((x - 8, 54, x + 8, 70), fill=BLACK)
        d.ellipse((x - 5, 57, x + 5, 67), fill=STEEL)
    d.rectangle((8, 44, 88, 47), fill=BLACK)
    d.rectangle((43, 18, 53, 22), fill=SCARLET)
    return img

def make_shahed(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (14, 8, 50, 44), (184, 52, 46, 80), 8))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (49, 20), (39, 54), (c, 58), (25, 54), (15, 20)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 13), (46, 22), (37, 50), (c, 54), (27, 50), (18, 22)], fill=STEEL)
    d.polygon([(c, 8), (c + 4, 16), (c - 4, 16)], fill=SCARLET)
    d.rectangle((c - 2, 54, c + 2, 60), fill=SCARLET_DARK)
    d.polygon([(18, 26), (8, 30), (10, 34), (20, 30)], fill=OLIVE, outline=BLACK)
    d.polygon([(46, 26), (56, 30), (54, 34), (44, 30)], fill=OLIVE, outline=BLACK)
    d.polygon([(c - 2, 52), (c + 2, 52), (c + 8, 62), (c - 8, 62)], fill=BLACK)
    return img

def make_recon(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (12, 12, 52, 38), (118, 132, 78, 70), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 10), (50, 22), (44, 34), (c, 46), (20, 34), (14, 22)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 14), (46, 23), (41, 32), (c, 42), (23, 32), (18, 23)], fill=STEEL)
    d.rectangle((c - 2, 8, c + 2, 12), fill=OLIVE_LIGHT)
    d.line((c, 8, c, 2), fill=OLIVE_LIGHT, width=2)
    d.ellipse((c - 3, 6, c + 3, 12), fill=SCARLET, outline=BLACK)
    d.polygon([(18, 26), (10, 30), (12, 33), (20, 29)], fill=OLIVE, outline=BLACK)
    d.polygon([(46, 26), (54, 30), (52, 33), (44, 29)], fill=OLIVE, outline=BLACK)
    return img

def make_bomber(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (10, 10, 54, 50), (184, 52, 46, 60), 8))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (52, 20), (44, 46), (c, 56), (20, 46), (12, 20)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 13), (47, 22), (40, 42), (c, 50), (24, 42), (17, 22)], fill=STEEL)
    d.polygon([(c - 3, 18), (c + 3, 18), (c + 6, 30), (c - 6, 30)], fill=SCARLET)
    d.polygon([(14, 28), (7, 34), (11, 37), (18, 31)], fill=OLIVE, outline=BLACK)
    d.polygon([(50, 28), (57, 34), (53, 37), (46, 31)], fill=OLIVE, outline=BLACK)
    d.ellipse((c - 5, 39, c + 5, 49), fill=SAND, outline=BLACK)
    return img

def make_missile(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (12, 12, 52, 40), (58, 64, 68, 70), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (50, 20), (42, 44), (c, 54), (22, 44), (14, 20)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 13), (46, 22), (39, 40), (c, 48), (25, 40), (18, 22)], fill=STEEL)
    d.polygon([(c, 8), (c + 6, 18), (c - 6, 18)], fill=SCARLET)
    d.polygon([(16, 26), (8, 30), (14, 35), (20, 31)], fill=OLIVE_LIGHT, outline=BLACK)
    d.polygon([(48, 26), (56, 30), (50, 35), (44, 31)], fill=OLIVE_LIGHT, outline=BLACK)
    d.line((c, 20, c, 46), fill=SCARLET, width=2)
    return img

def make_gunship(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (10, 10, 54, 44), (32, 36, 38, 70), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (50, 18), (48, 40), (c, 56), (16, 40), (14, 18)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 12), (46, 20), (44, 36), (c, 50), (20, 36), (18, 20)], fill=STEEL)
    d.rectangle((c - 10, 24, c + 10, 30), fill=OLIVE, outline=BLACK)
    d.rectangle((c - 2, 14, c + 2, 44), fill=SCARLET)
    d.polygon([(12, 24), (8, 32), (12, 36), (18, 28)], fill=OLIVE, outline=BLACK)
    d.polygon([(52, 24), (56, 32), (52, 36), (46, 28)], fill=OLIVE, outline=BLACK)
    d.ellipse((c - 4, 38, c + 4, 46), fill=SCARLET_DARK, outline=BLACK)
    return img

def make_interceptor(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (14, 10, 50, 38), (118, 132, 78, 60), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (48, 18), (42, 30), (c, 50), (22, 30), (16, 18)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 13), (45, 20), (40, 28), (c, 44), (24, 28), (19, 20)], fill=STEEL)
    d.polygon([(c - 3, 10), (c + 3, 10), (c + 7, 17), (c - 7, 17)], fill=SCARLET)
    d.polygon([(16, 20), (8, 24), (12, 28), (20, 24)], fill=OLIVE_LIGHT, outline=BLACK)
    d.polygon([(48, 20), (56, 24), (52, 28), (44, 24)], fill=OLIVE_LIGHT, outline=BLACK)
    d.line((c, 18, c, 40), fill=WHITE, width=2)
    return img

def make_jeep(size=64):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (10, 18, 54, 46), (58, 64, 68, 60), 6))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.rounded_rectangle((14, 20, 50, 42), radius=5, fill=STEEL_DARK, outline=BLACK, width=2)
    d.polygon([(18, 20), (28, 12), (42, 12), (46, 20)], fill=OLIVE, outline=BLACK)
    d.rectangle((22, 23, 42, 32), fill=STEEL)
    d.rectangle((20, 32, 44, 36), fill=STEEL_LIGHT)
    d.rectangle((26, 25, 29, 30), fill=SCARLET)
    d.rectangle((35, 25, 38, 30), fill=SCARLET)
    for x in (16, 48):
        d.ellipse((x - 5, 36, x + 5, 46), fill=BLACK)
        d.ellipse((x - 3, 38, x + 3, 44), fill=STEEL)
    d.rectangle((10, 29, 54, 31), fill=OLIVE_LIGHT)
    d.rectangle((29, 17, 35, 20), fill=SCARLET)
    return img

def make_bus(size=96):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (10, 22, 86, 66), (58, 64, 68, 60), 7))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((12, 22, 84, 62), radius=8, fill=STEEL_DARK, outline=BLACK, width=3)
    d.rectangle((18, 28, 78, 34), fill=OLIVE)
    d.rectangle((18, 36, 78, 52), fill=STEEL)
    for x in range(20, 76, 12):
        d.rectangle((x, 30, x + 6, 46), fill=STEEL_LIGHT)
    d.rectangle((24, 40, 72, 44), fill=SCARLET)
    d.rectangle((15, 24, 81, 27), fill=OLIVE_LIGHT)
    for x in (24, 72):
        d.ellipse((x - 8, 54, x + 8, 70), fill=BLACK)
        d.ellipse((x - 5, 57, x + 5, 67), fill=STEEL)
    d.rectangle((8, 44, 88, 47), fill=BLACK)
    d.rectangle((43, 18, 53, 22), fill=SCARLET)
    return img

def make_factory_base(size, variant='drone'):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    m = 8 if size <= 96 else 10
    d.rounded_rectangle((m, m + 4, size - m, size - m), radius=10, fill=STEEL_DARK, outline=BLACK, width=3)
    d.rectangle((m + 8, m + 12, size - m - 8, size - m - 10), fill=STEEL)
    if variant == 'vehicle':
        d.polygon([(m + 12, size - m - 10), (size // 2, m + 18), (size - m - 12, size - m - 10)], fill=OLIVE, outline=BLACK)
        d.rectangle((m + 14, m + 16, size - m - 14, m + 28), fill=DARK_GREEN)
        d.line((m + 12, size - m - 18, size - m - 12, size - m - 18), fill=SCARLET, width=4)
    else:
        d.polygon([(m + 12, size - m - 10), (size // 2, m + 16), (size - m - 12, size - m - 10)], fill=OLIVE, outline=BLACK)
        d.rectangle((m + 14, m + 16, size - m - 14, m + 28), fill=OLIVE_LIGHT)
        d.line((m + 12, size - m - 18, size - m - 12, size - m - 18), fill=SCARLET, width=3)
    for x in range(m + 12, size - m - 10, 18):
        for y in range(m + 12, size - m - 10, 18):
            d.ellipse((x, y, x + 3, y + 3), fill=BLACK)
    return img

def make_factory_top(size, variant='drone'):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    m = 10
    d.rounded_rectangle((m + 8, m, size - m - 8, size - m - 4), radius=6, fill=STEEL_LIGHT, outline=BLACK, width=2)
    d.polygon([(size // 2, m + 4), (size // 2 + 20, size // 2), (size // 2, size - m - 4), (size // 2 - 20, size // 2)], fill=OLIVE_LIGHT if variant == 'drone' else DARK_GREEN, outline=BLACK)
    d.rectangle((size // 2 - 3, size // 2 - 18, size // 2 + 3, size // 2 + 10), fill=SCARLET)
    d.polygon([(size // 2 - 10, size // 2 + 10), (size // 2 + 10, size // 2 + 10), (size // 2, size // 2 + 24)], fill=SCARLET_DARK)
    if variant == 'vehicle':
        d.rectangle((size // 2 - 24, size // 2 - 6, size // 2 + 24, size // 2 + 2), fill=STEEL_DARK)
        d.polygon([(size // 2 - 18, size // 2 - 20), (size // 2 + 18, size // 2 - 20), (size // 2 + 26, size // 2 - 4), (size // 2 - 26, size // 2 - 4)], fill=OLIVE, outline=BLACK)
        d.rectangle((size // 2 - 6, size // 2 - 16, size // 2 + 6, size // 2 - 4), fill=SCARLET)
    return img

def main():
    save(make_shahed(), 'sprites/units/shahed.png')
    save(cell_drone(64, 12, 9), 'sprites/units/shahed-cell.png')
    save(weapon_icon(24, 'warhead'), 'sprites/units/weapons/wardustry-shahed-warhead.png')
    save(make_factory_base(96, 'drone'), 'sprites/blocks/drone-factory.png')
    save(make_factory_top(96, 'drone'), 'sprites/blocks/drone-factory-top.png')

    save(make_kamikaze_body(64), 'sprites/units/kamikaze-drone.png')
    save(cell_drone(64, 14, 10), 'sprites/units/kamikaze-drone-cell.png')
    save(weapon_icon(24, 'warhead'), 'sprites/units/weapons/wardustry-kamikaze-drone-warhead.png')

    save(make_recon_body(64), 'sprites/units/recon-drone.png')
    save(cell_drone(64, 14, 10), 'sprites/units/recon-drone-cell.png')

    save(make_bomber_body(64), 'sprites/units/bomber-drone.png')
    save(cell_drone(64, 15, 10), 'sprites/units/bomber-drone-cell.png')
    save(weapon_icon(24, 'bomb'), 'sprites/units/weapons/wardustry-bomber-drone-bomb.png')

    save(make_missile_body(64), 'sprites/units/missile-drone.png')
    save(cell_drone(64, 14, 10), 'sprites/units/missile-drone-cell.png')
    save(weapon_icon(24, 'missile'), 'sprites/units/weapons/wardustry-missile-drone-missile.png')

    save(make_gunship_body(64), 'sprites/units/gunship-drone.png')
    save(cell_drone(64, 15, 11), 'sprites/units/gunship-drone-cell.png')
    save(weapon_icon(24, 'autocannon'), 'sprites/units/weapons/wardustry-gunship-drone-autocannon.png')

    save(make_interceptor_body(64), 'sprites/units/interceptor-drone.png')
    save(cell_drone(64, 14, 10), 'sprites/units/interceptor-drone-cell.png')
    save(weapon_icon(24, 'antiair'), 'sprites/units/weapons/wardustry-interceptor-drone-cannon.png')

    save(make_jeep_body(64), 'sprites/units/jeep.png')
    save(cell_drone(64, 15, 10), 'sprites/units/jeep-cell.png')
    save(weapon_icon(24, 'autocannon'), 'sprites/units/weapons/wardustry-jeep-autocannon.png')

    save(make_bus_body(96), 'sprites/units/bus.png')
    save(cell_drone(96, 24, 16), 'sprites/units/bus-cell.png')

    save(make_factory_base(96, 'vehicle'), 'sprites/blocks/vehicle-factory.png')
    save(make_factory_top(96, 'vehicle'), 'sprites/blocks/vehicle-factory-top.png')

if __name__ == '__main__':
    main()
