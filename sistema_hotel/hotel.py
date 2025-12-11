class Hotel:
    def __init__(self):
        self.__quartos = []
        self.__hospedes = []
        self.__reservas = []
        
    def add_quarto(self, quarto):
        self.__quartos.append(quarto)
    
    def remover_quarto(self, quarto):
        if quarto in self.__quartos:
            self.__quartos.remove(quarto)
            
    def registrar_hospede(self, hospede):
        self.__hospedes.append(hospede)
    
    def fazer_reserva(self, reserva):
        if reserva._quarto.estaDisponivel():
            self.__reservas.append(reserva)
            reserva._hospede.fazer_reserva(reserva)
            return True
        return False
    
    def cancelar_reserva(self, reserva):
        if reserva in self.__reservas:
            self.__reservas.remove(reserva)
            reserva._quarto.liberar()