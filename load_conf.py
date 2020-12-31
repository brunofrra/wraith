# load_conf.py

import os
import toml

# TODO: Create configuration class
class Config:

    class ImageConfig:

        def load (self,
                Background = None,
                Force_Truecolor = None,
                Height = None,
                Lines = None,
                Palette = None,
                Resize = None,
                Src = None,
                Type = None,
                Width = None,
                ):

            # Background
            if Background is not None:
                if isinstance (Background, list) and len (Background) == 3:
                    self.background = Background
                else:
                    self.err.append (('E', 'Invalid Image.Background: {}'
                            .format (Background)))

            # Force_Truecolor
            if Force_Truecolor is not None:
                if Force_Truecolor == True:
                    self.force_truecolor = True
                else:
                    self.force_truecolor = False

            # Palette
            if Palette is not None:
                if isinstance (Palette, str):
                    self.palette = Palette
                else:
                    self.err.append (('E', 'Invalid format for Image.Palette'))

            # Height/Lines
            if Height is not None or Lines is not None:
                if Height is None: Height = -1
                if Lines is None: Lines = -1
                if (isinstance (Height, int) and
                        isinstance (Lines, int)):
                    self.height = ('L', Lines)
                    if Height >= 0 and Lines >= 0:
                        self.err.append (('W', 'Both Image.Height and '
                                + 'Image.Lines set: Defaulting to using '
                                + 'Image.Lines'))
                    else:
                        self.height = ('H', Height)
                # TODO Err invalid height/lines

            # Resize
            if Resize is not None:
                if isinstance (Resize, str):
                    Resize = Resize.upper ()
                if Resize in ['STRETCH', True]:
                    self.resize = 'STRETCH'
                elif Resize in ['NONE', False]:
                    self.resize = 'NONE'
                else:
                    self.err.append (('E', 'Invalid format for Image.Resize'))

            # Src
            if Src is not None:
                if isinstance (Src, str):
                    self.src = [Src]
                elif isinstance (Src, list):
                    self.src = Src
                else:
                    self.err.append (('E', 'Invalid format for Image.Src'))
                    self.src = [os.path.join (
                            os.path.dirname (__file__),
                            'logo.png',
                            )]

            # Type
            if Type is not None:
                if Type.upper() in ['ASCII', 'ANSI', 'TEXT', 'NONE']:
                    self.type = Type
                else:
                    self.err.append (('E', "Could not understand Image.Type: "
                            + "'{}'".format (Type)))
                    self.type = 'NONE'

            # Width
            if Width is not None:
                if isinstance (Width, int):
                    self.width = Width
                else:
                    self.err.append (('E', 'Invalid format for Image.Width'))
                    self.width = -1
                pass

        def __init__ (self, **kwargs):
            # Set defaults
            self.err = []
            self.background = (0, 0, 0)
            self.force_truecolor = False
            self.height = ('H', -1)
            self.palette = '$8o:. '
            self.resize = False
            self.src = [os.path.join (os.path.dirname (__file__), 'logo.png')]
            self.type = 'None'
            self.width = -1
            # Load non defaults
            self.load (**kwargs)

        def __str__ (self):
            return str (self.__dict__)


    def __init__ (self,
            Info = None,
            **kwargs):
        if isinstance (Info, dict):
            self.info = Info
        else:
            # TODO: Checar se precisa de avisar erro
            self.info = {}
        self.err = []
        self.image = Config.ImageConfig (**kwargs['Image'])

        for i in self.image.err:
            self.err.append (i)
        #for i in self.info.err:
        #    self.err.append (i)
        del self.image.err
        #del self.info.err

    def __str__ (self):
        ret = 'Image: {}'.format (str (self.image))
        return ret

def load (filename):
    file_config = toml.load (filename)
    config = Config (**file_config)
    print (config)
    return file_config
