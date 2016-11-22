from tkinter import *


class SudokuUI(Frame):
    """ The Tkinter UI, responsible for drawing the board and accepting user input.
    """

    MARGIN = 20  # Margen de pixeles alrededor de la Tabla
    SIDE = 50  # Largo de cada cuadrado del grid
    WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Ancho y Alto de la cuadrícula

    def __init__(self, parent, game):
        self.game = game
        self.algX_solution = self.game.get_solucion_algX()
        self.comprobando_solucion = False
        self.parent = parent
        Frame.__init__(self, parent)

        self.fila, self.columna = 0, 0

        self.__initUI()

    def __initUI(self):
        self.parent.title("SudokIhToN - Huecos: " + str(
            self.game.get_nums_string().count('0')) + " - Posibles Soluciones: " + str(len(self.game.get_soluciones())))
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=self.WIDTH,
                             height=self.HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Limpiar Respuestas",
                              command=self.__limpiar_sudoku)
        clear_button.pack(expand=1, fill=BOTH, side=LEFT)

        generate_button = Button(self,
                                 text="Generar Nuevo Sudoku",
                                 command=self.__generar_sudoku)
        generate_button.pack(expand=1, fill=BOTH, side=RIGHT)

        check_button = Button(self,
                              text="Comprobar Solución",
                              command=self.__comprobar_solucion)
        check_button.pack(expand=1, fill=BOTH, side=TOP)

        solve_button = Button(self,
                              text="Solucionar Sudoku",
                              command=self.__solucionar_sudoku)
        solve_button.pack(expand=1, fill=BOTH, side=BOTTOM)

        self.__pintar_grid()
        self.__pintar_sudoku()

        self.canvas.bind("<Button-1>", self.__celda_clickada)
        self.canvas.bind("<Key>", self.__pulsar_tecla)

    def __pintar_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = self.MARGIN + i * self.SIDE
            y0 = self.MARGIN
            x1 = self.MARGIN + i * self.SIDE
            y1 = self.HEIGHT - self.MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = self.MARGIN
            y0 = self.MARGIN + i * self.SIDE
            x1 = self.WIDTH - self.MARGIN
            y1 = self.MARGIN + i * self.SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __pintar_sudoku(self):
        self.canvas.delete("numeros")
        for i in range(9):
            for j in range(9):
                answer = self.game.get_numero(i + 1, j + 1)
                if answer != 0:
                    x = self.MARGIN + j * self.SIDE + self.SIDE / 2
                    y = self.MARGIN + i * self.SIDE + self.SIDE / 2
                    color = "black" if self.game.cuadricula[i][j][1] else "red"
                    if not self.game.cuadricula[i][j][1] and answer == self.algX_solution[i][j] \
                            and self.comprobando_solucion:
                        color = "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numeros", fill=color
                    )

    def __limpiar_sudoku(self):
        print("Limpiamos las respuestas del sudoku")
        self.game.start(is_clear=True)
        self.canvas.delete("victory")
        self.__pintar_sudoku()
        self.fila, self.columna = -1, -1
        self.__pintar_cursor()

    def __generar_sudoku(self):
        print("Generamos un nuevo sudoku")
        self.__limpiar_sudoku()
        self.game.start()
        self.algX_solution = self.game.get_solucion_algX()
        self.canvas.delete("victory")
        self.__pintar_sudoku()
        self.fila, self.columna = -1, -1
        self.__pintar_cursor()
        self.parent.title("SudokIhToN - Huecos: " + str(
            self.game.get_nums_string().count('0')) + " - Posibles Soluciones: " + str(len(self.game.get_soluciones())))

    def __comprobar_solucion(self):
        print("Comprobar Solución")
        self.comprobando_solucion = True
        self.canvas.delete("victory")
        self.__pintar_sudoku()
        self.fila, self.columna = -1, -1
        self.__pintar_cursor()
        self.comprobando_solucion = False

    def __solucionar_sudoku(self):
        print("Solucionamos el Sudoku mediante el Dancing Links")
        self.__limpiar_sudoku()
        self.game.set_solucion_algX()
        self.comprobando_solucion = True
        self.canvas.delete("victory")
        self.__pintar_sudoku()
        self.fila, self.columna = -1, -1
        self.__pintar_cursor()
        self.comprobando_solucion = False

    def __celda_clickada(self, event):
        if self.game.game_over:
            return
        x, y = event.x, event.y
        if self.MARGIN < x < self.WIDTH - self.MARGIN \
                and self.MARGIN < y < self.HEIGHT - self.MARGIN:
            self.canvas.focus_set()

            # get columna and fila numbers from x,y coordinates
            fila, columna = int((y - self.MARGIN) / self.SIDE), int((x - self.MARGIN) / self.SIDE)

            # if cell was selected already - deselect it
            if (columna, fila) == (self.fila, self.columna):
                self.fila, self.columna = -1, -1
            elif not self.game.cuadricula[fila][columna][1]:
                self.fila, self.columna = fila, columna

        self.__pintar_cursor()

    def __pintar_cursor(self):
        self.canvas.delete("cursor")
        if self.fila >= 0 and self.columna >= 0:
            x0 = self.MARGIN + self.columna * self.SIDE + 1
            y0 = self.MARGIN + self.fila * self.SIDE + 1
            x1 = self.MARGIN + (self.columna + 1) * self.SIDE - 1
            y1 = self.MARGIN + (self.fila + 1) * self.SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )

    def __pulsar_tecla(self, event):
        if self.game.game_over:
            return
        if self.fila >= 0 and self.columna >= 0 and event.char in "1234567890":
            self.game.set_numero(self.fila + 1, self.columna + 1, int(event.char))
            self.fila, self.columna = -1, -1
            self.__pintar_sudoku()
            self.__pintar_cursor()
            if self.game.game_over:
                self.__pintar_victoria()

    def __pintar_victoria(self):
        # create a oval (which will be a circle)
        x0 = y0 = self.MARGIN + self.SIDE * 2
        x1 = y1 = self.MARGIN + self.SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        # create text
        x = y = self.MARGIN + 4 * self.SIDE + self.SIDE / 2
        self.canvas.create_text(
            x, y,
            text="Has Ganado!", tags="winner",
            fill="white", font=("Arial", 32)
        )
