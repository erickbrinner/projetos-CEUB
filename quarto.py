class Quarto:
    def __init__(self, numero, tipo):
        self.__numero = numero
        self.__tipo = tipo
        self.__disponivel = True
    
    def reservar_quarto(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False
        
    def liberar_quarto(self):
        self.__disponivel = True
        
    def estaDisponivel(self):
        return self.__disponivel
    
    def get_numero(self):
        return self.__numero