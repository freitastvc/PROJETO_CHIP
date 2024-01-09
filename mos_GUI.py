from tkinter import *
from PIL import Image, ImageTk
from MOSFET import MOSFET


def cria_janela(pop):

    MOS = MOSFET(0,0,0,0,0,1.0,0,0,0) 

    def inputs(): 
            
        def comandos():
            # Obtendo os valores inseridos nos campos de entrada
            MOS.V_G = float(vg.get()) if vg.get() else 0.0
            MOS.V_D = float(vd.get()) if vd.get() else 0.0
            MOS.V_S = float(vs.get()) if vs.get() else 0.0
            MOS.W = float(w.get()) if w.get() else 1.0e-6
            MOS.L= float(l.get()) if l.get() else 1.0e-6
            MOS.V_TH = float(vth.get()) if vth.get() else 0.0
            MOS.UO = float(u0.get()) if u0.get() else 0.0
            MOS.C_ox = float(cox.get()) if cox.get() else 0.0

            popupm.destroy()

        popupm = Toplevel()
        popupm.title("Especificações do Mosfet")

        #Input Vg
        label_vg = Label(popupm, text="Vg:")
        label_vg.grid(row=3, column=0, sticky=W)
        vg = Entry(popupm, width=30)
        vg.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        #Input Vd
        label_vd = Label(popupm, text="Vd:")
        label_vd.grid(row=5, column=0, sticky=W)
        vd = Entry(popupm, width=30)
        vd.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        #Input Vs
        label_vs = Label(popupm, text="Vs:")
        label_vs.grid(row=7, column=0, sticky=W)
        vs = Entry(popupm, width=30)
        vs.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        #Input W
        label_w = Label(popupm, text="W:")
        label_w.grid(row=9, column=0, sticky=W)
        w = Entry(popupm, width=30)
        w.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

        #Input L
        label_l = Label(popupm, text="L:")
        label_l.grid(row=11, column=0, sticky=W)
        l = Entry(popupm, width=30)
        l.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        #Input V_th
        label_vth = Label(popupm, text="Vth:")
        label_vth.grid(row=13, column=0, sticky=W)
        vth = Entry(popupm, width=30)
        vth.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

        #Input u0
        label_u0 = Label(popupm, text="U0:")
        label_u0.grid(row=15, column=0, sticky=W)
        u0 = Entry(popupm, width=30)
        u0.grid(row=16, column=0, columnspan=2, padx=10, pady=10)

        #Input cox
        label_cox = Label(popupm, text="Cox:")
        label_cox.grid(row=17, column=0, sticky=W)
        cox = Entry(popupm, width=30)
        cox.grid(row=18, column=0, columnspan=2, padx=10, pady=10)

        save = Button(popupm, text="Salvar", width=25, height=2, command=comandos)
        save.grid(row=19, column=0, padx=10, pady=10)

    def plotar_grafico():
        MOS.grafico(MOS)

    imagem_nmos = PhotoImage(file="nmos.png")
    imagem_pmos = PhotoImage(file="pmos.png")


    def nmos():
       botao_com_imagem.config(image= imagem_nmos)
        

    def pmos():
        botao_com_imagem.config(image= imagem_pmos)
       
    
    # Botão NMOS
    botao_nmos = Button(pop, text="NMOS", width=25, height=5,command=nmos)
    botao_nmos.grid(row=0, column=0, padx=10, pady=10)

    # Botão PMOS
    botao_pmos = Button(pop, text="PMOS", width=25, height=5,command=pmos)
    botao_pmos.grid(row=0, column=1, padx=10, pady=10)
  
  
    #label para manter a imagem de referenica de não sumir 
    label = Label(image=imagem_nmos)
    label.image = imagem_nmos # keep a reference!


    # Criando o botão com a imagem
    botao_com_imagem = Button(pop, image=imagem_nmos, width=500, height=500, command=inputs)
    botao_com_imagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    graficos = Button(pop, text="Plotar Curvas", width=50, height=5,command=plotar_grafico)
    graficos.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



