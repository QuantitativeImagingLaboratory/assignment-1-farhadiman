import random
import numpy as np
import cv2
class cell_counting:
    def __init__(self):
        self.info1 = 1
    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""


        h = image.shape
        size = h[0], h[1], 1

        temp = np.zeros(size, dtype=np.uint8)



        image=255-image





        k=1


        b1=h[0]-10
        b2= h[1]-10
        for py in range(1, h[1]-1):
            for px in range(1, h[0]-1):

                if (image[px, py] == 0):
                    continue
                else:

                   if (image[px,py]==255) and (image[px,py-1]==0) and (image[px-1,py]==0):
                     temp[px,py]=k

                     k=k+1
                   if (image[px, py] == 255) and (image[px, py - 1] == 0) and (image[px - 1, py] == 255):
                     temp[px, py]= temp[px-1, py]


                   if (image[px, py] == 255) and (image[px, py - 1] == 255) and (image[px - 1, py] == 0):
                     temp[px, py] = temp[px , py-1]
                   if (image[px, py] == 255) and (image[px, py - 1] == 255) and (image[px - 1, py] == 255):
                     temp[px, py] = temp[px, py-1]
                     temp[px-1 , py]=temp[px , py-1]















        regions = temp

        return regions,k



    def compute_statistics(self, region,k):


        temp=region


        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""


        posx = []
        posy = []
        cou = []
        for px in range(1, 10000):
            posx.append(0)
            posy.append(0)
            cou.append(0)

        h = temp.shape
        hist=[0]*1500

        for px in range(1, h[0]):
            for py in range(1, h[1]):
                g=int(temp[px, py])
                hist[g] = hist[g] + 1

        #hist, bins = np.histogram(temp.ravel(), k, [1, k])

        for px in range(1, h[0] - 1):
            for py in range(1, h[1] - 1):
                i = temp[px, py]
                posx[int(i)] = posx[int(i)] + px
                posy[int(i)] = posy[int(i)] + py
                cou[int(i)] = cou[int(i)] + 1

        for j in range(1, k):
            if (cou[j] != 0) and hist[j]>15:
                #image[posx[j] / cou[j]][posy[j] / cou[j]] = 0
                print "region number :" + str(j)+ " center :(" + str(posx[j] / cou[j]) + "," + str(posy[j] / cou[j]) + ") , area :   " + str(hist[j])


        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)


        return region,hist

    def mark_regions_image(self, image, hist):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""


        temp=image

        h = temp.shape
        size2 = h[0], h[1], 3
        temp2 = np.zeros(size2, dtype=np.uint8)

        for px in range(1, h[0]-10):
            for py in range(1, h[1]-10):

                if (temp[px][py]!=0) and [hist[int(temp[px,py])]>15]:

                  if (temp[px,py]%4==0):

                     temp2[px,py]=(255,0,0)

                  elif (temp[px, py] % 6 == 0):
                         temp2[px, py] = (0, 255, 0)

                  elif (temp[px, py] % 2 == 0):
                             temp2[px, py] = (0, 0, 255)

                  elif (temp[px, py] % 5 == 0):
                         temp2[px, py] = (255, 255, 0)
                  elif (temp[px, py] % 3 == 0):
                         temp2[px, py] = (155, 0, 155)
                  elif (temp[px, py] % 7 == 0):
                         temp2[px, py] = (255, 155, 0)
                  else:
                     temp2[px, py] = (0, 255, 255)

        cv2.imshow('matrix', temp2)
        cv2.waitKey(0)
        return temp2
