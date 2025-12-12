# Projetos CEUB
# 🏨 Sistema Hotel - Gerenciamento de Reservas

## 🌟 Visão Geral do Projeto

Este projeto foi desenvolvido como parte da sistematização da matéria de **Programação Orientada a Objetos (POO)**. O objetivo principal foi criar uma solução robusta e modular para atender às necessidades de uma empresa do ramo hoteleiro, focada no **gerenciamento eficiente de reservas de quartos**.

A solução foi concebida e implementada seguindo rigorosamente os princípios de POO, utilizando herança, encapsulamento e composição para garantir um código limpo, manutenível e escalável.

## 📐 Diagrama UML do Projeto

A arquitetura da solução foi definida com base no seguinte Diagrama de Classes UML, que estabelece as entidades, seus atributos, métodos e os relacionamentos entre elas:


## 🚀 Tecnologias e Conceitos de POO Aplicados

O projeto foi desenvolvido em Python, aplicando os seguintes pilares da Programação Orientada a Objetos:

### 1. Herança (Inheritance)

* A classe base **`Pessoa`** (abstrata, idealmente) serve como superclasse para **`Funcionario`** e **`Hospede`**.
* **Vantagem:** Reutilização de código, garantindo que atributos comuns como `_id`, `_nome` e `_e_mail` sejam definidos uma única vez.

### 2. Encapsulamento (Encapsulation)
* Todos os atributos críticos (ex: `_id`, `_numero`, `_reservas`) são protegidos ou privados (indicados pelo *leading underscore* `_`).
* O acesso e a modificação desses dados internos são controlados por métodos públicos (Getters e Setters, como `get_id()` e `get_nome()`), garantindo a integridade do estado do objeto.

### 3. Composição (Composition/Aggregation)
* A classe **`Hotel`** mantém coleções de objetos de outras classes (**`Quarto`**, **`Hospede`** e **`Reserva`**), utilizando estruturas de dados.
* **`Reserva`** é composta por um objeto **`Hospede`** e um objeto **`Quarto`**, definindo o vínculo essencial de uma reserva.

### 4. Estruturas de Dados
* Arrays ou Listas (`[]` no diagrama) são utilizadas dentro das classes **`Hotel`** (`_quartos`, `_hospedes`, `_reservas`) e **`Hospede`** (`_reservas`) para gerenciar coleções de objetos de forma eficiente.

## 🧩 Classes Implementadas

As seguintes classes foram implementadas para modelar o domínio hoteleiro:

| Classe | Descrição | Atributos Chave | Métodos Principais |
| :--- | :--- | :--- | :--- |
| **Pessoa** | Classe base para indivíduos. | `_id`, `_nome`, `_e_mail` | `get_id()`, `get_nome()` |
| **Funcionario** | Representa um funcionário do hotel. | (Herda de Pessoa) | `add_quarto()`, `registrar_hospede()` |
| **Hospede** | Representa um cliente com histórico de reservas. | `_reservas: []` | `fazer_reserva()`, `cancelar_reserva()` |
| **Quarto** | Representa uma unidade de acomodação. | `_numero`, `_tipo`, `_disponivel: bool` | `reservar()`, `liberar()`, `estaDisponivel()` |
| **Reserva** | Detalhes de uma reserva específica. | `_hospede: Hospede`, `_quarto: Quarto` | (Classe de dados de relacionamento) |
| **Hotel** | Classe principal de gerenciamento. | `_quartos: []`, `_hospedes: []`, `_reservas: []` | `add_quarto()`, `registrar_hospede()`, `cancelar_reserva()` |

## ⚙️ Execução do Projeto

O projeto pode ser executado através do arquivo principal:

1.  **Instanciação:** O arquivo `main.py` é responsável por instanciar as classes (`Hotel`, `Funcionario`, `Hospede`, `Quarto`).
2.  **Ação dos Métodos:** Em seguida, `main.py` aciona os métodos da aplicação para simular o fluxo de trabalho diário de um hotel:
    * Adicionar quartos.
    * Registrar um hóspede.
    * Fazer uma nova reserva.
    * Consultar a disponibilidade do quarto.
    * Cancelar uma reserva.
