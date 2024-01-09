from tkinter import *
from PIL import Image, ImageTk
from Oscilador import OSCILADOR

n = 3

def cria_janela(pop):

    def aumentar():
        global n
        n = max(n + 2, 3)
        rotulo_valor.config(text=str(n))

    def diminuir():
        global n
        n = max(n - 2, 3)
        rotulo_valor.config(text=str(n))

    def plotar_grafico():

        valor_i = float(i.get()) if i.get() else 1.0
        valor_vdd = float(vdd.get()) if vdd.get() else 1.0
        valor_c = float(c.get()) if c.get() else 1.0

        osc.I = valor_i
        osc.VDD = valor_vdd  # Obtém o valor de VDD no momento do clique do botão
        osc.N = n  # Define o valor de N
        osc.C = valor_c
        osc.grafico(osc)  # Chama a função de plotagem do gráfico


    osc = OSCILADOR(0,0,0,0)
        
    #Input Corrente
    label_i = Label(pop, text="Corrente:")
    label_i.grid(row=1, column=0, sticky=W)
    i = Entry(pop, width=60)
    i.grid(row=2, column=0, columnspan=3, padx=10, pady=10,sticky=W)


    #Input VDD
    label_vdd = Label(pop, text="VDD:")
    label_vdd.grid(row=3, column=0, sticky=W)
    vdd = Entry(pop, width=60)
    vdd.grid(row=4, column=0, columnspan=3, padx=10, pady=10,sticky=W)


    #Input Capacitância
    label_c = Label(pop, text="Capacitância:")
    label_c.grid(row=5, column=0, sticky=W)
    c = Entry(pop, width=60)
    c.grid(row=6, column=0, columnspan=3, padx=10, pady=10,sticky=W)


    #Input N
    label_n = Label(pop, text="N:")
    label_n.grid(row=7, column=0, sticky=W)
    rotulo_valor = Label(pop, text=str(n), font=("Arial", 18))
    rotulo_valor.grid(row=8, column=1, padx=10, pady=10)
    botao_aumentar = Button(pop, text="+", command=aumentar)
    botao_aumentar.grid(row=8, column=2, padx=10, pady=10,sticky=E)
    botao_diminuir = Button(pop, text="-", command=diminuir)
    botao_diminuir.grid(row=8, column=0, padx=10, pady=10,sticky=W)


    graficos = Button(pop, text="Plotar Gráfico", width=50, height=5,command=plotar_grafico)
    graficos.grid(row=9, column=0, columnspan=3, padx=10, pady=10)

    