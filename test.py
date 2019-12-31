#!/usr/bin/python3
import run_commands
import unittest

class TestRunCommands (unittest.TestCase):

    @unittest.skip ('Expected behaviour not yet defined')
    def testCommandFail (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['false']}}
        ret = run_commands.run (config)


    def testNoRhs (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': 2}}
        ret = run_commands.run (config)
        self.assertEqual (ret, [('', ''), ('', '')])
    
    def testNoLhs (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'_no_lhs': ['echo', 'rhs']}}
        ret = run_commands.run (config)
        self.assertEqual (ret, [('', 'rhs')])
    
    def testUnderscoreToSpace (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'Replace_underscore': ['echo', 'rhs']}}
        ret = run_commands.run (config)
        self.assertEqual (ret, [('Replace underscore', 'rhs')])

    def testListCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': ['echo', 'rhs']}}
        ret = run_commands.run (config)
        self.assertEqual (ret, [('lhs', 'rhs')])

    def testStringCommand (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'lhs': 'echo rhs'}}
        ret = run_commands.run (config)
        self.assertEqual (ret, [('lhs', 'rhs')])

    def testTwoCommands (self):
        config = {'Command_options': {'Timeout': 10},
                'Info': {'zFirst': 'echo rhs1', 'aLast': ['echo', 'rhs2']}}
        ret = run_commands.run (config)
        self.assertEqual (ret, [('zFirst', 'rhs1'), ('aLast', 'rhs2')])

if __name__ == '__main__':
    unittest.main ()

