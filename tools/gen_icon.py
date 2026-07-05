#!/usr/bin/env python3
"""Generate the WarDustry mod icon (icon.png). Military-tech themed, 256x256 RGBA.
The mod name 'WarDustry' is rendered prominently on the icon."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SIZE = 256
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

STEEL_DARK = (34, 38, 40, 255)
STEEL = (58, 64, 66, 255)
OLIVE = (74, 82, 45, 255)
OLIVE_LIGHT = (110, 122, 66, 255)
SCARLET = (214, 48, 40, 255)
WHITE = (238, 240, 236, 255)
HAZARD = (232, 190, 40, 255)
BLACK = (18, 20, 21, 255)


def font(sz):
    return ImageFont.truetype(FONT, sz)


def text_size(draw, txt, fnt):
    b = draw.textbbox((0, 0), txt, font=fnt)
    return b[2] - b[0], b[3] - b[1], b[0], b[1]


img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# rounded steel plate background
r = 28
d.rounded_rectangle([4, 4, SIZE - 5, SIZE - 5], radius=r, fill=STEEL_DARK)
# top olive band
d.rounded_rectangle([4, 4, SIZE - 5, 96], radius=r, fill=OLIVE)
d.rectangle([4, 60, SIZE - 5, 96], fill=OLIVE)
# vertical steel gradient sheen
sheen = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
sd = ImageDraw.Draw(sheen)
for y in range(96, SIZE - 5):
    t = (y - 96) / (SIZE - 101)
    c = int(58 + 18 * (1 - t))
    sd.line([(6, y), (SIZE - 7, y)], fill=(c, c + 6, c + 8, 255))
mask = Image.new("L", (SIZE, SIZE), 0)
ImageDraw.Draw(mask).rounded_rectangle([4, 4, SIZE - 5, SIZE - 5], radius=r, fill=255)
img.paste(sheen, (0, 0), Image.composite(sheen.split()[3], Image.new("L", (SIZE, SIZE), 0), mask if False else mask).point(lambda p: p))
d = ImageDraw.Draw(img)

# hazard stripes along the bottom edge
stripe_top = SIZE - 40
for x in range(-40, SIZE + 40, 32):
    d.polygon([(x, SIZE - 6), (x + 16, SIZE - 6), (x + 16 + 20, stripe_top),
               (x + 20, stripe_top)], fill=HAZARD)
    d.polygon([(x + 16, SIZE - 6), (x + 32, SIZE - 6), (x + 32 + 20, stripe_top),
               (x + 16 + 20, stripe_top)], fill=BLACK)
# reclip bottom stripes to rounded rect
clip = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
clip.paste(img, (0, 0), mask)
img = clip
d = ImageDraw.Draw(img)

# central emblem: a star (military insignia) behind the text on the olive band
cx, cy = SIZE // 2, 50
import math
pts = []
for i in range(10):
    ang = -math.pi / 2 + i * math.pi / 5
    rad = 34 if i % 2 == 0 else 15
    pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
d.polygon(pts, fill=HAZARD, outline=BLACK)

# main title: War (scarlet) + Dustry (white), auto-fit width
def draw_title(dr, y):
    for sz in range(58, 20, -2):
        f = font(sz)
        w1, h1, ox1, oy1 = text_size(dr, "War", f)
        w2, h2, ox2, oy2 = text_size(dr, "Dustry", f)
        total = w1 + w2
        if total <= SIZE - 40:
            h = max(h1, h2)
            start = (SIZE - total) // 2
            # shadow
            dr.text((start - ox1 + 2, y + 2), "War", font=f, fill=(0, 0, 0, 170))
            dr.text((start + w1 - ox2 + 2, y + 2), "Dustry", font=f, fill=(0, 0, 0, 170))
            dr.text((start - ox1, y - oy1), "War", font=f, fill=SCARLET)
            dr.text((start + w1 - ox2, y - oy2), "Dustry", font=f, fill=WHITE)
            return y + h
    return y

end_y = draw_title(d, 120)

# subtitle
sf = font(20)
sub = "MILITARY TECH"
ws, hs, oxs, oys = text_size(d, sub, sf)
d.text(((SIZE - ws) // 2 - oxs, 190 - oys), sub, font=sf, fill=(200, 205, 198, 255))

# outer border
d.rounded_rectangle([4, 4, SIZE - 5, SIZE - 5], radius=r, outline=BLACK, width=4)

img.save("/home/ubuntu/wardustry/icon.png")
print("wrote icon.png", img.size, img.mode)
