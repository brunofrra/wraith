#!/usr/bin/python3
# wraith.py

# Entry point
#
# Parses command-line arguments and hooks up the other modules.

import os

import load_conf
import run_commands
import image
import output

os.environ ['WRAITH_PATH'] = os.path.dirname (__file__)

conf_file = os.path.join (os.path.expandvars ('${WRAITH_PATH}'), 'config.toml')
#conf_file = os.path.join (os.path.expandvars ('${WRAITH_PATH}'), 'terroo.toml')

config = load_conf.load (conf_file)

img = image.draw (config)

info = run_commands.run (config)

output.show (config, img, info)

# TODO:
#   Handle errors
