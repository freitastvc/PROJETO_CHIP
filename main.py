from tkinter import *
from PIL import Image, ImageTk
import mos_GUI
import osc_GUI

janela = Tk()
janela.rowconfigure(1, weight=1)


janela.title("NOME")

menubar = Menu(janela)

def janela_osc():
    pop = Tk()
    pop.rowconfigure(1, weight=1)
    pop.columnconfigure([0, 1, 2], minsize=50, weight=1)
    pop.title("Oscilador")
    osc_GUI.cria_janela(pop)


def janela_mos():
    mos_GUI.cria_janela(janela)

menup = Menu(menubar)
menup.add_command(label="Mosfet",command=janela_mos)
menup.add_command(label="Oscilador",command=janela_osc)
menubar.add_cascade(label="Selecionar", menu=menup)



janela.config(menu=menubar)
janela.mainloop()


