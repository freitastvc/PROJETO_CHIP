import numpy as np
import math
import matplotlib.pyplot as plt
import mpl_interactions.ipyplot as iplt

# Classe de modelo do MOSFET
class MOSFET:
    V_G = 0       
    V_S = 0       
    V_D = 0       
    V_GS = V_G - V_S
    V_DS = V_D - V_S
    V_GD = V_G - V_D 
    I_D = 0      

    V_TH = 0.7     
    UO = 350          
    T_ox = 9e-7  
    K_ox = 0
    C_ox = K_ox* 8.85e-14/ T_ox      
    L = 0.5                        
    W = 50     


    def __init__(self, V_G, V_S, V_D, V_TH, U0, T_ox, K_ox, W, L):
        self.V_G = V_G
        self.V_S = V_S
        self.V_D = V_D
        self.V_TH = V_TH
        self.UO = U0
        self.T_ox = T_ox
        self.K_ox = K_ox
        self.C_ox = (K_ox * 8.85e-14 ) / T_ox
        self.W = W
        self.L = L
        self.V_DS = V_D - V_S
        self.V_GS = V_G - V_S
    
                       
#Objeto para modelo NMOS    
NMOS = MOSFET(3.3,0,3.3,0.7,350,9e-9,3.9,2e-6,350e-6) 
 
# ------------------- Tensão de limiar --------------------------------------------------------------------
def Tensao_Limiar(MOS,V_B,NA,NI):  

    V_SB = MOS.V_S - V_B     
    fermi = MOS.V_TH * math.ln(NA/NI)
    GAMMA = (math.sqrt(2*NA*1.04e-12*1,602e-19)/MOS.C_ox)

    V_T = MOS.V_TH + GAMMA((math.sqrt(V_SB + abs(2*fermi))) - math.sqrt(abs(2*fermi)))
    return V_T

# ------------------- Pontencial de contato da junção PN --------------------------------------------------
def PHI_zero(MOS): 

    NA,ND,NI = 0

    phi0 = MOS.V_TH - math.ln(NA*ND/NI**2)
    return phi0
     
# ------------------- Largura de depleção delta L ----------------------------------------------------------
def Largura_deplecao(MOS): 

    NA = 0
    phi0 = PHI_zero(MOS)

    deltaL =  (math.sqrt((2*1.04e-12)/(NA*1,602e-19)) * math.sqrt(MOS.V_DS -(MOS.V_DS - MOS.V_TH) + phi0))
    return deltaL
     
# ------------------- Modulação de canal -------------------------------------------------------------------
def Modulação_canal(MOS): 
     
    NA = 0
    phi0 = PHI_zero(MOS)

    LAMBDA = (math.sqrt((2*1.04e-12)/(NA*1,602e-19))/(2*MOS.L*math.sqrt(MOS.V_DS -(MOS.V_DS - MOS.V_TH) + phi0)))
    return LAMBDA

# ------------------- Calculo para corrente de Dreno  -----------------------------------------------------
def Corrente_corte(MOS):
        MOS.I_D = 0
        return(MOS.I_D)
    
   
def Corrente_triodo(MOS):
    MOS.I_D = MOS.UO*MOS.C_ox*(MOS.W/MOS.L)*((MOS.V_GS-MOS.V_TH)*MOS.V_DS-MOS.V_DS**2/2)
    return MOS.I_D
    

def Corrente_sat(MOS):
    MOS.I_D = ((MOS.UO*MOS.C_ox*(MOS.W/MOS.L)*(MOS.V_GS-MOS.V_TH)**2))/2
    return MOS.I_D

# ------------------- Calculo para corrente de Dreno com Modulação de canal -----------------------------------
def Corrente_modulacaotriodo(MOS):

    LAMBDAe = 0.1

    MOS.I_D = MOS.UO*MOS.C_ox*(MOS.W/MOS.L)*((MOS.V_GS-MOS.V_TH)*MOS.V_DS-MOS.V_DS**2/2)*(1 + LAMBDAe*MOS.V_DS)
    return MOS.I_D

