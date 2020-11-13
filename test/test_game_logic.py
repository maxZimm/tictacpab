import unittest
from unittest.mock import patch
import sys
sys.path.append('..')
from player import Player
from io import StringIO
from game_logic import GameLogic

class TestGameLogicMethods(unittest.TestCase):

    @patch('builtins.input', side_effect=['ScaryTerry','Holt'])
    def test_getplayer(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        game = GameLogic()
        self.assertIsInstance(game.player_1, Player)
        self.assertIsInstance(game.player_2, Player)
        self.assertEqual(game.player_1.name, 'ScaryTerry')
        self.assertEqual(game.player_2.name, 'Holt')
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
         

