import numpy as np

""" Converts a full scale image to it's representation in gray scale """
def to_bw(image, resolution):
    width = len(image[0])
    height = len(image)

    ratio = width/height

    bw_width = resolution
    bw_height = int(np.floor(bw_width/(ratio*2))) 
    #Need to multiply ratio by 2 because of the 2/1 ratio of text in terminal

    bw_image = np.zeros((bw_height,bw_width))

    x_step = int(np.floor(width/bw_width))
    y_step = int(np.floor(height/bw_height))

    for i in range(bw_height):
        for j in range(bw_width):
            bw_image[i][j] = int(np.sum(image[i*y_step][j*x_step])/3)

    return bw_image, bw_width, bw_height
