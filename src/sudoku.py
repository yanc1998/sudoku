class Sudoku:
    def __init__(self, board):
        self.board = board

    def check_sudoku_sol(self, board):
        n = len(board[0])
        for posx in range(0, n - 2, 3):
            for posy in range(0, n - 2, 3):
                if posx == posy == 6:
                    print('a')
                if not self.check_3x3_square(board, posx, posy):
                    return False

        return True

    def check_3x3_square(self, board, posx, posy):
        visit_pos = {}
        dis = 3
        for x in range(dis):
            for y in range(dis):
                nx = x + posx
                ny = y + posy
                value = board[nx][ny]
                if visit_pos.__contains__(value) or (value < 0 or value > 9):
                    return False
                else:
                    visit_pos[value] = True

        return True
