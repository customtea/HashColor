from PIL import Image, ImageDraw
from enum import Enum
import hashlib

#RGB
class OldColor(Enum):
    WHITE=  (0xFF,0xFF,0xFF)
    SILVER= (0xC0,0xC0,0xC0)
    GARY=   (0x80,0x80,0x80)
    BLACK=  (0x00,0x00,0x00)
    RED=    (0xFF,0x00,0x00)
    MAROON= (0x80,0x00,0x00)
    YELLOW= (0xFF,0xFF,0x00)
    OLIVE=  (0x80,0x80,0x00)
    LIME=   (0x00,0xFF,0x00)
    GREEN=  (0x00,0x80,0x00)
    AQUA=   (0x00,0xFF,0xFF)
    TEAL=   (0x00,0x80,0x80)
    BLUE=   (0x00,0x00,0xFF)
    NAVY=   (0x00,0x00,0x80)
    FUCHSIA=(0xFF,0x00,0xFF)
    PURPLE= (0x80,0x00,0x80)

class ModernColor(Enum):
    WHITE=  (0xFF,0xFF,0xFF)
    SILVER= (0xDD,0xDD,0xDD)
    GARY=   (0xAA,0xAA,0xAA)
    BLACK=  (0x11,0x11,0x11)
    RED=    (0xFF,0x41,0x31)
    MAROON= (0x85,0x14,0x4B)
    YELLOW= (0xFF,0xDC,0x00)
    OLIVE=  (0x3D,0x99,0x79)
    LIME=   (0x01,0xFF,0x70)
    GREEN=  (0x2E,0xCC,0x40)
    AQUA=   (0x7F,0xDB,0xFF)
    TEAL=   (0x39,0xCC,0xCC)
    BLUE=   (0x00,0x74,0xD9)
    NAVY=   (0x00,0x1F,0x3F)
    FUCHSIA=(0xF0,0x12,0xBE)
    PURPLE= (0xB1,0x0D,0xC9)


colorlist=[]
for c in ModernColor:
    colorlist.append(c.value)



def colordot(hexstring):
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
            #draw.rectangle((w, h, w+cell_width, h+cell_height), fill=colorlist[x], outline=(255, 255, 255))
            draw.rectangle((w, h, w+cell_width, h+cell_height), fill=colorlist[x])
            i+=1
    im.save('square.jpg', quality=95)


if __name__=='__main__':
    dat = "Github"
    hs = hashlib.sha256(dat.encode()).hexdigest()
    print(hs) 
    colordot(hs)