import unittest
from unittest.mock import patch
import sys
sys.path.append('..')
from player import Player
from io import StringIO

class TestPlayerMethods(unittest.TestCase):

    @patch('builtins.input', side_effect=['Jo','John'])
    def test_getName(self, mock_input):
        output = Player(1)
        self.assertEqual(output.name, 'John')

    @patch('builtins.input', side_effect=['ScaryTerry','Top ',' R'])
    def test_getMove(self, mock_input):
        output = Player(1)
        move = output.getMove()
        self.assertEqual(move, {'top': 'r', 'player': 1})

    @patch('builtins.input', side_effect=['ScaryJerry','RaT ',' z', 'mid', 'm'])
    def test_getMove(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        output = Player(1)
        move = output.getMove()
        self.assertEqual(move, {'mid': 'm', 'player': 1})
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()        
