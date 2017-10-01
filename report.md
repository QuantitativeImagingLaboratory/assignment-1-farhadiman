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
    
