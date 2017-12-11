from webcolors import *
from neopixel import *

gammaTable = [int(pow(float(i) / 255.0, 2.8) * 255.0) for i in range(256)]

def convertColor(color):
    red = color[0]
    green = color[1]
    blue = color[2]
    white = 0
    return (white << 24)| (red << 16)| (green << 8)| blue

def correctColor(color):
    gammaTable = [int(pow(float(i) / 255.0, 2.8) * 255.0) for i in range(256)]

    currentColor = name_to_rgb(color)
    colorR = gammaTable[currentColor[0]]
    colorG = gammaTable[currentColor[1]]
    colorB = gammaTable[currentColor[2]]
   
    correctColor = (colorG, colorR, colorB)
    return convertColor(correctColor)


