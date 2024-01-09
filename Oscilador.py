import numpy as np
import math
import matplotlib.pyplot as plt
import mpl_interactions.ipyplot as iplt
from MOSFET import MOSFET 

class OSCILADOR: 
    C = 0 
    N = 0
    VDD = 0
    I= 0

    def __init__(self,I,C,N,VDD):
        self.I = I
        self.C = C
        self.N = N
        self.VDD = VDD
    

    def frequencia(self,osc):
        f = (osc.I)/(osc.N*osc.C*osc.VDD)
        return f

    def grafico(self,osc):
        amplitude =  osc.VDD
        f = osc.frequencia(osc)
        tempo = np.linspace(0, 100e-6, 1000)  # Tempo de 0 a 1 microssegundo com 1000 pontos

        # Criando a onda senoidal
        onda = amplitude * np.sin(2 * np.pi * f * tempo)
        onda_quadrada = amplitude * np.sign(np.sin(2 * np.pi * f * tempo))

        # Plotando a onda senoidal
        plt.figure(1)
        plt.plot(tempo, onda)
        plt.title('Onda Senoidal')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.legend()

        # Plotando a onda quadrada
        plt.figure(2)
        plt.plot(tempo, onda_quadrada)
        plt.title('Onda Quadrada')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.legend()

        plt.show()
    
