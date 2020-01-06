# image.py
import os
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

    if config['Image']['Type'] == 'None':
        return ret;
    else:
        if config['Image']['Type'].upper() == 'ASCII':
            ascii_type = True
            ansi_type = False
        elif config['Image']['Type'].upper() == 'ANSI':
            ascii_type = False
            ansi_type = True
        src = config['Image']['Src']
        if isinstance (src, list):
            src = random.choice (src)
        elif not isinstance (src, str):
            ret.err.append ("Invalid image source '{}'".format (src))
            # TODO: try catch return default image

    os.putenv ('WRAITH_IMAGE_SOURCE', src)
    img = Image.open (src)

    # Remove alpha
    if 'A' in img.mode or 'transparency' in img.info:
        alpha = img.convert ('RGBA').split () [-1]
        bg = Image.new ('RGBA', img.size,
                tuple (config['Image']['Background']) + (255,))
        bg.paste (img, mask=alpha)
        img = bg

    # Resize
    if config['Image']['Resize'].lower () == 'none':
        height = img.size[1]
        if ascii_type:
            # A character is twice as tall
            width = img.size[0] * 2
        else:
            width = img.size[0]
    elif config['Image']['Resize'].lower () == 'crop':
        pass
    elif config['Image']['Resize'].lower () == 'contain':
        height = config['Image']['Lines']
        width = int (2 * img.size[0] * height / img.size[1])
    elif config['Image']['Resize'].lower () == 'cover':
        pass
    else:
        ret.err.append ('Invalid resize type')
    img = img.resize ((width, height))
    ret.width = width

    if ascii_type:
        # Set ASCII Palette
        pal = config['Image']['Palette']
        img = img.convert (mode='L')
        img = img.quantize (colors=len (pal), dither = Image.NONE)
    elif ansi_type:
        # TODO: convert to 256 palette
        if config['Image']['Force_Truecolor'] == True:
            os.environ ['COLORTERM'] = 'Forced'
        import truecolor

    # Output
    data = list (img.getdata ())
    for i in range (height):
        if ansi_type and i % 2 != 0:
            # Skip i lines
            continue
        out = ''
        for j in range (width):
            if ascii_type:
                out += pal[ data[i*width + j] ]
            elif ansi_type:
                pos = i*width + j
                color_top = (data[pos][0], data[pos][1], data[pos][2])
                pos += width
                if (pos < len (data)):
                    color_bot = (data[pos][0], data[pos][1], data[pos][2])
                else:
                    color_bot = None
                if color_bot is not None:
                    out += truecolor.color_text ('▀',
                            foreground = color_top,
                            background = color_bot,
                            )
                else:
                    out += truecolor.fore_text ('▀',
                            foreground = color_top,
                            )
        ret.out.append (out)

    return ret
