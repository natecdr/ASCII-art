from image_blackandwhiter import to_bw
import matplotlib.image as img
import numpy as np
import time
import cv2
import os

""" Draws an image/frame as ASCII art in terminal """
def draw_art(image, chars):
    bw_image, width, height= to_bw(image, 100)

    line = ""
    for i in range(height):
        for j in range(width):
            line += chars[int(np.floor(bw_image[i][j]/26))]
        line += "\n"
    print(line)

""" Webcam video input as ASCII art """
def draw_webcam(chars):
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        rval, frame = vc.read()

    while rval:
        draw_art(frame, chars)
        rval, frame = vc.read()
        key = cv2.waitKey(20)

""" Video file input as ASCII art """
def draw_video(chars):
    vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
    success,image = vidcap.read()
    while success:
        draw_art(image, chars)
        success,image = vidcap.read()

""" Image file input as ASCII art """
def draw_image(chars):
    image= img.imread('portrait.jpeg')
    draw_art(image, chars)


if __name__ == "__main__":
    chars = [' ','.','-',':','=','+','*','#','%','@']
    draw_webcam(chars)
    #draw_video(chars)
    #draw_image(chars)
