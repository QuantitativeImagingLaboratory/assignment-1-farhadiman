import numpy as np
import math
import cv2
class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here

        # iterate over the entire image.



        height, width, channels = image.shape
        mx =int( width * float(fy))
        my = int(height *float (fx))
        size = my,mx, 3
        m = np.zeros(size, dtype=np.uint8)
        for py in range(0, mx):
            for px in range(0, my):
                 m [px,py]=   image [int(round(px/float(fx))),int(round(py/float(fy)))]






        cv2.imshow('matrix', m)
        cv2.waitKey(0)

        return image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here

        height, width, channels = image.shape


        mx = int((width-3) * float(fx))
        my = int((height-3) * float(fy))

        size = mx, my, 3
        m = np.zeros(size, dtype=np.uint8)




        for py in range(0, my):
            for px in range(0, mx):

                q21x= math.ceil(px / float(fx))
                q21y = math.floor(py / float(fy))

                q22x = math.ceil(px / float(fx))
                q22y = math.ceil(py / float(fy))

                q11x = math.floor(px / float(fx))
                q11y = math.floor(py / float(fy))

                q12x = math.floor(px / float(fx))
                q12y = math.ceil(py / float(fy))

                if (q22x - q11x != 0) and (q22y - q11y != 0):
                  ir1 = ((q22x - (px / float(fx))) * image[int(q11x), int(q11y)]) + (((px / float(fx)) - q11x) * image[int(q21x), int(q21y)])
                  ir2 = ((q22x - (px / float(fx))) * image[int(q12x), int(q12y)]) + (((px / float(fx)) - q11x) * image[int(q22x), int(q22y)])
                  fin = (((q22y - (py / float(fy)))) * ir1) + ((((py / float(fy)) - q11y)) * ir2)
                  m[px, py] = fin

                if (q22x - q11x == 0) and (q22y - q11y != 0):
                  ir1 = ((q22y - (py / float(fy))) * image[int(q11x), int(q11y)]) + (((py / float(fy)) - q11y) * image[int(q21x), int(q21y)])
                  m[px, py] = ir1

                if (q22x - q11x != 0) and (q22y - q11y == 0):
                  ir1 = ((q22x - (px / float(fx))) * image[int(q11x), int(q11y)]) + (((px / float(fx)) - q11x) * image[int(q21x), int(q21y)])
                  m[px, py] = ir1

                if (q22x - q11x == 0) and (q22y - q11y == 0):
                  m[px, py] = image[int(q11x), int(q11y)]

        cv2.imshow('matrix', m)
        cv2.waitKey(0)

        return image
