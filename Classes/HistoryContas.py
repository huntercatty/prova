
from .Conta import Conta

class HistoryContas:
    def __init__(self) -> None:
        self.__contas  = []#É uma lista de todas as contas
    def getMediaKw(self):
        media = 0
        for conta in self.__contas:
            media+=conta.getKwGasto()
        return media/len(self.__contas)

    def getValorMediaContas(self):
        media = 0
        for conta in self.__contas:
            media+=conta.getValorPagar()
        return f"{media/len(self.__contas):.2f}"
    
    def getMesMaiorConsumo(self):
        maior  =  self.__contas[0]
        for  conta  in  self.__contas:

            if maior.getKwGasto () <= conta.getKwGasto(): 
                maior = conta 
        return maior.getDataLeitura ()

    def getMesMenorConsumo(self):
          menor  =  self.__contas[0]
          for  conta  in  self.__contas:
            if menor.getKwGasto () >=  conta.getKwGasto(): 
                menor = conta 
          return menor.getDataLeitura ()


    def setConta(self,conta:Conta):
        self.__contas.append(conta)
        
    