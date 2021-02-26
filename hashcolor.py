from PIL import Image, ImageDraw
from enum import Enum
import hashlib
from argparse import ArgumentParser
import os

OutputMode = 'm'
OutputSaveFlag = False
OutputSaveFilename = 'hash.jpg'

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
    WHITE=  (0xFF,0xFF,0xFF) #0
    SILVER= (0xDD,0xDD,0xDD) #1
    GARY=   (0xAA,0xAA,0xAA) #2
    BLACK=  (0x11,0x11,0x11) #3
    RED=    (0xFF,0x41,0x31) #4
    MAROON= (0x85,0x14,0x4B) #5
    YELLOW= (0xFF,0xDC,0x00) #6
    OLIVE=  (0x3D,0x99,0x79) #7
    LIME=   (0x01,0xFF,0x70) #8
    GREEN=  (0x2E,0xCC,0x40) #9
    AQUA=   (0x7F,0xDB,0xFF) #10
    TEAL=   (0x39,0xCC,0xCC) #11
    BLUE=   (0x00,0x74,0xD9) #12
    NAVY=   (0x00,0x1F,0x3F) #13
    FUCHSIA=(0xF0,0x12,0xBE) #14
    PURPLE= (0xB1,0x0D,0xC9) #15



def generator(hexstring):
    width = 640
    height = 640

    im = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    cell_width = 80
    cell_height = 80
    str_index = 0

    colorlist=[]
    if OutputMode == 'm':
        for c in ModernColor:
            colorlist.append(c.value)
    elif OutputMode == 'o':
        for c in OldColor:
            colorlist.append(c.value)
    elif OutputMode == 'g':
        for c in range(0,256,16):
            colorlist.append((c,c,c))
    else:
        for c in ModernColor:
            colorlist.append(c.value)

    for h in range(0, height, cell_height):
        for w in range(0, width, cell_width):
            x = int(hexstring[str_index],16)
            draw.rectangle((w, h, w+cell_width, h+cell_height), fill=colorlist[x])
            str_index+=1

    if OutputSaveFlag:
        im.save(OutputSaveFilename+'.jpg')
    else:
        im.show()


def get_option():
    usage = 'Usage: python {} Text [--file] [--type] [--save]'.format(__file__)
    parser = ArgumentParser(usage=usage)

    parser.add_argument('itext', type=str, help='input string for hash')
    parser.add_argument('-f', '--file', action='store_true', default=False, help='input file for hash')
    parser.add_argument('-t', '--type', nargs='?', type=str, const='m', help='Image type select -> m:ModernColor o:OldColor g:Grayscale. <- Default is Modern')
    parser.add_argument('-s', '--save', nargs='?', type=str, default=False, const='hash.jpg', help='Result picture save. default file name is "hash .jpg"')
    
    return parser.parse_args()


def parser():
    args = get_option() 

    global OutputMode
    global OutputSaveFlag
    global OutputSaveFilename

    OutputMode = args.type

    if args.save:
        OutputSaveFlag = True
        OutputSaveFilename = args.save

    if args.file:
        hashstr =  file_hasher(args.itext)
    elif args.itext:
        hashstr = hashlib.sha256(args.itext.encode()).hexdigest()
    
    
    return hashstr


def file_hasher(path):
    h = hashlib.new('sha256')
    Length = hashlib.new('sha256').block_size * 0x80

    if not os.path.exists(path):
        print("No such file")
        exit(1)
    
    with open(path,'rb') as f:
        BinaryData = f.read(Length)

        while BinaryData:
            h.update(BinaryData)
            BinaryData = f.read(Length)

    return h.hexdigest()


if __name__=='__main__':
    hashstr =  parser()
    print(hashstr) 
    generator(hashstr)

