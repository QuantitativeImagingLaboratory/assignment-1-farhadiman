from __future__ import division
import numpy as np
import cv2

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256


        #hist = cv2.calcHist([image], [0], None, [256], [0, 256])
       # hist, bins = np.histogram(image.ravel(), 256, [0, 256])
        h = image.shape

        for py in range(0, h[1]):
            for px in range(0, h[0]):
                hist[image[px,py]]=hist[image[px,py]]+1
        print hist
        return hist

    def find_optimal_threshold(self, hist,n):

        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""
        p = [0] * 256
        threshold = 0
        for i in range(0, 254):
          p[i] = hist[i] / n

        t = 127
        m1 = 0
        for j in range(0, 100):
            for i in range(0, int (t)):
              m1 = m1 + round(p[i] * i)
            m2 = 0
            for i in range(int (t), 255):
                m2 = m2 + round(p[i] * i)
            t1= (m1 + m2) / 2
            if (t1==t):
                break
            t=t1

        threshold=t









        return threshold

    def binarize(self, image,threshold):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""



        bin_img = image.copy()

        h = image.shape

        for py in range(0, h[1]):
            for px in range(0, h[0]):
                if (image[px,py]>threshold):
                 bin_img[px, py]=255
                else:
                    bin_img[px, py] = 0



        return bin_img
