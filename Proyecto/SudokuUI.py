from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM


class SudokuUI(Frame):
    """ The Tkinter UI, responsible for drawing the board and accepting user input.
    """

    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()

    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=self.game.WIDTH,
                             height=self.game.HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        solve_button = Button(self,
                              text="Solve Sudoku",
                              command=self.__solve_sudoku)
        solve_button.pack(fill=BOTH, side=BOTTOM)
        clear_button = Button(self,
                              text="Clear Answers",
                              command=self.__clear_answers)
        clear_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = self.game.MARGIN + i * self.game.SIDE
            y0 = self.game.MARGIN
            x1 = self.game.MARGIN + i * self.game.SIDE
            y1 = self.game.HEIGHT - self.game.MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = self.game.MARGIN
            y0 = self.game.MARGIN + i * self.game.SIDE
            x1 = self.game.WIDTH - self.game.MARGIN
            y1 = self.game.MARGIN + i * self.game.SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                print(i, j)
                answer = self.game.get_numero(j + 1, i + 1)
                if answer != 0:
                    x = self.game.MARGIN + j * self.game.SIDE + self.game.SIDE / 2
                    y = self.game.MARGIN + i * self.game.SIDE + self.game.SIDE / 2
                    original = self.game.get_numero(j + 1, i + 1)
                    color = "black" if answer == original else "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )

    def __solve_sudoku(self):
        self.game.cuadricula = self.game.get_solucion_algX()
        self.canvas.delete("victory")
        self.__draw_puzzle()

    def __clear_answers(self):
        self.game.start(is_clear=True)
        self.canvas.delete("victory")
        self.__draw_puzzle()

    def __cell_clicked(self, event):
        if self.game.game_over:
            return
        x, y = event.x, event.y
        if self.game.MARGIN < x < self.game.WIDTH - self.game.MARGIN and self.game.MARGIN < y < self.game.HEIGHT - self.game.MARGIN:
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row, col = int((y - self.game.MARGIN) / self.game.SIDE), int((x - self.game.MARGIN) / self.game.SIDE)


            # if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.game.get_numero(row+1, col+1) == 0:
                self.row, self.col = row, col

            print(row+1, col+1, self.game.get_numero(row+1, col+1))

        self.__draw_cursor()

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = self.game.MARGIN + self.col * self.game.SIDE + 1
            y0 = self.game.MARGIN + self.row * self.game.SIDE + 1
            x1 = self.game.MARGIN + (self.col + 1) * self.game.SIDE - 1
            y1 = self.game.MARGIN + (self.row + 1) * self.game.SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )

    def __key_pressed(self, event):
        if self.game.game_over:
            return
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.game.set_numero(self.row, self.col, event.char)
            self.col, self.row = -1, -1
            self.__draw_puzzle()
            self.__draw_cursor()
            if self.game.check_solucion():
                self.__draw_victory()

    def __draw_victory(self):
        # create a oval (which will be a circle)
        x0 = y0 = self.game.MARGIN + self.game.SIDE * 2
        x1 = y1 = self.game.MARGIN + self.game.SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        # create text
        x = y = self.game.MARGIN + 4 * self.game.SIDE + self.game.SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="winner",
            fill="white", font=("Arial", 32)
        )
