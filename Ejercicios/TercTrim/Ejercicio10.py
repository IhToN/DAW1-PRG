"""
    Crear un conversor de temperatura entre grados Celsius, Fahrenheit y Kelvin.
"""

import tkinter


class Ventana(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent, background='white')

        print("Init Frame")

        self.parent = parent
        self.vc_cls = tkinter.DoubleVar()
        self.vc_kel = tkinter.DoubleVar()
        self.vc_fah = tkinter.DoubleVar()

        self.initUI()

        self.bind("<Button-1>", self.callback)

    def initUI(self):
        '''Interfaz Gráfico'''
        self.parent.title('Ejercicio 10')
        self.grid()

        print("Init GUI")
        self.initTXT()
        # self.initBTN()

    def initTXT(self):
        vcmd = (self.register(self.validate_float), '%P', '%S')

        self.txt_cls = tkinter.Label(self, text='Celsius:', background='white')
        self.etr_cls = tkinter.Entry(self, textvariable=self.vc_cls, validate='key', validatecommand=vcmd)
        self.txt_cls.grid(row=0, column=0, sticky='W')
        self.etr_cls.grid(row=0, column=2, sticky='E')
        self.etr_cls.bind("<Return>", self.from_celsius)
        self.etr_cls.bind("<FocusIn>", self.clear)

        self.txt_kel = tkinter.Label(self, text='Kelvin:', background='white')
        self.etr_kel = tkinter.Entry(self, textvariable=self.vc_kel, validate='key', validatecommand=vcmd)
        self.txt_kel.grid(row=1, column=0, sticky='W')
        self.etr_kel.grid(row=1, column=2, sticky='E')
        self.etr_kel.bind("<Return>", self.from_kelvin)
        self.etr_kel.bind("<FocusIn>", self.clear)

        self.txt_fah = tkinter.Label(self, text='Fahrenheit:', background='white')
        self.etr_fah = tkinter.Entry(self, textvariable=self.vc_fah, validate='key', validatecommand=vcmd)
        self.txt_fah.grid(row=2, column=0, sticky='W')
        self.etr_fah.grid(row=2, column=2, sticky='E')
        self.etr_fah.bind("<Return>", self.from_fahrenheit)
        self.etr_fah.bind("<FocusIn>", self.clear)

        self.txt_info = tkinter.Label(self, text="Pulsa INTRO para aplicar el conversor.")
        self.txt_info.grid(row=5, column=0)

    def initBTN(self):
        self.txt_frm = tkinter.Label(self, text='Calcular desde:', background='white')
        self.txt_frm.grid(row=3, column=0, sticky='E')

        self.btn_cls = tkinter.Button(self, text='Celsius', command=self.from_celsius)
        self.btn_cls.grid(row=4, column=0)

        self.btn_kel = tkinter.Button(self, text='Kelvin', command=self.from_kelvin)
        self.btn_kel.grid(row=4, column=1)

        self.btn_fah = tkinter.Button(self, text='Fahrenheit', command=self.from_fahrenheit)
        self.btn_fah.grid(row=4, column=2)

    def validate_float(self, value_if_allowed, text):
        if text in '0123456789.-+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def from_celsius(self, event):
        grados = self.vc_cls.get()
        self.vc_kel.set(round(grados + 273.15, 2))
        self.vc_fah.set(round(1.8 * grados + 32, 2))

        self.callback(event)

    def from_kelvin(self, event):
        grados = self.vc_kel.get()
        self.vc_cls.set(round(grados - 273.15, 2))
        self.vc_fah.set(round(1.8 * grados - 459.67, 2))

        self.callback(event)

    def from_fahrenheit(self, event):
        grados = self.vc_fah.get()
        self.vc_cls.set(round((grados - 32) / 1.8, 2))
        self.vc_kel.set(round((459.67 + grados) / 1.8, 2))

        self.callback(event)

    def callback(self, event):
        self.focus_set()

    def clear(self, event):
        self.vc_cls.set(0.0)
        self.vc_kel.set(0.0)
        self.vc_fah.set(0.0)


def main():
    root = tkinter.Tk()
    app = Ventana(root)
    root.mainloop()


if __name__ == "__main__":
    main()

    # j1n869ddte77e
