# Write your code here
from images import Image

def invert(image):
    """Invert the colors in the given image."""
    width = image.getWidth()
    height = image.getHeight()

    for y in range(height):
        for x in range(width):
            (r, g, b) = image.getPixel(x, y)
            # Invert each color component
            newR = 255 - r
            newG = 255 - g
            newB = 255 - b
            image.setPixel(x, y, (newR, newG, newB))
    return image

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    invert(image)
    image.draw()

if __name__ == "__main__":
    main()
