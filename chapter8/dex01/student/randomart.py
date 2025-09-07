"""
File: randomart.py
Generates and saves images with random colors.
"""

from images import Image
import random

def main():
    """Generates and saves images with random colors.
    Inputs: The image's width, height,
    and output file name."""
    width = int(input("Enter the image's width: "))
    height = int(input("Enter the image's height: "))
    fileName = input("Enter the image's file name: ")
    
    image = Image(width, height)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            image.setPixel(x, y, (r, g, b))

    print("Close the image window to quit. ")
    image.draw()
    image.save(fileName)

if __name__ == "__main__":
    main()