class Candidato:
    def __init__(self, numero, nome):
        self.__numero = numero
        self.__nome = nome
        self.__votos = 0
        
    def getDados(self):
        return self.__numero, self.__nome, self.__votos
    
    def getVotos(self):
        return self.__votos
    
    def addVoto(self):
        self.__votos += 1
    
    def getNome(self):
        return self.__nome
    
    def getNumero(self):
        return self.__numero