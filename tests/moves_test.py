import unittest
import sys
sys.path.append('..')
from moves import Moves

class TestMovesMethods(unittest.TestCase):

    def test_acceptmove(self):
        move = Moves()
        move.acceptMove({'top': 'l', 'player': 1})
        self.assertEqual(move.topRow, {'l': 1, 'm':0, 'r':0})

    def test_showavailmoves(self):
        move = Moves()
        self.assertEqual(move.showAvailMoves()['topRow'], [])
        self.assertEqual(move.showAvailMoves()['midRow'], [])
        self.assertEqual(move.showAvailMoves()['botRow'], [])

if __name__  == '__main__':
    unittest.main()
