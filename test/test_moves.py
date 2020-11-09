import unittest
import sys
sys.path.append('..')
from moves import Moves, InputError

class TestMovesMethods(unittest.TestCase):

    def test_acceptmove(self):
        move = Moves()
        move.acceptMove({'top': 'l', 'player': 1})
        self.assertEqual(move.topRow, {'l': 1, 'm':0, 'r':0})
        self.assertRaises(InputError, move.acceptMove, {'top': 'l', 'player': 2})
        move.acceptMove({'mid': 'm', 'player': 2})
        self.assertEqual(move.midRow, {'l': 0, 'm':2, 'r':0})
        move.acceptMove({'bot': 'r', 'player': 2})
        self.assertEqual(move.botRow, {'l': 0, 'm':0, 'r':2})
        move.acceptMove({'bot': 'm', 'player': 1})
        self.assertEqual(move.botRow, {'l': 0, 'm':1, 'r':2})
        

    def test_showavailmoves(self):
        move = Moves()
        self.assertEqual(move.showAvailMoves(), {'topRow':['l','m','r'],
                                                 'midRow':['l','m','r'],
                                                 'botRow':['l','m','r']})
        move.acceptMove({'mid': 'm', 'player': 2})
        self.assertEqual(move.showAvailMoves()['midRow'], ['l','r'])
        move.acceptMove({'mid': 'l', 'player': 1})
        move.acceptMove({'mid': 'r', 'player': 2})
        self.assertEqual(move.showAvailMoves()['midRow'], [])

if __name__  == '__main__':
    unittest.main()
