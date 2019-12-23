# run_commands.py

# Runs the commands from and populates the output list
# This could be done in parallel, but is the overhead really worth it?
import subprocess

def run (config):
    ret = []
    for i in config['Info']:
        if isinstance (config['Info'][i], str):
            use_shell = True
        elif isinstance (config['Info'][i], list):
            use_shell = False
        elif isinstance (config['Info'][i], int):
            ret.append (('', '') * config['Info'][i])
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
        ret.append ((i.replace ('_', ' '), out))
    return ret
