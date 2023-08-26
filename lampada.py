class Lampada():

    #atributos (caracteristicas)
    __potencia = 0
    __tensao = 0
    __cor = "branca"
    __estado = False

    #construtor
    def __init__(self, cor, potencia, tensao):
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao

    #metodos (funcionalidades)
    
    @property
    def potencia(self):
        return self.__potencia
    
    @potencia.setter
    def potencia(self, nova_potencia):
        if nova_potencia > 0:
            self.__potencia = nova_potencia
        else:
            raise TypeError("Nao pode")



    
    def get_tensao(self):
        return self.__tensao 

    def ligar (self):
        self.__estado = True

    def desligar(self):
        pass

    def iluminar(self):
        pass

    def aquecer(self):
        pass



