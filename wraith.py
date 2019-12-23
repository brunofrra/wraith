#!/usr/bin/python3
# wraith.py
# TODO: Comment better
import subprocess
import toml

config = toml.load ('config.toml')

print (config)
print ()

info = []
max_info = 0
for i in config['Info']:
    if len (i) > max_info: max_info = len (i)
    if isinstance (config['Info'][i], str):
        use_shell = True
    elif isinstance (config['Info'][i], list):
        use_shell = False
    else:
        # TODO Handle more gracefully
        print ('Error on input {}'.format (i))
        continue
    out = (subprocess.run (config['Info'][i],
            capture_output = True,
            check = True,
            shell = use_shell,
            timeout = config['Command_options']['Timeout'])
            .stdout.decode ('utf-8')[:-1])
    info.append ((i.replace ('_', ' '), out))

for i in info:
   # Get separator from main config
   print ('{info: >{size}}{sep}{out}'.format
            (info = i[0],
            out = i[1],
            sep = config['Output']['Separator'],
            size = max_info))

# TODO: Read TOML configs
#       Define config-file structure
#       Display pixel art image
#       Fetch system info on parallel
#       Display system info
