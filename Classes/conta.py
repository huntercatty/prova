from datetime import datetime
import datetime as dt
class Conta:
    def __init__(self,n_conta:str ="",dataleitura:datetime=datetime.now(),nleitura:str="", valor:float=0,kwgasto:int=0) -> None:
        self.__n_conta = n_conta
        self.__dataleitura = dataleitura
        self.__n_leitura=nleitura
        self.__valor_pagar = valor
        self.__data_pgto = dt.timedelta(days=20)+dataleitura
        self.__kwGasto = kwgasto

    def getDataLeitura(self):
            return self.__dataleitura.strftime(" %d %m %Y ")
    def getKwGasto(self):
            return self.__kwGasto
    def getValorPagar(self):
            return self.__valor_pagar
    def getDadosConta(self):
            pass

    def toString(self):
            return f"numero da conta: {self.__n_conta}\n data da conta: {self.__dataleitura}\n" +\
            f"numero de leitura: {self.__n_leitura}\n valor a pagar {self.__valor_pagar} \n kwgasto :{self.__kwgasto}\n "