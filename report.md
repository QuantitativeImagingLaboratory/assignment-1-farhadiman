nearest neighbor interpolation :

Firstly, an image with new dimensions is created as follows:
height, width, channels = image.shape
        mx =int( width * float(fy))
        my = int(height *float (fx))
        size = my,mx, 3
        m = np.zeros(size, dtype=np.uint8)
        
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
                
                
  Then we can apply linear interpolation horizontally between two pairs of points as follows:
   ir1 = ((q22x - (px / float(fx))) * image[int(q11x), int(q11y)]) + (((px / float(fx)) - q11x) * image[int(q21x), int(q21y)])
    ir2 = ((q22x - (px / float(fx))) * image[int(q12x), int(q12y)]) + (((px / float(fx)) - q11x) * image[int(q22x), int(q22y)])
    
    Now, everything is ready to calculate second linear interpolation vertically as follows:
    fin = (((q22y - (py / float(fy)))) * ir1) + ((((py / float(fy)) - q11y)) * ir2)
                  m[px, py] = fin
                  
                  
    
