# Write your code here
from images import Image

def grayscale(image):
    """Convert image to grayscale by averaging RGB values."""
    width = image.getWidth()
    height = image.getHeight()

    for y in range(height):
        for x in range(width):
            (r, g, b) = image.getPixel(x, y)
            # Simple average method
            avg = (r + g + b) // 3
            image.setPixel(x, y, (avg, avg, avg))
    return image

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    grayscale(image)
    image.draw()

if __name__ == "__main__":
    main()
