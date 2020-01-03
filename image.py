# image.py
import random
from PIL import Image

class ImageOutput:

    def __init__ (self,
            err = None,
            out = None,
            width = 0,
            ):
        self.err = err or []
        self.out = out or []
        self.width = width

    def __str__ (self):
        return str (self.__dict__)


def draw (config):

    ret = ImageOutput ()

    if config['Image']['Type'] == 'Ascii':
        src = config['Image']['Src']
        if isinstance (src, list):
            src = random.choice (src)
        elif not isinstance (src, str):
            ret.err.append ("Invalid image source '{}'".format (src))
            # TODO: try catch return default image

    img = Image.open (src)

    # Remove alpha
    if 'A' in img.mode or 'transparency' in img.info:
        alpha = img.convert ('RGBA').split () [-1]
        bg = Image.new ('RGBA', img.size,
                tuple (config['Image']['Background']) + (255,))
        bg.paste (img, mask=alpha)
        img = bg

    # Resize
    if config['Image']['Resize'] == 'crop':
        pass
    elif config['Image']['Resize'] == 'contain':
        height = config['Image']['Lines']
        width = int (2 * img.size[0] * height / img.size[1])
    elif config['Image']['Resize'] == 'cover':
        pass
    else:
        ret.err.append ('Invalid resize type')
    img = img.resize ((width, height))
    ret.width = width

    # Set ASCII Palette
    pal = config['Image']['Palette']
    img = img.convert (mode='L')
    img = img.quantize (colors=len (pal), dither = Image.NONE)

    # Output
    data = list (img.getdata ())
    for i in range (height):
        out = ''
        for j in range (width):
            out += pal[ data[i*width + j] ]
        ret.out.append (out)

    return ret
