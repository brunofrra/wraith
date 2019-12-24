# output.py

# Show the text and image on two columns
import re

def show (config, info):
    # Padding
    max_size_0 = 0
    max_size_1 = 0
    for i in info:
        if len (i[0]) > max_size_0: max_size_0 = len (i[0])
        clean_i1 = re.sub ('\\033\\[.*m', '', i[1])
        if len (clean_i1) > max_size_1:
            max_size_1 = len (clean_i1)
    for i in info:
        print ('x{pre}{info: >{size0}}{sep}{mid}{out: <{size1}}{post}x'.format
                (info = i[0],
                mid = '\033[0m', # Remove this, add actual color support
                out = i[1],
                post = '\033[0m', # Remove this, add actual color support
                pre = '\033[0;34m', # Remove this, add actual color support
                sep = config['Output']['Separator'],
                size0 = max_size_0,
                size1 = max_size_1,
                ))#size = max_info))
