# run_commands.py

# Runs the commands from and populates the output list
# This could be done in parallel, but is the overhead really worth it?
import subprocess

def run (config):
    ret = []
    err = []
    for i in config['Info']:
        if isinstance (config['Info'][i], str):
            use_shell = True
        elif isinstance (config['Info'][i], list):
            use_shell = False
        elif isinstance (config['Info'][i], int):
            for j in range (config['Info'][i]):
                ret.append (('', ''))
            continue
        else:
            err.append ("Invalid command '{}'".format (i))
            continue
        # Left hand side
        lhs = i.replace ('_', ' ')
        if lhs[0] == ' ':
            if lhs[-1] == ' ': lhs = '_centered_'
            else: lhs = ''
        # Right hand side
        try:
            out = (subprocess.run (config['Info'][i],
                    capture_output = True,
                    check = True,
                    shell = use_shell,
                    timeout = config['Command_options']['Timeout'])
                    .stdout.decode ('utf-8')[:-1])
            ret.append ((lhs, out))
        except subprocess.CalledProcessError:
            err.append ("Command '{}' returned a non-success code".format (i))
        except subprocess.TimeoutExpired:
            err.append ("Command '{}' not done after timeout".format (i))
    return ret, err
