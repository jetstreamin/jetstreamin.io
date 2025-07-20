from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Mesh ID and target directory
mesh_id = "MEDIA-70689b0357ef69bf"
out_dir = Path.home() / "jetstreamin.io" / mesh_id
out_dir.mkdir(parents=True, exist_ok=True)

# Image settings
size = (512, 512)
bg_color = (173, 216, 230)  # Light blue
fg_color = (0, 0, 0)        # Black
font_size = 160

# Load font or fallback
try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)
except:
    font = ImageFont.load_default()

# Generate images 1–4
for i in range(1, 5):
    img = Image.new("RGB", size, bg_color)
    draw = ImageDraw.Draw(img)
    text = str(i)
    bbox = draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pos = ((size[0] - w) // 2, (size[1] - h) // 2)
    draw.text(pos, text, fill=fg_color, font=font)
    img.save(out_dir / f"{mesh_id}_img{i}.png")
