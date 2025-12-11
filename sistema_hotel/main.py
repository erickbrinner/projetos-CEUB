from pessoa import Pessoa
from funcionarios import Funcionario
from hospede import Hospede
from quarto import Quarto
from reserva import Reserva
from hotel import Hotel

def main():

    hotel = Hotel()
    
    func = Funcionario(1, "Erick", "erick@gmail.com")
    print("Funcionario criado:")
    print("ID:", func.get_id())
    print("Nome:", func.get_nome())
    print("E-mail:", func.get_email(), "\n")
    
    quarto101 = Quarto(101, "Standard")
    quarto802 = Quarto(802, "Luxo")
    quarto1003 = Quarto(1003, "Suíte")
    print("Quartos criados:")
    if quarto101.estaDisponivel == True:
        print(f"Quarto {quarto101.get_numero()} disponível!")
    if quarto802.estaDisponivel == True:
        print(f"Quarto {quarto802.get_numero()} disponível!")
    if quarto1003.estaDisponivel == True:
        print(f"Quarto {quarto1003.get_numero()} disponível!")    
    
    print("Adicionando quartos ao hotel...\n")
    func.add_quarto(hotel, quarto101)
    func.add_quarto(hotel, quarto802)
    func.add_quarto(hotel, quarto1003)
    
    hospede1 = Hospede(10, "Anna", "anna@gmail.com")
    print("Hóspede criado:")
    print("ID:", hospede1.get_id())
    print("Nome:", hospede1.get_nome())
    print("E-mail:", hospede1.get_email())
    
    print("Registrando hóspede no hotel...\n")
    func.registrar_hospede(hotel, hospede1)
    
    reserva1 = Reserva(quarto101, hospede1)
    print(f"Tentando reservar o quarto {quarto101.get_numero()} para o hospede {hospede1.get_nome()}...")
    
    sucesso = hotel.fazer_reserva(reserva1)
    if sucesso:
        print("Reserva realizada com sucesso\n")
    else:
        print("Não foi possível realizar a reserva\n")
        
    print(f"Verificando disponibilidade do quarto {quarto101.get_numero()}...")
    
    if quarto101.estaDisponivel == True:
        print(f"Quarto {quarto101.get_numero()} está disponível!\n")
    else:
        print(f"Quarto {quarto101.get_numero()} está reservado.\n")       
                
main()
