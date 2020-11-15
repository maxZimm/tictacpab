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

    @patch('builtins.input', side_effect=['ScaryTerry','Holt'])
    def test_checkwinner(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        game = GameLogic()
        self.assertEqual(game.check_winner(), None)
        game.moves.state['mid']['l'] = 1
        game.moves.state['mid']['m'] = 1
        game.moves.state['mid']['r'] = 1
        self.assertEqual(game.check_winner(), 1)
        game.moves.state['mid']['m'] = 2
        self.assertEqual(game.check_winner(), None)
        game.moves.state['top']['r'] = 2
        game.moves.state['bot']['l'] = 2
        self.assertEqual(game.check_winner(), 2)
        game.moves.state['top']['l'] = 1
        game.moves.state['bot']['l'] = 1
        self.assertEqual(game.check_winner(), 1)
        sys.stdout = sys.__stdout__
         

if __name__ == '__main__':
    unittest.main()
