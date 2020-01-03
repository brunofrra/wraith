# image.py
import re
import subprocess

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
    ansi_escape = re.compile (r'\x1B\[[^m]*m')#(r'\x1B[@-_][0-?]*[ -/]*[@-~]')

    if config['Image']['Type'] == 'Command':
        src = config['Image']['Src']
        if isinstance (src, str):
            use_shell = True
        elif isinstance (src, list):
            use_shell = False
        else:
            ret.err.append ("Invalid image source '{}'".format (src))
            # TODO: try catch return default image

        try:
            out = (subprocess.run (src,
                    capture_output = True,
                    check = True,
                    shell = use_shell,
                    timeout = config['Command_options']['Timeout'])
                    .stdout.decode ('utf-8'))
            out = out.split ('\n')
            if ansi_escape.sub ('', out[-1]) == '':
                out = out [:-1] # Remove empty last line
            for o in out:
                width = len (ansi_escape.sub ('', o).rstrip ())
                if width > ret.width: ret.width = width
                ret.out.append ((o, width))
                #ret.out.append ((ansi_escape.sub ('', o).rstrip (), width))
                lhs = ''

        except subprocess.CalledProcessError:
            ret.err.append ("Command '{}' returned a non-success code".format
                    (i))
        except subprocess.TimeoutExpired:
            ret.err.append ("Command '{}' not done after timeout".format (i))

    return ret
