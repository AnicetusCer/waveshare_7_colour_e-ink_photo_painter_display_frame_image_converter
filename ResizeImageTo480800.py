import os
from PIL import Image

def resize_image(image_path, output_path, target_width, target_height):
    # Open the image
    image = Image.open(image_path)

    # Calculate the aspect ratio of the original image
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height

    # Calculate the new width while maintaining the aspect ratio
    new_width = target_width
    new_height = int(target_width / aspect_ratio)

    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Create a new canvas with the target size
    canvas = Image.new("RGB", (target_width, target_height), (255, 255, 255))

    # Calculate the center position to paste the resized image
    paste_x = 0
    paste_y = (target_height - new_height) // 2

    # Paste the resized image onto the canvas
    canvas.paste(resized_image, (paste_x, paste_y))

    # Update the file extension of the output filename to .bmp
    output_path = os.path.splitext(output_path)[0] + ".bmp"

    # Save the canvas as a 24-bit BMP file
    canvas.save(output_path, "BMP")

# Directory containing the original images
input_directory = "OriginalImages"

# Output directory for the resized images
output_directory = "ResizedImages"

# Target dimensions for resizing
target_width = 480
target_height = 800

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate through all image files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".bmp") or filename.endswith(".webp"):
        # Get the full path of the input image
        input_image = os.path.join(input_directory, filename)

        # Generate the output path for the resized image
        output_image = os.path.join(output_directory, filename)

        # Resize the image and save it
        resize_image(input_image, output_image, target_width, target_height)
