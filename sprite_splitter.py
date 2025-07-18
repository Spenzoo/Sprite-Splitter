from PIL import Image
import os
import sys

# -- Check for drag-and-drop input --
if len(sys.argv) < 2:
    input("❌ No image dropped. Drag a PNG file onto this script.\nPress Enter to exit...")
    sys.exit(1)

sprite_path = sys.argv[1]
filename = os.path.splitext(os.path.basename(sprite_path))[0]
output_dir = f"frames_{filename}"

# -- Ask for grid size --
try:
    columns = int(input("Columns (frames across): "))
    rows = int(input("Rows (frames down): "))
except ValueError:
    input("❌ Invalid number. Press Enter to exit...")
    sys.exit(1)

# -- Load image --
try:
    img = Image.open(sprite_path)
except Exception as e:
    input(f"❌ Failed to load image: {e}\nPress Enter to exit...")
    sys.exit(1)

img_w, img_h = img.size

# -- Validate dimensions --
if img_w % columns != 0 or img_h % rows != 0:
    input(f"❌ Image size {img_w}x{img_h} is not divisible by {columns}x{rows}.\nPress Enter to exit...")
    sys.exit(1)

frame_w = img_w // columns
frame_h = img_h // rows

# -- Make output folder --
os.makedirs(output_dir, exist_ok=True)

# -- Slice frames --
frame = 0
for row in range(rows):
    for col in range(columns):
        x0 = col * frame_w
        y0 = row * frame_h
        box = (x0, y0, x0 + frame_w, y0 + frame_h)
        img.crop(box).save(os.path.join(output_dir, f"frame_{frame:03}.png"))
        frame += 1

input(f"✅ {frame} frames saved to '{output_dir}'\nPress Enter to exit...")
