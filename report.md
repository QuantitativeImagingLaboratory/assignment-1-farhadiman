nearest neighbor interpolation :

Firstly, an image with new dimensions is created as follows:
height, width, channels = image.shape
        mx =int( width * float(fy))
        my = int(height *float (fx))
        size = my,mx, 3
        m = np.zeros(size, dtype=np.uint8)
        
 Afterwards, we ccan find the nearest neighbor in source image using the round image:
 
 m [px,py]=   image [int(round(px/float(fx))),int(round(py/float(fy)))]
        
---------------------------------------------------------------------------------------------------------------
bilinear_interpolation:

Firstly, an image with new dimensions is created as follows:

height, width, channels = image.shape 
        mx =int( width * float(fy))
        my = int(height *float (fx))
        size = my,mx, 3
        
      Afterwards, four different points is calculated based on input scale as follows:
      
       q21x= math.ceil(px / float(fx))
                q21y = math.floor(py / float(fy))

                q22x = math.ceil(px / float(fx))
                q22y = math.ceil(py / float(fy))

                q11x = math.floor(px / float(fx))
                q11y = math.floor(py / float(fy))

                q12x = math.floor(px / float(fx))
                q12y = math.ceil(py / float(fy))
                
                
  Then, we can apply linear interpolation horizontally between two pairs of points as follows:
   ir1 = ((q22x - (px / float(fx))) * image[int(q11x), int(q11y)]) + (((px / float(fx)) - q11x) * image[int(q21x), int(q21y)])
    ir2 = ((q22x - (px / float(fx))) * image[int(q12x), int(q12y)]) + (((px / float(fx)) - q11x) * image[int(q22x), int(q22y)])
    
    Now, everything is ready to calculate second linear interpolation vertically as follows:
    fin = (((q22y - (py / float(fy)))) * ir1) + ((((py / float(fy)) - q11y)) * ir2)
                  m[px, py] = fin
 ---------------------------------------------------------------------------------------------------------------------------------------
                  
    Finding Optimal Threshold
    
    firstly, we initialize the optimal threhold as 127 then instead of using while loop , a for loop along with a condition to break the loop was used as follows:
    
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
    
-----------------------------------------------------------------------------------------------------------------

Binarizing:

using the obtained optimal threshold, binariing the image is done as follows:

        for py in range(0, h[1]):
            for px in range(0, h[0]):
                if (image[px,py]>threshold):
                 bin_img[px, py]=255
                else:
                    bin_img[px, py] = 0
                    
 -------------------------------------------------------------------------------------
Blob Coloring:

Firstly, we create a new 2d array to hold the lable numbers based on input image
h = image.shape
        size = h[0], h[1], 1

        temp = np.zeros(size, dtype=np.uint8)
 then, we complement the input image
 image=255-image
 
 Now, we can detect the lable of each pixel based on its neighborhood as follows:
 
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
-------------------------------------------------------------------------------------------------------------------
compute statistics:

The first step in this section is to calculate how many pixels have been labled by each K.
To do so we use a piece of code similar to calculation of histogram as follows:

hist=[0]*1500

        for px in range(1, h[0]):
            for py in range(1, h[1]):
                g=int(temp[px, py])
                hist[g] = hist[g] + 1
  
  This data collected in hist array would help us to filter the regions based on their area in the next steps.
  the next step, is to find the centroid of each region . To do so we define two array posx and posy to calculate and store the centroid of each region as follows:
  
          for px in range(1, h[0] - 1):
            for py in range(1, h[1] - 1):
                i = temp[px, py]
                posx[int(i)] = posx[int(i)] + px
                posy[int(i)] = posy[int(i)] + py
                cou[int(i)] = cou[int(i)] + 1
    
    Now we can easily print the data of each region at the output console.
  
-----------------------------------------------------------------------------------------------------------------------------

Marking regions:

In this section we try to assign a specific color each region. To do so we use the number of each region and a simple math.
Suppose that all region numbers have been stored in temp array. We can use mod operator to assign a specific color each region as follows.
 if (temp[px,py]%4==0):

                     temp2[px,py]=(255,0,0)

                  elif (temp[px, py] % 6 == 0):
                         temp2[px, py] = (0, 255, 0)
                         .
                         .
                         .
 it means that based on the number of lable and its mode result to specific numbers we can assign a specific color each region. 
 
  Filtering the regions:
  
  Returning the hist array enables us to filter the regions based on the number of pixels as follows:
  
                  if (temp[px][py]!=0) and [hist[int(temp[px,py])]>15]:

                  if (temp[px,py]%4==0):

                     temp2[px,py]=(255,0,0)

                  elif (temp[px, py] % 6 == 0):
                         temp2[px, py] = (0, 255, 0)

                  elif (temp[px, py] % 2 == 0):
                             temp2[px, py] = (0, 0, 255)
                             .
                             .
                             .
 ---------------------------------------------------------------------------------------------------------------------------------
 

