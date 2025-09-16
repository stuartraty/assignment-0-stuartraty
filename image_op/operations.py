import math
from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def flip(self, image, direction="horizontal"):
        """
        Perform image flipping along horizontal or vertical direction

        image: the input image to flip
        direction: direction along which to flip

        return: output_image
        """

        rows, cols = shape(image)[:2]
        output_image = zeros(shape(image), uint8)

        if direction == "horizontal":

            for r in range(rows):
                for c in range(cols):
                    output_image[r][c] = image[r][cols - 1 - c]
        elif direction == "vertical":

            for r in range(rows):
                for c in range(cols):
                    output_image[r][c] = image[rows - 1 - r][c]
        else:

            output_image = image

        return output_image
    def chroma_keying(self, foreground, background, target_color, threshold):
        """
        Perform chroma keying to create an image where the targeted green pixels is replaced with
        background

        foreground_img: the input image with green background
        background_img: the input image with normal background
        target_color: the target color to be extracted (green)
        threshold: value to threshold the pixel proximity to the target color

        return: output_image
        """


        height = len(foreground)
        width = len(foreground[0])


        output_image = zeros((height, width, 3), dtype=uint8)


        threshold_sq = threshold * threshold


        target_r, target_g, target_b = target_color

        for y in range(height):
            for x in range(width):

                fg_pixel = foreground[y][x]
                fg_r, fg_g, fg_b = int(fg_pixel[0]), int(fg_pixel[1]), int(fg_pixel[2])


                distance_sq = ((fg_r - target_r) ** 2 +
                               (fg_g - target_g) ** 2 +
                               (fg_b - target_b) ** 2)


                if distance_sq <= threshold_sq:
                    output_image[y][x] = background[y][x]
                else:
                    output_image[y][x] = foreground[y][x]

        return output_image
    # Please do not change the structure
         # Currently the input image is returned, please replace this with the color extracted image

   
