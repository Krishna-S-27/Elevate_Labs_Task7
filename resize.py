import os
from PIL import Image

default_size = (800, 600)

use_custom = input("Do you want to set a custom size? (y/n): ").strip().lower()
if use_custom == 'y':
    try:
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        new_size = (width, height)
    except ValueError:
        print("Invalid input. Using default size.")
        new_size = default_size
else:
    new_size = default_size

input_folder = input("Enter the path to the input folder: ").strip()
output_folder = input("Enter the path to save resized images: ").strip()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp' , '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img_resized = img.resize(new_size)
        save_path = os.path.join(output_folder, filename)
        img_resized.save(save_path)

        print(f"Resized and saved: {save_path}")

print("\nAll images have been resized successfully!")
