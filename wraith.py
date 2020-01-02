#!/usr/bin/python3
# wraith.py

# Entry point
#
# Parses command-line arguments and hooks up the other modules.

import load_conf
import run_commands
import image
import output

conf_file = 'config.toml'
#conf_file = 'terroo.toml'

config = load_conf.load (conf_file)

info = run_commands.run (config)

output.show (config, info)

# TODO:
#   Handle errors
