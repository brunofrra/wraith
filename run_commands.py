# run_commands.py

# Runs the commands from and populates the output list
# This could be done in parallel, but is the overhead really worth it?
# TODO: Create a return class, with lots of info
import re
import subprocess

class CommandOutput:
    
    def __init__ (self,
            err = None,
            max_lhs = 0,
            max_rhs = 0,
            out = None,
            ):
        self.err = err or []
        self.max_lhs = max_lhs
        self.max_rhs = max_rhs
        self.out = out or []

    def __eq__ (self, other):
        return self.__dict__ == other.__dict__

    def __str__ (self):
        return str (self.__dict__)

def run (config):
    ret = CommandOutput ()
    ansi_escape = re.compile (r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    for i in config['Info']:
        if isinstance (config['Info'][i], str):
            use_shell = True
        elif isinstance (config['Info'][i], list):
            use_shell = False
        elif isinstance (config['Info'][i], int):
            for j in range (config['Info'][i]):
                ret.out.append (('','', 0))
            continue
        else:
            ret.err.append ("Invalid command '{}'".format (i))
            continue
        # Left hand side
        lhs = i.replace ('_', ' ')
        if len (lhs) > ret.max_lhs: ret.max_lhs = len (lhs)
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
            out = out.split ('\n')
            if out[-1] == '': out = out [:-1] # Remove empty last line
            for o in out:
                size = len (ansi_escape.sub ('', o))
                if size > ret.max_rhs: ret.max_rhs = size
                ret.out.append ((lhs, o, size))
                lhs = ''
        except subprocess.CalledProcessError:
            ret.err.append ("Command '{}' returned a non-success code".format (i))
        except subprocess.TimeoutExpired:
            ret.err.append ("Command '{}' not done after timeout".format (i))
    return ret
