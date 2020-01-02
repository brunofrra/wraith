#!/usr/bin/python3
import run_commands
import unittest

class TestRunCommands (unittest.TestCase):

    def testMultiLineCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['printf', 'foo\nbar\n']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out':
                [('lhs', 'foo', 3), ('', 'bar', 3)]})
        self.assertEqual (returned, expected)

    def testCommandFail (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['false']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'err': [(
                "Command 'lhs' returned a non-success code")]})
        self.assertEqual (returned, expected)

    def testCommandTimeout (self):
        config = {'Command_options': {'Timeout': 0.1},
                'Info': {'lhs': ['sleep', '2']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'err': [(
                "Command 'lhs' not done after timeout")]})
        self.assertEqual (returned, expected)

    def testIntCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': 2}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out': [(''), ('')]})
        self.assertEqual (returned, expected)
    
    def testCenteredOutput (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'_centered_output_': ['echo', 'rhs']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out':
                [('_centered_', 'rhs', 3)]})
        self.assertEqual (returned, expected)

    def testNoLhs (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'_no_lhs': ['echo', 'rhs']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out': [('', 'rhs', 3)]})
        self.assertEqual (returned, expected)
    
    def testUnderscoreToSpace (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'Replace_underscore': ['echo', 'rhs']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out':
                [('Replace underscore', 'rhs', 3)]})
        self.assertEqual (returned, expected)

    def testListCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['echo', 'rhs']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out': [('lhs', 'rhs', 3)]})
        self.assertEqual (returned, expected)

    def testStringCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': 'echo rhs'}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out': [('lhs', 'rhs', 3)]})
        self.assertEqual (returned, expected)

    def testTwoCommands (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'zFirst': 'echo rhs1', 'aLast': ['echo', 'rhs2']}}
        returned = run_commands.run (config)
        expected = run_commands.CommandOutput (**{'out':
                [('zFirst', 'rhs1', 4),
                 ('aLast', 'rhs2', 4)]})
        self.assertEqual (returned, expected)

if __name__ == '__main__':
    unittest.main ()

