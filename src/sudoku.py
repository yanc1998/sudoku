class Sudoku:
    def __init__(self, board):
        self.board = board
        self.all_solves = []

    def check_sudoku_sol(self, board):
        n = len(board[0])
        for posx, posy in self.pos_board(n - 2, n - 2, 3):
            if posx == posy == 6:
                print('a')
            if not self.check_3x3_square(board, posx, posy):
                return False

        return True

    def check_3x3_square(self, board, posx, posy):
        visit_pos = {}
        dis = 3
        for x, y in self.pos_board(dis, dis, 1):
            nx = x + posx
            ny = y + posy
            value = board[nx][ny]
            if visit_pos.__contains__(value) or (value < 0 or value > 9):
                return False
            else:
                visit_pos[value] = True

        return True

    def create_sudoku_candidates(self, board):
        empty_pos = self.find_empty_pos(board)
        candidates = {}
        for x, y in empty_pos:
            candidates[(x, y)] = self.valid(board, x, y)
        return candidates

    def find_unico_oculto(self, board):
        candidates = self.create_sudoku_candidates(board)
        sol = []
        for c in candidates:
            if len(candidates[c]) == 1:
                sol.append((candidates[c], c))
        return sol

    def valid(self, board, posx, posy):
        col = self.find_column(board, posx, posy)
        fil = self.find_fil(board, posx, posy)
        valid = []
        for i in range(1, 10):
            if not col.__contains__(i) and not fil.__contains__(i):
                valid.append(i)

        return valid

    def find_fil(self, board, _posx, _posy):
        take_values = set()
        for i in range(_posx, len(board[0])):
            take_values.add(board[i][_posy])
        for i in range(_posx, -1, -1):
            take_values.add(board[i][_posy])
        return take_values

    def find_column(self, board, _posx, _posy):
        take_values = set()
        for i in range(_posy, len(board)):
            take_values.add(board[_posx][i])
        for i in range(_posx, -1, -1):
            take_values.add(board[_posx][i])
        return take_values

    def find_empty_pos(self, board):
        list_index_empty = []
        for x, y in self.pos_board(len(board[0]), len(board), 1):
            if board[x][y] == 0:
                list_index_empty.append((x, y))
        return list_index_empty

    def pos_board(self, x, y, increment):
        for i in range(0, x, increment):
            for j in range(0, y, increment):
                yield i, j

    def solve(self, board):
        self.all_solves = []
        self._solve(board)
        return self.all_solves

    def _solve(self, board):

        # poner los que tienen que ir obligado
        unicos_oculto = self.find_unico_oculto(board)
        while len(unicos_oculto) > 0:
            for value, (x, y) in unicos_oculto:
                board[x][y] = value[0]
            unicos_oculto = self.find_unico_oculto(board)

        if self.check_sudoku_sol(board):
            self.all_solves.append(board.copy())
            return

        candidates = self.create_sudoku_candidates(board)
        for c in candidates:
            for value in candidates[c]:
                board[c[0]][c[1]] = value
                self.solve(board)
                board[c[0]][c[1]] = 0
