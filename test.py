#!/usr/bin/python3
import run_commands
import unittest

class TestRunCommands (unittest.TestCase):

    def testCommandFail (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['false']}}
        ret, err = run_commands.run (config)
        self.assertEqual (ret, [])
        self.assertEqual (err, ["Command 'lhs' returned a non-success code"])

    def testCommandTimeout (self):
        config = {'Command_options': {'Timeout': 1},
                'Info': {'lhs': ['sleep', '2']}}
        ret, err = run_commands.run (config)
        self.assertEqual (ret, [])
        self.assertEqual (err, ["Command 'lhs' not done after timeout"])

    def testIntCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': 2}}
        ret, err = run_commands.run (config)
        self.assertEqual (ret, [('', ''), ('', '')])
        self.assertEqual (err, [])
    
    def testCenteredOutput (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'_centered_output_': ['echo', 'rhs']}}
        ret, err = run_commands.run (config)
        self.assertEqual (ret, [('_centered_', 'rhs')])
        self.assertEqual (err, [])

    def testNoLhs (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'_no_lhs': ['echo', 'rhs']}}
        ret, err = run_commands.run (config)
        self.assertEqual (ret, [('', 'rhs')])
        self.assertEqual (err, [])
    
    def testUnderscoreToSpace (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'Replace_underscore': ['echo', 'rhs']}}
        ret, err = run_commands.run (config)
        self.assertEqual (ret, [('Replace underscore', 'rhs')])
        self.assertEqual (err, [])

    def testListCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['echo', 'rhs']}}
        ret, err = run_commands.run (config)
        self.assertEqual (ret, [('lhs', 'rhs')])
        self.assertEqual (err, [])

    def testStringCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': 'echo rhs'}}
        ret, err = run_commands.run (config)
        self.assertEqual (ret, [('lhs', 'rhs')])
        self.assertEqual (err, [])

    def testTwoCommands (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'zFirst': 'echo rhs1', 'aLast': ['echo', 'rhs2']}}
        ret, err = run_commands.run (config)
        self.assertEqual (ret, [('zFirst', 'rhs1'), ('aLast', 'rhs2')])
        self.assertEqual (err, [])

if __name__ == '__main__':
    unittest.main ()

