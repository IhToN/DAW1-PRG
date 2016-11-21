from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, LEFT, RIGHT, BOTTOM


class SudokuUI(Frame):
    """ The Tkinter UI, responsible for drawing the board and accepting user input.
    """

    def __init__(self, parent, game):
        self.game = game
        self.algX_solution = self.game.get_solucion_algX()
        self.parent = parent
        Frame.__init__(self, parent)

        self.fila, self.columna = 0, 0

        self.__initUI()

    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=self.game.WIDTH,
                             height=self.game.HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Limpiar Respuestas",
                              command=self.__clear_answers)
        clear_button.pack(expand=1, fill=BOTH, side=LEFT)
        solve_button = Button(self,
                              text="Solucionar Sudoku",
                              command=self.__solve_sudoku)
        solve_button.pack(expand=1, fill=BOTH, side=RIGHT)

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
        self.canvas.delete("numeros")
        for i in range(9):
            for j in range(9):
                answer = self.game.get_numero(i + 1, j + 1)
                if answer != 0:
                    x = self.game.MARGIN + j * self.game.SIDE + self.game.SIDE / 2
                    y = self.game.MARGIN + i * self.game.SIDE + self.game.SIDE / 2
                    color = "black" if self.game.cuadricula[i][j][1] else "red"
                    if not self.game.cuadricula[i][j][1] and answer == self.algX_solution[i][j]:
                        color = "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numeros", fill=color
                    )

    def __solve_sudoku(self):
        self.__clear_answers()
        self.game.set_solucion_algX()
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
        if self.game.MARGIN < x < self.game.WIDTH - self.game.MARGIN \
                and self.game.MARGIN < y < self.game.HEIGHT - self.game.MARGIN:
            self.canvas.focus_set()

            # get columna and fila numbers from x,y coordinates
            fila, columna = int((y - self.game.MARGIN) / self.game.SIDE), int((x - self.game.MARGIN) / self.game.SIDE)

            # if cell was selected already - deselect it
            if (columna, fila) == (self.fila, self.columna):
                self.fila, self.columna = -1, -1
            elif not self.game.cuadricula[fila][columna][1]:
                self.fila, self.columna = fila, columna

        self.__draw_cursor()

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.fila >= 0 and self.columna >= 0:
            x0 = self.game.MARGIN + self.columna * self.game.SIDE + 1
            y0 = self.game.MARGIN + self.fila * self.game.SIDE + 1
            x1 = self.game.MARGIN + (self.columna + 1) * self.game.SIDE - 1
            y1 = self.game.MARGIN + (self.fila + 1) * self.game.SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )

    def __key_pressed(self, event):
        if self.game.game_over:
            return
        if self.fila >= 0 and self.columna >= 0 and event.char in "1234567890":
            self.game.set_numero(self.fila + 1, self.columna + 1, event.char)
            self.fila, self.columna = -1, -1
            self.__draw_puzzle()
            self.__draw_cursor()
            self.game.check_solucion()
            if self.game.game_over:
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
            text="Has Ganado!", tags="winner",
            fill="white", font=("Arial", 32)
        )
