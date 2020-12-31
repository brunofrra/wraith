# System overview

**Wraith** is a fetch-like program. It's objective is to show system information
mostly for screenshots.

This is an overview of its internals, for programmers. It has limited usefulness
for end users. The readership is expected to know and understand Python and a
basic of Software Engineering.

## Rationale

After several months without touching this code, I felt a need to document how
it worked so I could better understand it and come back to contributing to it.

This means this document is meant mostly for myself, and as such, there's no
strict adherence to any conventions.

## Top-down view

The code is split in 6 python code files:

* image.py: Handles converting the image to ASCII;

* load_conf.py: Handles the TOML configuration file;

* output.py: Takes the strings returned from the other modules and displays them
    side by side;

* run_commands.py: Runs the external commands and captures their outputs.

* test.py: Tests.

* wraith.py: Main entry point. Mostly glue code for the other modules.

TODO:

* Add a UML diagram.

* Add a brief explanation of the rest of the files.

* Add an in depth explanation of the files.

## Walk-through

TODO

