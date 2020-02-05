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

    def __eq__ (self, other):
        return self.__dict__ == other.__dict__


def draw (config):

    ret = ImageOutput ()

    # None
    if config['Image']['Type'] == 'None':
        return ret;

    # Some
    ascii_type = False
    ansi_type = False
    text_type = False
    if config['Image']['Type'].upper() == 'ASCII':
        ascii_type = True
    elif config['Image']['Type'].upper() == 'ANSI':
        ansi_type = True
    elif config['Image']['Type'].upper() == 'TEXT':
        text_type = True
    src = config['Image']['Src']

    # Chose image source
    while len (src) > 0:
        try_src = random.choice (src)
        src.remove (try_src)
        try_src = os.path.expandvars (try_src)
        try:
            if text_type:
                with open (try_src):
                    pass
            else:
                img = Image.open (try_src)
            src = [try_src]
            break
        except Exception as e:
            ret.err.append (('W', "Unable to open file '{}'".format (try_src)))

    if len (src) > 0: # Success!
        src = try_src
    else:
        ret.err.append (('E', 'Could not open any file'))
        return ret

    os.putenv ('WRAITH_IMAGE_SOURCE', src)

    # Text type
    if text_type:
        with open (src) as f:
            txt = f.read ()
        txt = txt.split ('\n')
        ret.width = len (txt[0])
        for line in txt:
            ret.out.append (line)
        return ret

    # Image types
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
        width = img.size[0]
    elif config['Image']['Resize'].lower () == 'stretch':
        height = config['Image']['Lines']
        width = config['Image']['Width']
    else:
        ret.err.append (('W', 'Invalid resize type'))
        height = img.size [1]
        width = img.size [0]
    if ascii_type and not config['Image']['Resize'].lower () == 'stretch':
        # A character is twice as tall
        width = width * 2
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
