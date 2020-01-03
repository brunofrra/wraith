# output.py

# Show the text and image on two columns

def show (config, info):
    # Probably refactor the whole thing?

    for i in info.out:
        if i[0] == '':
            separator = ' ' * len (config['Output']['Separator'])
        else:
            separator = config['Output']['Separator']
        if i[0] == '_centered_':
            size = info.max_lhs + len (separator) + info.max_rhs
            pad_size = size - i[2]
            pad0 = ' '
            pad0 *= info.max_lhs - int ((i[2] - len (separator) + 1) / 2)
            pad1 = ' '
            pad1 *= (pad_size - len (pad0))
            print ('x{pad0}{out}{pad1}x'.format 
                (out = i[1],
                pad0 = pad0,
                pad1 = pad1,
                ))
        else:
            pad1 = ' ' * (info.max_rhs - i[2])
            print ('x{pre}{info: >{size0}}{sep}{mid}{out}{pad}{post}x'.format
                (info = i[0],
                mid = '\033[0m', # Remove this, add actual color support
                out = i[1],
                pad = pad1,
                post = '\033[0m', # Remove this, add actual color support
                pre = '\033[0;34m', # Remove this, add actual color support
                sep = separator,
                size0 = info.max_lhs,
                ))
