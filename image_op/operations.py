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

        for r in range(rows):
            for c in range(cols):
                if direction == "horizontal":
                    output_image[r][cols == 1 - c] = image [r][c]
                elif direction == "vertical":
                    output_image[rows - 1 - r][c] = image [r][c]
                else:
                    output_image[r][c] = image [r][c]
                    raise Exception("Invalid direction")

        

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

        # add your code here
        rows, cols = shape(foreground)[:2]
        output_image = zeros(shape(foreground), uint8)

        tr, tg, tb = target_color
        for r in range(rows):
            for c in range(cols):
                fr, fg, fb = foreground[r][c]
                distance = math.sqrt((fr - tg) ** 2 + (fb - tb) ** 2)

                if distance < threshold:
                    output_image[r][c] = background[r][c]
                else:
                    output_image[r][c] = foreground[r][c]

        # Please do not change the structure
        return  output_image # Currently the input image is returned, please replace this with the color extracted image

   
