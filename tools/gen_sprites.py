#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path('/home/ubuntu/wardustry/assets')

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
    if variant == 'boss':
        d.polygon([(m + 10, size - m - 12), (size // 2, m + 14), (size - m - 10, size - m - 12)], fill=OLIVE, outline=BLACK)
        d.rectangle((m + 14, m + 18, size - m - 14, m + 34), fill=DARK_GREEN)
        d.rectangle((m + 18, size // 2 - 10, size - m - 18, size // 2 + 8), fill=STEEL_LIGHT)
        d.line((m + 10, size - m - 22, size - m - 10, size - m - 22), fill=SCARLET, width=5)
        d.line((size // 2, m + 16, size // 2, size - m - 16), fill=SCARLET_DARK, width=4)
    elif variant == 'vehicle':
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
    if variant == 'boss':
        d.rectangle((size // 2 - 28, size // 2 - 8, size // 2 + 28, size // 2 + 4), fill=STEEL_DARK)
        d.polygon([(size // 2 - 22, size // 2 - 24), (size // 2 + 22, size // 2 - 24), (size // 2 + 30, size // 2 - 2), (size // 2 - 30, size // 2 - 2)], fill=OLIVE, outline=BLACK)
        d.rectangle((size // 2 - 8, size // 2 - 18, size // 2 + 8, size // 2 - 4), fill=SCARLET)
        d.ellipse((size // 2 - 14, size // 2 - 14, size // 2 + 14, size // 2 + 14), outline=SCARLET, width=3)
    elif variant == 'vehicle':
        d.rectangle((size // 2 - 24, size // 2 - 6, size // 2 + 24, size // 2 + 2), fill=STEEL_DARK)
        d.polygon([(size // 2 - 18, size // 2 - 20), (size // 2 + 18, size // 2 - 20), (size // 2 + 26, size // 2 - 4), (size // 2 - 26, size // 2 - 4)], fill=OLIVE, outline=BLACK)
        d.rectangle((size // 2 - 6, size // 2 - 16, size // 2 + 6, size // 2 - 4), fill=SCARLET)
    return img

def make_plasma_liquid(size=32):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (5, 5, size - 5, size - 5), (64, 244, 255, 90), 5))
    img = overlay(img, layer_glow(size, (8, 8, size - 8, size - 8), (255, 72, 200, 55), 4))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.ellipse((6, 7, size - 6, size - 7), fill=(23, 120, 148, 230), outline=(7, 20, 24, 255), width=2)
    d.ellipse((10, 10, size - 10, size - 14), fill=(64, 244, 255, 140))
    d.polygon([(c, 4), (size - 8, c), (c, size - 5), (8, c)], fill=(255, 68, 198, 120))
    d.polygon([(c, 8), (size - 12, c), (c, size - 9), (12, c)], fill=(178, 255, 255, 120))
    d.ellipse((c - 3, c - 3, c + 3, c + 3), fill=(255, 255, 255, 220))
    return img

def make_uranium_item(size=32):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (4, 4, size - 4, size - 4), (136, 255, 42, 80), 4))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 3), (size - 7, c), (c, size - 4), (7, c)], fill=(82, 180, 32, 255), outline=BLACK)
    d.polygon([(c, 7), (size - 11, c), (c, size - 8), (11, c)], fill=(170, 255, 74, 255))
    d.regular_polygon((c, c, 4), 6, fill=BLACK)
    d.regular_polygon((c, c, 7), 3, fill=(24, 28, 24, 255))
    d.line((c, 7, c, size - 7), fill=BLACK, width=2)
    d.line((7, c, size - 7, c), fill=BLACK, width=2)
    return img

def make_plasma_reactor_base(size=96):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    m = 10
    d.rounded_rectangle((m, m, size - m, size - m), radius=12, fill=STEEL_DARK, outline=BLACK, width=3)
    d.rectangle((m + 10, m + 12, size - m - 10, size - m - 14), fill=STEEL)
    d.ellipse((size // 2 - 18, size // 2 - 18, size // 2 + 18, size // 2 + 18), fill=(23, 120, 148, 255), outline=BLACK, width=2)
    d.ellipse((size // 2 - 10, size // 2 - 10, size // 2 + 10, size // 2 + 10), fill=(64, 244, 255, 255))
    d.polygon([(size // 2, 18), (size // 2 + 14, size // 2), (size // 2, size - 18), (size // 2 - 14, size // 2)], fill=OLIVE, outline=BLACK)
    for x in range(m + 12, size - m - 12, 16):
        d.rectangle((x, size - m - 12, x + 4, size - m - 8), fill=SCARLET)
    return img

def make_plasma_reactor_top(size=96):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    d.rounded_rectangle((18, 18, size - 18, size - 18), radius=10, outline=(255, 72, 200, 255), width=3)
    d.ellipse((c - 26, c - 26, c + 26, c + 26), outline=(64, 244, 255, 255), width=4)
    d.polygon([(c, 10), (c + 10, c + 20), (c, c + 30), (c - 10, c + 20)], fill=SCARLET)
    d.line((c, 18, c, size - 18), fill=(255, 255, 255, 180), width=2)
    d.line((18, c, size - 18, c), fill=(255, 255, 255, 180), width=2)
    return img

def make_uranium_launcher(size=96):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (10, 14, size - 10, size - 10), (136, 255, 42, 70), 6))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.rounded_rectangle((16, 20, size - 16, size - 14), radius=12, fill=STEEL_DARK, outline=BLACK, width=3)
    d.polygon([(c, 12), (size - 22, 30), (size - 28, 46), (c, 38), (28, 46), (22, 30)], fill=OLIVE, outline=BLACK)
    d.rectangle((c - 6, 18, c + 6, 56), fill=STEEL_LIGHT)
    d.rectangle((c - 3, 10, c + 3, 20), fill=(136, 255, 42, 255))
    d.rectangle((c - 12, 48, c + 12, 58), fill=SCARLET)
    d.ellipse((c - 18, 30, c + 18, 66), outline=(136, 255, 42, 255), width=3)
    return img

def make_drill_base(size, color=OLIVE, powered=False):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (8, 8, size - 8, size - 8), (136, 255, 42, 60) if powered else (118, 132, 78, 55), 6))
    d = ImageDraw.Draw(img)
    m = 6 if size <= 64 else 8
    d.rounded_rectangle((m, m + 3, size - m, size - m), radius=8, fill=STEEL_DARK, outline=BLACK, width=2)
    d.rectangle((m + 7, m + 12, size - m - 7, size - m - 10), fill=STEEL)
    d.polygon([(size // 2, 10), (size - m - 10, size // 2), (size // 2, size - m - 10), (m + 10, size // 2)], fill=color, outline=BLACK)
    d.rectangle((size // 2 - 4, 8, size // 2 + 4, size // 2 + 8), fill=SCARLET)
    if powered:
        d.rectangle((size // 2 - 12, size - m - 18, size // 2 + 12, size - m - 10), fill=(64, 244, 255, 255))
    return img

def make_drill_rotator(size, powered=False):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    d.ellipse((c - 18, c - 18, c + 18, c + 18), outline=(136, 255, 42, 255) if powered else OLIVE_LIGHT, width=4)
    d.line((c, c - 18, c, c + 18), fill=SCARLET, width=3)
    d.line((c - 18, c, c + 18, c), fill=SCARLET, width=3)
    d.polygon([(c, 8), (c + 6, c), (c, c + 6), (c - 6, c)], fill=STEEL_LIGHT)
    return img

def make_drill_top(size, powered=False):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 8), (size - 12, c), (c, size - 8), (12, c)], fill=OLIVE_LIGHT if not powered else (136, 255, 42, 255), outline=BLACK)
    d.rectangle((c - 4, 10, c + 4, size - 10), fill=SCARLET)
    d.line((12, c, size - 12, c), fill=STEEL_LIGHT, width=2)
    return img

def make_tactical_drill(size=64, powered=False):
    return make_drill_base(size, powered=powered)

def make_tactical_riot_drill(size=96):
    return make_drill_base(size, color=OLIVE_LIGHT, powered=True)

def make_jshon_body(size=128):
    img = canvas(size)
    img = overlay(img, layer_glow(size, (16, 16, size - 16, size - 16), (64, 244, 255, 80), 8))
    img = overlay(img, layer_glow(size, (24, 18, size - 24, size - 18), (255, 72, 200, 55), 7))
    d = ImageDraw.Draw(img)
    c = size // 2
    d.polygon([(c, 10), (96, 26), (110, 52), (100, 92), (c, 116), (28, 92), (18, 52), (32, 26)], fill=STEEL_DARK, outline=BLACK)
    d.polygon([(c, 20), (86, 32), (96, 54), (88, 84), (c, 102), (40, 84), (32, 54), (42, 32)], fill=STEEL)
    d.polygon([(c, 12), (c + 12, 24), (c - 12, 24)], fill=(136, 255, 42, 255))
    d.rectangle((c - 10, 88, c + 10, 112), fill=SCARLET_DARK)
    d.rectangle((c - 32, 58, c + 32, 70), fill=OLIVE)
    d.rectangle((c - 18, 48, c + 18, 58), fill=STEEL_LIGHT)
    d.polygon([(24, 60), (14, 68), (18, 76), (30, 68)], fill=OLIVE, outline=BLACK)
    d.polygon([(104, 60), (114, 68), (110, 76), (98, 68)], fill=OLIVE, outline=BLACK)
    d.rectangle((54, 34, 74, 42), fill=(255, 72, 200, 255))
    d.rectangle((58, 42, 70, 52), fill=(64, 244, 255, 255))
    return img

def make_jshon_cell(size=128):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    d.rounded_rectangle((c - 24, c - 20, c + 24, c + 20), radius=8, fill=WHITE, outline=(220, 198, 198, 255), width=3)
    d.rounded_rectangle((c - 14, c - 12, c + 14, c + 12), radius=5, fill=(220, 198, 198, 255))
    d.rectangle((c - 8, c - 30, c + 8, c - 20), fill=WHITE)
    return img

def make_jshon_weapon(size=32, kind='cannon'):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    if kind == 'cannon':
        d.rounded_rectangle((5, 12, size - 5, 20), radius=3, fill=STEEL_DARK, outline=BLACK)
        d.rectangle((size - 10, 14, size - 3, 18), fill=SCARLET)
        d.polygon([(8, 12), (16, 4), (24, 4), (28, 12)], fill=OLIVE, outline=BLACK)
    elif kind == 'close':
        d.ellipse((5, 5, size - 5, size - 5), fill=STEEL_DARK, outline=BLACK)
        d.ellipse((10, 10, size - 10, size - 10), fill=SCARLET)
    elif kind == 'wide':
        d.rounded_rectangle((4, 10, size - 4, 22), radius=4, fill=STEEL_DARK, outline=BLACK)
        d.rectangle((size - 7, 11, size - 3, 21), fill=SCARLET)
        d.rectangle((7, 13, 12, 19), fill=(64, 244, 255, 255))
    return img

def make_ore_variant(index):
    size = 32
    img = canvas(size)
    img = overlay(img, layer_glow(size, (2, 2, size - 2, size - 2), (136, 255, 42, 35), 3))
    d = ImageDraw.Draw(img)
    c = size // 2
    wobble = index * 2
    d.polygon([(c, 2 + index), (size - 6 - wobble, c - 1), (c + 1, size - 3), (6 + wobble, c + 1)], fill=(72, 160, 28, 255), outline=BLACK)
    d.polygon([(c, 6 + index), (size - 10 - wobble, c), (c + 1, size - 7), (10 + wobble, c)], fill=(170, 255, 74, 255))
    d.rectangle((c - 2, 6, c + 2, 26), fill=BLACK)
    d.rectangle((6, c - 2, 26, c + 2), fill=BLACK)
    d.ellipse((12 - index, 12 - index, 20 + index, 20 + index), fill=(40, 66, 20, 255))
    return img

def make_armored_conveyor_frame(blend, frame):
    size = 32
    img = canvas(size)
    d = ImageDraw.Draw(img)
    # steel shell
    d.rounded_rectangle((3, 4, 29, 28), radius=5, fill=STEEL_DARK, outline=BLACK, width=2)
    # reinforce depending on blend bit
    if blend & 1:
        d.rectangle((4, 5, 8, 27), fill=OLIVE)
    if blend & 2:
        d.rectangle((24, 5, 28, 27), fill=OLIVE)
    if blend & 4:
        d.rectangle((5, 4, 27, 8), fill=OLIVE_LIGHT)
    # central belt and motion
    for x in range(10, 23, 5):
        d.rectangle((x, 12, x + 3, 20), fill=STEEL_LIGHT)
    shift = frame % 4
    d.rectangle((8 + shift, 14, 24 + shift, 18), fill=SCARLET)
    d.line((7, 16, 25, 16), fill=BLACK, width=1)
    d.rectangle((6, 9, 26, 11), fill=STEEL_LIGHT)
    d.rectangle((6, 21, 26, 23), fill=STEEL_LIGHT)
    d.ellipse((12, 8, 20, 24), outline=(64, 244, 255, 120), width=1)
    return img

def main():
    save(make_plasma_liquid(), 'sprites/liquids/plasma-energy.png')
    save(make_uranium_item(), 'sprites/items/uranium.png')
    save(make_ore_variant(0), 'sprites/blocks/ore-uranium1.png')
    save(make_ore_variant(1), 'sprites/blocks/ore-uranium2.png')
    save(make_ore_variant(2), 'sprites/blocks/ore-uranium3.png')

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

    save(make_plasma_reactor_base(96), 'sprites/blocks/plasma-reactor.png')
    save(make_plasma_reactor_top(96), 'sprites/blocks/plasma-reactor-top.png')
    save(make_uranium_launcher(96), 'sprites/blocks/uranium-launcher.png')

    save(make_drill_base(64), 'sprites/blocks/tactical-drill.png')
    save(make_drill_rotator(64), 'sprites/blocks/tactical-drill-rotator.png')
    save(make_drill_top(64), 'sprites/blocks/tactical-drill-top.png')

    save(make_drill_base(96, powered=True), 'sprites/blocks/tactical-bore.png')
    save(make_drill_rotator(96, powered=True), 'sprites/blocks/tactical-bore-rotator.png')
    save(make_drill_top(96, powered=True), 'sprites/blocks/tactical-bore-top.png')

    save(make_factory_base(128, 'boss'), 'sprites/blocks/jshon-ban-factory.png')
    save(make_factory_top(128, 'boss'), 'sprites/blocks/jshon-ban-factory-top.png')
    save(make_jshon_body(128), 'sprites/units/jshon-ban.png')
    save(make_jshon_cell(128), 'sprites/units/jshon-ban-cell.png')
    save(make_jshon_weapon(32, 'cannon'), 'sprites/units/weapons/wardustry-jshon-ban-cannon.png')
    save(make_jshon_weapon(32, 'close'), 'sprites/units/weapons/wardustry-jshon-ban-close-blast.png')
    save(make_jshon_weapon(32, 'wide'), 'sprites/units/weapons/wardustry-jshon-ban-wide-blast.png')

    for blend in range(7):
        for frame in range(4):
            save(make_armored_conveyor_frame(blend, frame), f'sprites/blocks/armored-conveyor-{blend}-{frame}.png')

if __name__ == '__main__':
    main()
