# Write your code here
from images import Image

def posterize(image, rgb_tuple):
    """Converts an image to two colors: white and the given RGB color.

    Args:
        image (Image): The image to modify.
        rgb_tuple (tuple): A tuple (r, g, b) for the custom color.
    """
    width = image.getWidth()
    height = image.getHeight()

    for y in range(height):
        for x in range(width):
            (r, g, b) = image.getPixel(x, y)
            brightness = (r + g + b) // 3  # average brightness

            if brightness < 128:
                image.setPixel(x, y, rgb_tuple)  # use custom color
            else:
                image.setPixel(x, y, (255, 255, 255))  # white


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    
    red = int(input("Enter an integer [0..255] for red: "))
    green = int(input("Enter an integer [0..255] for green: "))
    blue = int(input("Enter an integer [0..255] for blue: "))

    color = (red, green, blue)

    posterize(image, color)
    image.draw()


if __name__ == "__main__":
    main()
