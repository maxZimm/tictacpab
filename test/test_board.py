import unittest
import sys
sys.path.append('..')
from board import Board
from moves import Moves, InputError
from io import StringIO

class TestBoardMethods(unittest.TestCase):

    def test_topRow(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        board = Board()
        board.topRow()
        self.assertEqual('_|_|_\n', captured_output.getvalue())
        board.topRow(r=1)
        self.assertIn('_|_|X\n', captured_output.getvalue())
        board.topRow(l=2)
        self.assertIn('O|_|_\n', captured_output.getvalue())
        board.topRow(l=2,m=1)
        self.assertIn('O|X|_\n', captured_output.getvalue())
        sys.stdout = sys.__stdout__

    def test_middleRow(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        board = Board()
        board.middleRow()
        self.assertEqual('_|_|_\n', captured_output.getvalue())
        board.middleRow(r=1)
        self.assertIn('_|_|X\n', captured_output.getvalue())
        board.middleRow(l=2)
        self.assertIn('O|_|_\n', captured_output.getvalue())
        board.middleRow(l=2,m=1)
        self.assertIn('O|X|_\n', captured_output.getvalue())
        sys.stdout = sys.__stdout__

    def test_bottomRow(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        board = Board()
        board.bottomRow()
        self.assertEqual(' | | \n', captured_output.getvalue())
        board.bottomRow(r=1)
        self.assertIn(' | |X\n', captured_output.getvalue())
        board.bottomRow(l=2)
        self.assertIn('O| | \n', captured_output.getvalue())
        board.bottomRow(l=2,m=1)
        self.assertIn('O|X| \n', captured_output.getvalue())
        sys.stdout = sys.__stdout__

    def test_printBoard(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        board = Board()
        move = Moves()
        board.printBoard(move)
        self.assertEqual('_|_|_\n_|_|_\n | | \n', captured_output.getvalue())
        move.acceptMove({'top': 'l', 'player': 1})
        board.printBoard(move)
        self.assertIn('X|_|_\n_|_|_\n | | \n', captured_output.getvalue())
        sys.stdout = sys.__stdout__
        
if __name__  == '__main__':
    unittest.main()
