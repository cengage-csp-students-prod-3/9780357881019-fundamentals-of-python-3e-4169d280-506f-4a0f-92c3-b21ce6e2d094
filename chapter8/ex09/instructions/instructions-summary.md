<!-- manual -->

## Instructions

Darkening an image requires adjusting its pixels toward black as a limit, whereas lightening an image requires adjusting them toward white as a limit. Because black is RGB (0, 0, 0) and white is RGB (255, 255, 255), adjusting the three RGB values of each pixel by the same amount in either direction will have the desired effect. Of course, the algorithms must avoid exceeding either limit during the adjustments. (LO: 8.2)

Lightening and darkening are actually special cases of a process known as color filtering. A color filter is any RGB triple applied to an entire image. The filtering algorithm adjusts each pixel by the amounts specified in the triple. For example, you can increase the amount of red in an image by applying a color filter with a positive red value and green and blue values of 0. The filter (20, 0, 0) would make an image’s overall color slightly redder.
Alternatively, you can reduce the amount of red by applying a color filter with a negative red value. Once again, the algorithms must avoid exceeding the limits on the RGB values.

Develop three algorithms for lightening, darkening, and color filtering as three related Python functions, `lighten`, `darken`, and `colorFilter` (in the file **colorfilter.py**). The first two functions should expect an image and a positive integer as arguments. The third function should expect an image and a tuple of integers (the RGB values) as arguments. The following session shows how these functions can be used with the images image1, image2, and image3, which are initially transparent:

```python
>>> image1 = Image(100, 50)
>>> image2 = Image(100, 50)
>>> image3 = Image(100, 50)
>>> darken(image1, 128) # Converts to gray
>>> darken(image2, 64) # Converts to dark gray
>>> colorFilter(image3, (255, 0, 0)) # Converts to red
```

## Your Tasks
