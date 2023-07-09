# Intro

The scripts here were written specifically to size images in to portrait (480x800 px)  
For use with the WaveShare PhotoPainter 7 color e-ink photo frame.

There is only one requirement; the Pillow library:
Example install:  
pip install pillow

# Run Order:
### Pre-image work script

The 'ResizeImageto480800.py' script will iterate through images found in the   
OriginalImages directory. It will scale the image keeping the aspect within 480x800,  
It will then be set to a canvas of 480x800 and saved as a 24bit bmp file of the same name
in the ResizedImages File.

### Convert image work script 
The main.py will do the actual job of converting the bmp image to only 7 colours using the
floyd-steinberg, it iterates through all files found in the ResizedImage directory and
outputs them to the OutputImages Directory.  

reference:  
https://www.waveshare.com/wiki/PhotoPainter  
https://www.waveshare.com/wiki/E-Paper_Floyd-Steinberg
