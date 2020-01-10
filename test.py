#!/usr/bin/python3
import image
import run_commands
import unittest

class TestImage (unittest.TestCase):

    def testAnsi (self):
        config = {'Image': {
                'Background': [0, 0, 0],
                'Force_Truecolor': True,
                'Resize': 'none',
                'Src': ['logo-mini.png'],
                'Type': 'ansi',
                }}
        returned = image.draw (config)
        expected = image.ImageOutput (**{'out':
            ['\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;170;170;170m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;170;170m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;170;170;170m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02',
             '\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;170;170m\x02\x01\x1b[48;2;85;85;85m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;170;170m\x02\x01\x1b[48;2;170;170;170m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02',
             '\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;170;170m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;170;170;170m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;85;85;85m\x02\x01\x1b[48;2;170;170;170m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;170;170m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;170;170m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02',
             '\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;85;85;85m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;170;170m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;170;170m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02\x01\x1b[38;2;0;0;0m\x02\x01\x1b[48;2;0;0;0m\x02▀'
            +'\x01\x1b[0m\x02'
             ], 'width': 8})
        self.assertEqual (returned, expected)

    def testAscii (self):
        config = {'Image': {
                'Background': [0, 0, 0],
                'Palette': '$8o:. ',
                'Resize': 'none',
                'Src': ['logo-mini.png'],
                'Type': 'ascii',
                }}
        returned = image.draw (config)
        expected = image.ImageOutput (**{ 'out': [
                '                ',
                '     :8$8o..88: ',
                ' .oo.    .oo.   ',
                ' .::.    :88:   ',
                '   .o8$$o: .oo. ',
                '       :8$8o.   ',
                '     .:oo88o.   ',
                '                ',
                ], 'width': 16})
        self.assertEqual (returned, expected)

    def testBackground (self):
        config = {'Image': {
                'Background': [255, 255, 255],
                'Palette': '$8o:. ',
                'Resize': 'none',
                'Src': ['logo-mini.png'],
                'Type': 'ascii',
                }}
        returned = image.draw (config)
        expected = image.ImageOutput (**{ 'out': [
                '$$$$$8.      .8$',
                '$8.  .ooo: .oo. ',
                ' .::.    .::.   ',
                ' .::.    .oo.   ',
                '$8. :ooo:. .::. ',
                '$$$8.  .ooo: .8$',
                '$$$8. .::oo: .8$',
                '$$$$$8.    .8$$$'
                ], 'width': 16})
        self.assertEqual (returned, expected)

    def testFileError (self):
        config = {'Image': {
                'Src': ['/dev/null/fail'],
                'Type': 'ASCII',
                }}
        returned = image.draw (config)
        expected = image.ImageOutput (**{'err': [
                ('W', "Unable to open file '/dev/null/fail'"),
                ('E', 'Could not open any file'),
                ]})
        self.assertEqual (returned, expected)

    def testText (self):
        config = {'Image': {'Type': 'text', 'Src': ['img.txt']}}
        returned = image.draw (config)
        expected = image.ImageOutput (**{'out': ['    ',
            '\x1b[1;30;40m▄\x1b[1;31;41m▄\x1b[1;32;42m▄\x1b[1;34;44m▄\x1b[0m',
            '\x1b[1;37;47m▄\x1b[1;33;43m▀\x1b[1;36;46m▀\x1b[1;35;45m▀\x1b[0m',
            '    ', ''], 'width': 4})
        self.assertEqual (returned, expected)


class TestRunCommands (unittest.TestCase):

    def testCenteredOutput (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'_centered_output_': ['echo', 'rhs']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out':
                [('_centered_', 'rhs', 3)],
                'max_rhs': 3})
        self.assertEqual (returned, expected)

    def testCommandFail (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['false']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'err': [('E',
                "Command 'lhs' returned a non-success code")]})
        self.assertEqual (returned, expected)

    def testCommandTimeout (self):
        config = {'Command_options': {'Timeout': 0.1},
                'Info': {'lhs': ['sleep', '2']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'err': [('E',
                "Command 'lhs' not done after timeout")]})
        self.assertEqual (returned, expected)

    def testIntCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': 2}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out':
                [('', '', 0), ('', '', 0)]})
        self.assertEqual (returned, expected)

    def testListCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['echo', 'rhs']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out': [('lhs', 'rhs', 3)],
                'max_lhs': 3, 'max_rhs': 3})
        self.assertEqual (returned, expected)

    def testMultiLineCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['printf', 'foo\nbar']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out':
                [('lhs', 'foo', 3), ('', 'bar', 3)],
                'max_lhs': 3, 'max_rhs': 3})
        self.assertEqual (returned, expected)

    def testNoLhs (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'_no_lhs': ['echo', 'rhs']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out': [('', 'rhs', 3)],
                'max_lhs': 0, 'max_rhs': 3})
        self.assertEqual (returned, expected)
    
    def testStringCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': 'echo rhs'}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out': [('lhs', 'rhs', 3)],
                'max_lhs': 3, 'max_rhs': 3})
        self.assertEqual (returned, expected)

    def testTwoCommands (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'zFirst': 'echo rhs1', 'aLast': ['echo', 'rhs2']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out':
                [('zFirst', 'rhs1', 4),
                 ('aLast', 'rhs2', 4)],
                'max_lhs': 6, 'max_rhs': 4})
        self.assertEqual (returned, expected)

    def testUnderscoreToSpace (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'Replace_underscore': ['echo', 'rhs']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out':
                [('Replace underscore', 'rhs', 3)],
                'max_lhs': 18, 'max_rhs': 3})
        self.assertEqual (returned, expected)

if __name__ == '__main__':
    unittest.main ()

