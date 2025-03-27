class Figure(object):
    """Шахматная фигура"""
    def __init__(self, color=None, symbol=None):
        """Инициализирует фигуры.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        self.color = color
        self.symbol = symbol

class Rook(Figure):
    """Ладья"""
    def __init__(self, color, symbol):
        """Инициализирует ладью.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        """Проверяет ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.
          board (list): Шахматная доска.

        Returns:
          bool: Допустимость хода.
        """
        if start[0] == end[0]: 
          for column in range(start[1] + 1, end[1]):
             if board[start[0]][column]:
                return False
        elif start[1] == end[1]: 
          for row in range(start[0] + 1, end[0]):
             if board[row][start[1]]:
                return False
        else:
          return False
        return True

class Pawn(Figure):
    """Пешка"""
    def __init__(self, color, symbol):
        """Инициализирует пешку.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        """Проверяет ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.
          board (list): Шахматная доска.

        Returns:
          bool: Допустимость хода.
        """
        if self.color == 'white':
          if start[0] == 1 and end[0] == 3 and start[1] == end[1] and not board[2][end[1]] and not board[3][end[1]]:
            return True
          elif start[0] + 1 == end[0] and start[1] == end[1] and not board[end[0]][end[1]]:
            return True
        else:
          if start[0] == 6 and end[0] == 4 and start[1] == end[1] and not board[5][start[1]] and not board[4][start[1]]:
            return True
          elif start[0] - 1 == end[0] and start[1] == end[1] and not board[end[0]][end[1]]:
            return True
        if abs(end[0]-start[0] == 1) and abs(end[1]-start[1]) == 1:
          if board[end[0]][end[1]] and board[end[0]][end[1]].color != self.color:
            return True
        return False

class Knight(Figure):
    """Конь"""
    def __init__(self, color, symbol):
        """Инициализирует коня.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        """Проверяет ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.
          board (list): Шахматная доска.

        Returns:
          bool: Допустимость хода.
        """
        step_1 = abs(start[0] - end[0])
        step_2 = abs(start[1] - end[1])
        return (step_1 == 2 and step_2 == 1) or (step_1 == 1 and step_2 == 2)

class Bishop(Figure):
    """Слон"""
    def __init__(self, color, symbol):
        """Инициализирует слона.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        """Проверяет ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.
          board (list): Шахматная доска.

        Returns:
          bool: Допустимость хода.
        """
        diag_horiz = abs(start[0] - end[0])
        diag_vert = abs(start[1] - end[1])
        if diag_horiz != diag_vert:
            return False
        move_horiz = 1 if end[0] > start[0] else -1
        move_vert = 1 if end[1] > start[1] else -1
        coord_1, coord_2 = start[0] + move_horiz, start[1] + move_vert
        while (coord_1, coord_2) != end:
            if board[coord_1][coord_2]:
                return False
            coord_1 += move_horiz
            coord_2 += move_vert
        return True

class King(Figure):
    """Король"""
    def __init__(self, color, symbol):
        """Инициализирует короля.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        """Проверяет ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.
          board (list): Шахматная доска.

        Returns:
          bool: Допустимость хода.
        """
        step_1 = abs(start[0] - end[0])
        step_2 = abs(start[1] - end[1])
        return (step_1 <= 1 and step_2 <= 1)

