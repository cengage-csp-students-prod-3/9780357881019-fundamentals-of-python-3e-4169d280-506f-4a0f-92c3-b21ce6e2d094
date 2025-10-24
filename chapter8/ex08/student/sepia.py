from images import Image

def grayscale(image):
    """Converts a color image to grayscale."""
    width = image.getWidth()
    height = image.getHeight()

    for y in range(height):
        for x in range(width):
            (r, g, b) = image.getPixel(x, y)
            # Compute average intensity
            gray = int((r + g + b) / 3)
            image.setPixel(x, y, (gray, gray, gray))

def sepia(image):
    """Converts a color image to sepia tone."""
    # Step 1: Convert to grayscale
    grayscale(image)

    # Step 2: Apply sepia transformation
    width = image.getWidth()
    height = image.getHeight()

    for y in range(height):
        for x in range(width):
            (red, green, blue) = image.getPixel(x, y)

            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)

            image.setPixel(x, y, (red, green, blue))

def main():
    """Tests the sepia filter."""
    filename = input("Enter the image file name: ")
    image = Image(filename)
    print("Displaying original image...")
    image.draw()

    sepia(image)
    print("Displaying sepia-toned image...")
    image.draw()

if __name__ == "__main__":
    main()
