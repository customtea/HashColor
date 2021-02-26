from PIL import Image, ImageDraw
from enum import Enum
import hashlib


def graydot(hexstring):
    width = 640
    height = 640

    im = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    cell_width = 80
    cell_height = 80
    i = 0

    for h in range(0, height, cell_height):
        for w in range(0, width, cell_width):
            x = int(hexstring[i],16)
            draw.rectangle((w, h, w+cell_width, h+cell_height), fill=(16*x,16*x,16*x))
            i+=1
    im.save('gray'+'.jpg')


if __name__=='__main__':
    dat = "Github"
    hs = hashlib.sha256(dat.encode()).hexdigest()
    print(hs) 
    graydot(hs)