class Queen(Figure):
    """Королева"""
    def __init__(self, color, symbol):
        """Инициализирует фигуры.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        super().__init__(color, symbol)
  
    def is_valid_move(self, start, end, board):
        """Проверяет ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.
          board (list): Шахматная доска.

        Returns:
          bool: Допустимость хода.
        """
        if start[0] == end[0]: 
          for column in range(start[1] + 1, end[1]):
             if board[start[0]][column]:
                return False
        elif start[1] == end[1]: 
          for row in range(start[0] + 1, end[0]):
             if board[row][start[1]]:
                return False
        
        else:
            diag_horiz = abs(start[0] - end[0])
            diag_vert = abs(start[1] - end[1])
            if diag_horiz != diag_vert:
                return False
            move_horiz = 1 if end[0] > start[0] else -1
            move_vert = 1 if end[1] > start[1] else -1
            coord_1, coord_2 = start[0] + move_horiz, start[1] + move_vert
            while (coord_1, coord_2) != end:
                if board[coord_1][coord_2]:
                    return False
                coord_1 += move_horiz
                coord_2 += move_vert
        return True

class Scandic(Figure):
    """Скандик"""
    def __init__(self, color, symbol):
        """Инициализирует скандик.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        """Проверяет ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.
          board (list): Шахматная доска.

        Returns:
          bool: Допустимость хода.
        """
        step_1 = abs(start[0] - end[0])
        step_2 = abs(start[1] - end[1])
        return (step_1 <= 2 and step_2 <= 2)

class Viperr(Figure):
    """Вайперр"""
    def __init__(self, color, symbol):
        """Инициализирует вайперр.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        """Проверяет ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.
          board (list): Шахматная доска.

        Returns:
          bool: Допустимость хода.
        """
        step_1 = abs(start[0] - end[0])
        step_2 = abs(start[1] - end[1])
        return (step_1 == step_2 == 1)

class Timur(Figure):
    """Тимур"""
    def __init__(self, color, symbol):
        """Инициализирует Тимура.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        """Проверяет ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.
          board (list): Шахматная доска.

        Returns:
          bool: Допустимость хода.
        """
        step_1 = abs(start[0] - end[0])
        step_2 = abs(start[1] - end[1])
        return (step_1 == 3 and step_2 == 1) or (step_1 == 1 and step_2 == 3)

