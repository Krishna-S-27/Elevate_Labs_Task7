# Image Resizer Tool

A simple and efficient Python script for batch resizing images using the [Pillow](https://python-pillow.org/) library.

## Overview

This tool allows you to resize all images in a specified folder to a desired size (default or custom) and saves the resized images to an output folder. It supports popular image formats such as PNG, JPG, JPEG, WEBP, BMP, and GIF.

## Features

- **Batch Processing:** Resize multiple images at once.
- **Custom Size Option:** Choose your own width and height, or use the default size (800x600).
- **Format Support:** Works with PNG, JPG, JPEG, WEBP, BMP, and GIF files.
- **Easy to Use:** Simple command-line prompts for input and output folders.

## How It Works

1. **User Input:**  
   - The script prompts you to choose between the default size or a custom size for resizing.
   - You provide the input folder (where your images are) and the output folder (where resized images will be saved).

2. **Image Processing:**  
   - The script iterates through all supported image files in the input folder.
   - For each image, it uses Pillow's `Image.open()` to load the image and `Image.resize()` to resize it to the specified dimensions.
   - The resized image is saved to the output folder with the same filename.

3. **Feedback:**  
   - After each image is processed, the script prints the path of the resized image.
   - Once all images are done, a success message is displayed.

## Code Highlights

- **Pillow Library:**  
  Utilizes `Image.open()` to read images and `Image.resize()` for resizing.
- **File Handling:**  
  Uses Python's `os` module to handle directories and file paths.
- **Robust Input:**  
  Handles invalid size input gracefully by falling back to the default size.

## Usage

1. **Install Pillow:**
    ```
    pip install pillow
    ```

2. **Run the Script:**
    ```
    python resize.py
    ```

3. **Follow Prompts:**
    - Choose custom or default size.
    - Enter the input folder path.
    - Enter the output folder path.

## Example

```
Do you want to set a custom size? (y/n): y
Enter width: 1024
Enter height: 768
Enter the path to the input folder: images/
Enter the path to save resized images: resized/
Resized and saved: resized/photo1.jpg
Resized and saved: resized/photo2.png
...
All images have been resized successfully!
```

## Requirements

- Python 3.x
- Pillow library

---

**Developed by Krishna Shalawadi**
Github: [Krishna-S-27](https://github.com/Krishna-S-27)
