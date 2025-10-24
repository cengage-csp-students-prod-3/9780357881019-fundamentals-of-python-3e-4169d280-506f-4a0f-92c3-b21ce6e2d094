from images import Image  # assumes the 'images' module from your textbook

def sharpen(image, degree, threshold):
    """Sharpen the given image by darkening edge pixels.
    
    Args:
        image (Image): The image to sharpen.
        degree (int): The amount to darken edge pixels (higher = sharper).
        threshold (int): The difference in brightness needed to count as an edge.
    """
    width = image.getWidth()
    height = image.getHeight()
    
    # Create a new image to avoid overwriting original pixels during processing
    new_image = Image(width, height)
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            (r, g, b) = image.getPixel(x, y)
            (r_right, g_right, b_right) = image.getPixel(x + 1, y)
            (r_down, g_down, b_down) = image.getPixel(x, y + 1)
            
            # Compute brightness as average of RGB
            brightness = (r + g + b) // 3
            brightness_right = (r_right + g_right + b_right) // 3
            brightness_down = (r_down + g_down + b_down) // 3
            
            # If difference exceeds threshold, darken pixel (sharpen edge)
            if abs(brightness - brightness_right) > threshold or abs(brightness - brightness_down) > threshold:
                new_r = max(0, r - degree)
                new_g = max(0, g - degree)
                new_b = max(0, b - degree)
            else:
                new_r, new_g, new_b = r, g, b
            
            new_image.setPixel(x, y, (new_r, new_g, new_b))
    
    return new_image