def Corrente_modulacaosat(MOS):

    LAMBDAe = 0.1

    MOS.I_D = (0.5*(MOS.UO*MOS.C_ox*(MOS.W/MOS.L)*(MOS.V_GS-MOS.V_TH)**2))*(1 + LAMBDAe*MOS.V_DS)
    return MOS.I_D

# ------------------- Trancondutância em Saturação --------------------------------------------------------------
def transcondutancia_sat(MOS):
    gm = math.sqrt(2*MOS.UO*MOS.C_ox*(MOS.W/MOS.L)*MOS.I_D)
    return gm

# ------------------- Função para plotar os gráficos --------------------------------------------------------------
def grafico(MOS):


    #Variaçao de Vds de 0 até 3.3
    Vds_list = np.arange(0,3.3,0.1)
    
    #Variaçao de Vgs de 0 até 3.3
    Vgs_list = np.arange(0,3.3,0.1)

    #Diferentes valores de Vg para plotar no gráfico
    vg =[0.5,1,1.5,2.0,2.5,3]

    #Gráfico de Corrente por tensão Vds
    for MOS.V_GS in vg: #Plota o gŕafico para os diferentes valores de Vg
        id_list = [Corrente_triodo(MOS)if (MOS.V_DS < MOS.V_GS - MOS.V_TH) else Corrente_sat(MOS) for MOS.V_DS in Vds_list] #Calcula a corrente para trido e saturação para Vds de 0 até 3.3
        plt.figure(1) #Cria uma janela para gráfico
        plt.plot(Vds_list,id_list)# Faz a plotagem das curvas
        plt.title("Vds x ID")
        plt.xlabel("Tensão Vds [V]")
        plt.ylabel("Corrente [A]")

    #Gráfico Corrente por tensão Vds com Modulação de Canal
    for MOS.V_GS in vg: #Plota o gŕafico para os diferentes valores de Vg
        id_modulacao = [Corrente_modulacaotriodo(MOS)if (MOS.V_DS < MOS.V_GS - MOS.V_TH) else Corrente_modulacaosat(MOS) for MOS.V_DS in Vds_list] #Calcula a corrente para trido e saturação para Vds de 0 até 3.3 considerando o efeito de modulação de canal
        plt.figure(2) #Cria uma janela para gráfico
        plt.plot(Vds_list,id_modulacao) # Faz a plotagem das curvas
        plt.title("Vds x ID com modulação de canal")
        plt.xlabel("Tensão Vds [V]")
        plt.ylabel("Corrente [A]")

    #Gráfico da transcondutância pela Corrente
    id_trans = [Corrente_triodo(MOS)if (MOS.V_DS < MOS.V_GS - MOS.V_TH) else Corrente_sat(MOS) for MOS.V_DS in Vds_list] #Define o valor da corrente 
    gm_list = [transcondutancia_sat(MOS)for MOS.I_D in id_trans] #Define o valor da Trancondutância para os diferentes valores de corrente
    plt.figure(3)#Cria uma janela para gráfico
    plt.plot(id_trans,gm_list)# Faz a plotagem das curvas
    plt.title("gm x ID")
    plt.xlabel("Corrente [A]")
    plt.ylabel("Transcondutância")

    #Gráfio da Corrente pela tensão Vgs
    id_liss = [Corrente_corte(MOS)if (MOS.V_GS < MOS.V_TH) else Corrente_triodo(MOS)if (MOS.V_DS < MOS.V_GS - MOS.V_TH) else Corrente_sat(MOS) for MOS.V_GS in Vgs_list] #Calcula a corrente para trido e saturação para Vgs de 0 até 3.3
    plt.figure(4) #Cria uma janela para gráfico
    plt.plot(Vgs_list,id_liss)# Faz a plotagem das curvas
    plt.title("Vgs x ID")
    plt.xlabel("Tensão Vgs [V]")
    plt.ylabel("Corrente [A]")

    plt.show()


grafico(NMOS)