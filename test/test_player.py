import unittest
from unittest.mock import patch
import sys
sys.path.append('..')
from player import Player
from io import StringIO

class TestPlayerMethods(unittest.TestCase):

    @patch('builtins.input', side_effect=['Jo','John'])
    def test_getName(self, mock_input):
        output = Player()
        self.assertEqual(output.name, 'John')

    @patch('builtins.input', side_effect=['ScaryTerry','top ',' r'])
    def test_getMove(self, mock_input):
        # need to determine format we might want
        # cool things is we can play around with that here to help
        # determine the shape of the data we want to send to GameLogic which in turn will send it to moves?
        output = Player()
        move = output.getMove()
        self.assertEqual(move, ('top', 'r'))

if __name__ == '__main__':
    unittest.main()        
