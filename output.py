# output.py

# Show the text and image on two columns

def show (config, img, info):

    # Check who is bigger
    img_size = len (img.out)
    info_size = len (info.out)

    # Pad it
    diff = img_size - info_size
    if diff == 0:       # Same size
        total = img_size
    elif diff > 0:      # Image is bigger
        half = int (diff / 2)
        for i in range (half):
            info.out.insert (0, ('', '', 0))
        for i in range (img_size - half):
            info.out.append (('', '', 0))
        total = img_size
    else:               # Info is bigger
        half = -int (diff / 2)
        for i in range (half):
            img.out.insert (0, ' ' * img.width)
        for i in range (- diff - half):
            img.out.append (' ' * img.width)
        total = info_size
    for i in range (total):
        # Image
        print ('{image_line}{clear}'.format (
                clear = '\033[0m',
                image_line = img.out [i],
                ),
                end = ' ')

        # Info
        if info.out[i][0] == '':
            separator = ' ' * len (config['Output']['Separator'])
        else:
            separator = config['Output']['Separator']
        if info.out[i][0] == '_centered_':
            size = info.max_lhs + len (separator) + info.max_rhs
            pad_size = size - info.out[i][2]
            pad0 = ' '
            pad0 *= info.max_lhs - int ((info.out[i][2] - len (separator)) / 2)
            pad1 = ' '
            pad1 *= (pad_size - len (pad0))
            print ('{pad0}{out}{pad1}'.format 
                (out = info.out[i][1],
                pad0 = pad0,
                pad1 = pad1,
                ))
        else:
            pad1 = ' ' * (info.max_rhs - info.out[i][2])
            print ('{pre}{info: >{size0}}{sep}{mid}{out}{pad}{post}'.format
                (info = info.out[i][0],
                mid = '\033[0m', # Remove this, add actual color support
                out = info.out[i][1],
                pad = pad1,
                post = '\033[0m', # Remove this, add actual color support
                pre = '\033[0;34m', # Remove this, add actual color support
                sep = separator,
                size0 = info.max_lhs,
                ))