class Game(object):
    """Игра"""
    def __init__(self):
        """Инициализирует фигуры.

        Args:
          color (str): Цвет фигуры. 
          symbol (str): Символ фигуры.
        """
        self.current_turn = 'white'
        self.count = 0
        self.fields = self._initialize_board()
        self._place_pieces()

    def _initialize_board(self):
        return [[None for _ in range(8)] for _ in range(8)]

    def _place_pieces(self):
        self.fields[0][0] = Rook('white', 'R')
        self.fields[0][7] = Rook('white', 'R')
        self.fields[7][0] = Rook('black', 'R')
        self.fields[7][7] = Rook('black', 'R')
        self.fields[0][6] = Viperr('white', 'v')
        self.fields[7][6] = Viperr('black', 'v')
        self.fields[1][0] = Timur('white', 't')
        self.fields[6][0] = Timur('black', 't')
        self.fields[1][7] = Scandic('white', 's')
        self.fields[6][7] = Scandic('black', 's')
        self.fields[0][1] = Knight('white', 'k')
        self.fields[7][1] = Knight('black', 'k')
        self.fields[0][3] = King('white', 'K')
        self.fields[7][3] = King('black', 'K')
        self.fields[0][4] = Queen('white', 'Q')
        self.fields[7][4] = Queen('black', 'Q')
        self.fields[0][2] = Bishop('white', 'b')
        self.fields[0][5] = Bishop('white', 'b')
        self.fields[7][2] = Bishop('black', 'b')
        self.fields[7][5] = Bishop('black', 'b')
        for place in range (1,7):
          self.fields[1][place] = Pawn('white', 'p')
          self.fields[6][place] = Pawn('black', 'p')

    def display_board(self):
        """Шахматная доска"""
        print("  A B C D E F G H")
        for index, row in enumerate(self.fields, start=1):
          print(f"{8 - index + 1} ", end='')  
          print(' '.join([str(cell.symbol) if cell else '.' for cell in row] + [f" {8 - index + 1}"]))
        print("  A B C D E F G H")  

    def validate_move(self, start, end):
        """Проверяет ход.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.

        Returns:
          bool: Допустимость хода.
        """
        piece = self.fields[start[0]][start[1]]
        if not piece:
          return False
        if self.fields[end[0]][end[1]] and self.fields[end[0]][end[1]].color == piece.color:
          return False 
        return piece.is_valid_move(start, end, self.fields)

    def make_move(self, start, end):
        """Ход фигуры.

        Args:
          start (tuple): Начальные координаты фигуры.
          end (tuple): Конечные координаты фигуры.

        Returns:
          bool: Выполнение хода.
        """
        if self.fields[start[0]][start[1]].color != self.current_turn:
          return False
            
        if start[0] < 0 or start[0] >= 8 or start[1] < 0 or start[1] >= 8:
            return False
        if end[0] < 0 or end[0] >= 8 or end[1] < 0 or end[1] >= 8:
            return False  
            
        if self.validate_move(start, end):
          piece = self.fields[start[0]][start[1]]
          self.fields[start[0]][start[1]] = None
          self.fields[end[0]][end[1]] = piece
          self.count += 1
            
          if isinstance(piece, Pawn) and (end[0] == 0 or end[0] == 7):
            choice = input('which piece do you want the pawn turn into')
            if choice == 'Queen':
              self.fields[end[0]][end[1]] = Queen(piece.color, 'Q')
            elif choice == 'Rook':
              self.fields[end[0]][end[1]] = Rook(piece.color, 'R')
            elif choice == 'Bishop':
              self.fields[end[0]][end[1]] = Bishop(piece.color, 'b')
            elif choice == 'Knight':
              self.fields[end[0]][end[1]] = Knight(piece.color, 'k')
            elif choice == 'Viperr':
              self.fields[end[0]][end[1]] = Viperr(piece.color, 'v')
            elif choice == 'Timur':
              self.fields[end[0]][end[1]] = Timur(piece.color, 't')
            elif choice == 'Scandic':
              self.fields[end[0]][end[1]] = Scandic(piece.color, 's')
                
          self.current_turn = 'black' if self.current_turn == 'white' else 'white'
          return True
        return False

    def is_check(self, color):
        """Король под шахом.

        Args:
          color (str): Цвет фигуры.

        Returns:
          bool: Нахождение под шахом.
        """
        king_position = None
        for coord_1 in range(8):
            for coord_2 in range(8):
                if isinstance(self.fields[coord_1][coord_2], King) and self.fields[coord_1][coord_2].color == color:
                    king_position = (coord_1, coord_2)
                    break
            if king_position:
                break
        if not king_position:
            return False  
        for coord_1 in range(8):
            for coord_2 in range(8):
                piece = self.fields[coord_1][coord_2]
                if piece and piece.color != color:
                    if piece.is_valid_move((coord_1, coord_2), king_position, self.fields):
                        return True  
        return False

    def is_checkmate(self, color):
        """Мат.

        Args:
          color (str): Цвет фигуры.

        Returns:
          bool: Мат королю.
        """
        if not self.is_check(color):
            return False 
        king_position = None
        for coord_1 in range(8):
            for coord_2 in range(8):
                if isinstance(self.fields[coord_1][coord_2], King) and self.fields[coord_1][coord_2].color == color:
                    king_position = (coord_1, coord_2)
                    break
            if king_position:
                break
        if not king_position:
            return False

        for coord_1 in range(8):
            for coord_2 in range(8):
                piece = self.fields[coord_1][coord_2]
                if piece and piece.color != color:
                    if piece.is_valid_move((coord_1, coord_2), king_position, self.fields):
                        return False
        return True
            
def convert_coordinates(coord_1, coord_2):
    coord_1 = ord(coord_1) - ord('A')
    coord_2 = 8 - int(coord_2)
    return (coord_2, coord_1)

game = Game()

while True:
    game.display_board()
    start_x = input('which piece you move (A-H): ')
    start_y = input('which piece you move (1-8): ')
    start = convert_coordinates(start_x, start_y)
    end_x = input('where you move (A-H): ')
    end_y = input('where you move (1-8): ')
    end = convert_coordinates(end_x, end_y)
    game.make_move(start, end)
    game.display_board()
    print(f'Move counter: {game.count}\n')
