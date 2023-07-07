# encoding: utf-8

import os
from PIL import Image, ImageOps

# Specify the directory path for input images
input_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ResizedImages")

# Specify the output directory path
output_directory = os.path.join(os.path.dirname(__file__), "OutputImages")

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate over all .bmp files in the input directory
for filename in os.listdir(input_directory):
    if filename.lower().endswith(".bmp"):
        input_filepath = os.path.join(input_directory, filename)
        print(f'Input File: {input_filepath}')

        # Read input image
        input_image = Image.open(input_filepath)

        # Get the original image size
        width, height = input_image.size

        # Determine the orientation based on image dimensions
        if width > height:
            print("Image orientation: Landscape")
            # Process for landscape orientation
            target_width, target_height = 800, 480
            display_direction = 'landscape'
        else:
            print("Image orientation: Portrait")
            # Process for portrait orientation
            target_width, target_height = 480, 800
            display_direction = 'portrait'

        # Specify the image conversion mode and dithering algorithm
        display_mode = 'scale'
        display_dither = Image.FLOYDSTEINBERG

        if display_mode == 'scale':
            # Computed scaling
            scale_ratio = max(target_width / width, target_height / height)

            # Calculate the size after scaling
            resized_width = int(width * scale_ratio)
            resized_height = int(height * scale_ratio)

            # Resize image
            output_image = input_image.resize((resized_width, resized_height))

            # Create the target image and center the resized image
            resized_image = Image.new('RGB', (target_width, target_height), (255, 255, 255))
            left = (target_width - resized_width) // 2
            top = (target_height - resized_height) // 2
            resized_image.paste(output_image, (left, top))
        elif display_mode == 'cut':
            # Calculate the fill size to add or the area to crop
            if width / height >= target_width / target_height:
                # The image aspect ratio is larger than the target aspect ratio,
                # padding needs to be added on the left and right
                delta_width = int(height * target_width / target_height - width)
                padding = (delta_width // 2, 0, delta_width - delta_width // 2, 0)
                box = (0, 0, width, height)
            else:
                # The image aspect ratio is smaller than the target aspect ratio and needs to be filled up and down
                delta_height = int(width * target_height / target_width - height)
                padding = (0, delta_height // 2, 0, delta_height - delta_height // 2)
                box = (0, 0, width, height)

            resized_image = ImageOps.pad(input_image.crop(box), size=(target_width, target_height),
                                         color=(255, 255, 255), centering=(0.5, 0.5))
        else:
            # Handle the case when display_mode is neither 'scale' nor 'cut'
            raise ValueError("Invalid display_mode specified.")

        # Create a palette object
        pal_image = Image.new("P", (1, 1))
        pal_image.putpalette(
            (0, 0, 0, 255, 255, 255, 0, 255, 0, 0, 0, 255, 255, 0, 0, 255, 255, 0, 255, 128, 0) +
            (0, 0, 0) * 249)

        # The color quantization and dithering algorithms are performed, and the results are converted to RGB mode
        quantized_image = resized_image.quantize(dither=display_dither, palette=pal_image).convert('RGB')

        # Save output image with modified filename in the output directory
        output_filename = (
            os.path.splitext(filename)[0] + '_' + display_mode + '_' + display_direction + '_output.bmp'
        )
        output_filepath = os.path.join(output_directory, output_filename)
        quantized_image.save(output_filepath)

        print(f'Successfully converted {input_filepath} to {output_filepath}')
