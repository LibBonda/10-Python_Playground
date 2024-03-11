# python code to change terminal color background (need to install sty module and colorama)

import random
from sty import fg

def generateRGB():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red, green, blue
    
red, green, blue = generateRGB()


def generateColor(red, green, blue):
    return fg(red, green, blue)

print(red, green, blue)
    