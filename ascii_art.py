from turtle import resetscreen
import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt

""" Draws an image/frame as ASCII art in terminal """
def draw_art(image, width, height):
    chars =  ".:-=+*#%@"
    bw_image = preprocess(image, width, height, chars)
    
    line = ""
    for i in range(height):
        for j in range(width):
            line += chars[bw_image[i][j]]
        line += "\n"
    print(line)

""" Webcam video input as ASCII art """
def convert_webcam(width, height):
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        rval, frame = vc.read()

    while rval:
        draw_art(frame, width, height)
        rval, frame = vc.read()
        key = cv2.waitKey(20)

""" Video file input as ASCII art """
def convert_video(file, width, height):
    vidcap = cv2.VideoCapture(file, 0)

    if vidcap.isOpened():
        success,image = vidcap.read()

    while success:
        draw_art(image, width, height)
        success,image = vidcap.read()
        key = cv2.waitKey(20)

""" Image file input as ASCII art """
def convert_image(file, width, height):
    image = cv2.imread(file, 0)
    draw_art(image, width, height)

"""Image preprocessing"""
def preprocess(image, width, height, chars):
    res = cv2.resize(image, (width, height))
    if len(res.shape) > 2:
        res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    res = res/256 * len(chars)
    return res.astype(int)


def init_parser():
    parser = argparse.ArgumentParser(description="Image to ASCII Art converter")
    parser.add_argument("type", metavar="{img, video}", type=str, help = "Type of input")
    parser.add_argument("source", metavar = "src", type=str, help = "Source image or video, 'cam' to have your webcam as the source")
    parser.add_argument("width", metavar = "width", type=int, help = "Width of output ASCII image")
    parser.add_argument("height", metavar = "height", type=int, help = "Height of output ASCII image")
    return parser


if __name__ == "__main__":
    parser = init_parser()
    args = parser.parse_args()
    width = args.width
    height = int(args.height / 2) #Text output is of height 2 and width 1

    if args.type == "img":
        try: 
            source_file = args.source
            convert_image(source_file, width, height)
        except Exception as e:
            print(str(e))
            print("There was an error, check that the file exists.")
            
    elif args.type == "video":
        try:
            if args.source == "cam":
                convert_webcam(width, height)
            else:
                source_file = args.source
                convert_video(source_file, width, height)
        except Exception as e:
            print(str(e))
            print("There was an error, check that the file exists or if your webcam works properly.")
        
    else:
        print("Invalid argument for type")
