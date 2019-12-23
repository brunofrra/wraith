# output.py

# Show the text and image on two columns

def show (config, info):
    for i in info:
        # Get separator from main config
        print ('{pre}{info}{sep}{mid}{out}{post}'.format
                (info = i[0],
                mid = '\033[0m', # Remove this, add actual color support
                out = i[1],
                post = '\033[0m', # Remove this, add actual color support
                pre = '\033[0;34m', # Remove this, add actual color support
                sep = config['Output']['Separator'],
                ))#size = max_info))
