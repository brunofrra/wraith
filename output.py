# output.py

# Show the text and image on two columns
import re

def show (config, info):
    # Probably refactor the whole thing?

    # Padding
    max_size_0 = 0
    max_size_1 = 0
    ansi_escape = re.compile (r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    for i in info:
        if i[0] != '' and i[0][0] == '_':
            # TODO handle this better? what if i[1] is big?
            continue
        if len (i[0]) > max_size_0: max_size_0 = len (i[0])
        clean_i1 = ansi_escape.sub ('', i[1])
        if len (clean_i1) > max_size_1:
            max_size_1 = len (clean_i1)
    for i in info:
        if i[0] == '':
            separator = ' ' * len (config['Output']['Separator'])
        else:
            separator = config['Output']['Separator']
        clean_i1 = ansi_escape.sub ('', i[1])
        if i[0] == '_centered_':
            size = max_size_0 + len (separator) + max_size_1
            pad_size = size - len (clean_i1)
            pad0 = ' ' * int (pad_size / 2)
            pad1 = ' ' * (pad_size - len (pad0))
            print ('x{pad0}{out}{pad1}x'.format 
                (out = i[1],
                pad0 = pad0,
                pad1 = pad1,
                ))
        else:
            pad1 = ' ' * (max_size_1 - len (clean_i1))
            print ('x{pre}{info: >{size0}}{sep}{mid}{out}{pad}{post}x'.format
                (info = i[0],
                mid = '\033[0m', # Remove this, add actual color support
                out = i[1],
                pad = pad1,
                post = '\033[0m', # Remove this, add actual color support
                pre = '\033[0;34m', # Remove this, add actual color support
                sep = separator,
                size0 = max_size_0,
                ))#size = max_info))
