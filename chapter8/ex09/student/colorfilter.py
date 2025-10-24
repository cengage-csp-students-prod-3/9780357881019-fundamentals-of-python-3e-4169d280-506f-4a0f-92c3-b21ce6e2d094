# Write your code here
from images import Image  # Assuming you’re using the Image class from your textbook’s graphics library

def clamp(value):
    """Keep RGB values within the 0–255 range."""
    return max(0, min(255, value))


def colorFilter(image, rgb_values):
    """
    Applies a color filter to the image.
    rgb_values is a tuple (r_change, g_change, b_change)
    that adjusts each pixel by the given amounts.
    """
    width = image.getWidth()
    height = image.getHeight()
    r_change, g_change, b_change = rgb_values

    for y in range(height):
        for x in range(width):
            (r, g, b) = image.getPixel(x, y)
            new_r = clamp(r + r_change)
            new_g = clamp(g + g_change)
            new_b = clamp(b + b_change)
            image.setPixel(x, y, (new_r, new_g, new_b))


def lighten(image, amount):
    """
    Lightens the image by moving each pixel's RGB values
    toward white (255, 255, 255).
    """
    width = image.getWidth()
    height = image.getHeight()

    for y in range(height):
        for x in range(width):
            (r, g, b) = image.getPixel(x, y)
            new_r = clamp(r + amount)
            new_g = clamp(g + amount)
            new_b = clamp(b + amount)
            image.setPixel(x, y, (new_r, new_g, new_b))


def darken(image, amount):
    """
    Darkens the image by moving each pixel's RGB values
    toward black (0, 0, 0).
    """
    width = image.getWidth()
    height = image.getHeight()

    for y in range(height):
        for x in range(width):
            (r, g, b) = image.getPixel(x, y)
            new_r = clamp(r - amount)
            new_g = clamp(g - amount)
            new_b = clamp(b - amount)
            image.setPixel(x, y, (new_r, new_g, new_b))
