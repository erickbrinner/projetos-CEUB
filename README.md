# 🎓 Repositório de Projetos Acadêmicos

Este repositório contém os projetos e trabalhos desenvolvidos durante a graduação em Análise e Desenvolvimento de Sistemas.

O objetivo é centralizar o código, as soluções e as aplicações práticas dos conceitos aprendidos em diversas disciplinas.

---

## 📚 Projetos da Disciplina: Programação Orientada a Objetos (POO)

Aqui está o detalhamento do projeto de gerenciamento hoteleiro:

### 🏨 Sistema Hotel - Gerenciamento de Reservas

| Detalhe | Informação |
| :--- | :--- |
| **Disciplina** | Programação Orientada a Objetos (POO) |
| **Objetivo** | Desenvolver um sistema para gerenciamento de reservas de quartos, simulando a operação de uma empresa hoteleira. |
| **Conceitos Aplicados** | **Herança** (`Pessoa` -> `Funcionario`, `Hospede`), **Encapsulamento**, **Composição** e Estruturas de Dados. |
| **Classes Implementadas** | `Pessoa`, `Funcionario`, `Hospede`, `Hotel`, `Quarto`, `Reserva`. |
| **Ponto Principal** | Implementação das relações *um-para-muitos* e *muitos-para-muitos* definidas no Diagrama UML. |


#### 📊 Arquitetura do Sistema (Diagrama de Classes UML)

A solução foi desenvolvida seguindo rigorosamente a arquitetura abaixo, construída para demonstrar a aplicação de herança e composição.

```mermaid
classDiagram
    direction LR

    class Pessoa{
        -int _id
        -str _nome
        -str _e_mail
        +get_id()
        +get_nome()
        +get_email()
    }
    class Funcionario{
        +add_quarto(hotel, quarto)
        +remover_quarto(hotel, quarto)
        +registrar_hospede(hotel, hospede)
        +cancelar_reserva(hotel, reserva)
    }
    class Hospede{
        -list _reservas
        +fazer_reserva(reserva)
        +cancelar_reserva(reserva)
        +consultar_reservas()
    }
    class Hotel{
        -list _quartos
        -list _hospedes
        -list _reservas
        +add_quarto(quarto)
        +remover_quarto(quarto)
        +registrar_hospede(hospede)
        +cancelar_reserva(reserva)
    }
    class Quarto{
        -int _numero
        -str _tipo
        -bool _disponivel
        +reservar()
        +liberar()
        +estaDisponivel()
    }
    class Reserva{
        -Hospede _hospede
        -Quarto _quarto
    }

    Pessoa <|-- Funcionario
    Pessoa <|-- Hospede

    Funcionario --> Hotel : gerencia
    Hospede --> Hotel : utiliza

    Hotel "1" *-- "*" Quarto : possui
    Hotel "1" *-- "*" Reserva : gerencia

    Reserva --> Hospede : feita_por
    Reserva --> Quarto : aloca

    Funcionario --> Quarto : opera.



#### 💻 Como Executar

O projeto principal que instancia as classes e aciona o fluxo de trabalho do hotel (criação de quartos, registro de hóspedes, realização de reservas, etc.) está no arquivo `main.py`.

1.  Clone este repositório.
2.  Navegue até o diretório do projeto (`/sistema_hotel/`).
3.  Execute o arquivo principal:
    ```bash
    python main.py
    ```


