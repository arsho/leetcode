'''
Title     : 999. Available Captures for Rook
Category  : Array
URL       : https://leetcode.com/problems/available-captures-for-rook/
Author    : arsho
Created   : 12 April 2019
'''
import unittest


class Solution(object):

    def getSymbolPosition(self, board, symbol):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == symbol:
                    return [i, j]
        return None

    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        Input description:
        empty squares: '.'
        black pawns: 'p'
        white bishops: 'B'
        white rook: 'R'
        :rtype: int
        """
        empty_square = '.'
        black_pawn = 'p'
        white_bishop = 'B'
        white_rook = 'R'

        rook_x, rook_y = self.getSymbolPosition(board, white_rook)
        count_black_pawn = 0

        # count north side pawn
        for i in range(rook_x, -1, -1):
            if board[i][rook_y] == white_bishop:
                break
            if board[i][rook_y] == black_pawn:
                count_black_pawn += 1
                break

        # count south side pawn
        for i in range(rook_x, len(board)):
            if board[i][rook_y] == white_bishop:
                break
            if board[i][rook_y] == black_pawn:
                count_black_pawn += 1
                break

        # count east side pawn
        for j in range(rook_y, -1, -1):
            if board[rook_x][j] == white_bishop:
                break
            if board[rook_x][j] == black_pawn:
                count_black_pawn += 1
                break

        # count west side pawn
        for j in range(rook_y, len(board[0])):
            if board[rook_x][j] == white_bishop:
                break
            if board[rook_x][j] == black_pawn:
                count_black_pawn += 1
                break

        return count_black_pawn


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_no_white_bishop(self):
        # example 1
        board = [[".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", "p", ".", ".", ".", "."],
                 [".", ".", ".", "R", ".", ".", ".", "p"],
                 [".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", "p", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."]]
        assert self.solution.numRookCaptures(board) == 3

    def test_white_bishops_all_side(self):
        # example 2
        board = [[".", ".", ".", ".", ".", ".", ".", "."],
                 [".", "p", "p", "p", "p", "p", ".", "."],
                 [".", "p", "p", "B", "p", "p", ".", "."],
                 [".", "p", "B", "R", "B", "p", ".", "."],
                 [".", "p", "p", "B", "p", "p", ".", "."],
                 [".", "p", "p", "p", "p", "p", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."]]
        assert self.solution.numRookCaptures(board) == 0

    def test_white_bishops_black_pawns(self):
        # example 3
        board = [[".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", "p", ".", ".", ".", "."],
                 [".", ".", ".", "p", ".", ".", ".", "."],
                 ["p", "p", ".", "R", ".", "p", "B", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", "B", ".", ".", ".", "."],
                 [".", ".", ".", "p", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."]]
        assert self.solution.numRookCaptures(board) == 3


if __name__ == '__main__':
    pass
    # Unit tests are for local testing. Leetcode doesn't support this.
    # Uncomment the following line to test code locally
    # unittest.main()
