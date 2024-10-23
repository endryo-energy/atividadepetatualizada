class Animal:
    def __init__(self, nome, idade, especie):
        self._nome = nome
        self._idade = idade
        self._especie = especie

    def calcular_preco_servico(self, servico):
        pass


class Cachorro(Animal):
    def calcular_preco_servico(self, servico):
        if servico == "banho":
            return 50 + 50  # Adicionando R$50
        elif servico == "tosa":
            return 80 + 50  # Adicionando R$50
        elif servico == "medico":
            return 100 + 50  # Adicionando R$50
        return 0


class Gato(Animal):
    def calcular_preco_servico(self, servico):
        if servico == "banho":
            return 40 + 40  # Adicionando R$40
        elif servico == "tosa":
            return 70 + 40  # Adicionando R$40
        elif servico == "medico":
            return 90 + 40  # Adicionando R$40
        return 0


class Passaro(Animal):
    def calcular_preco_servico(self, servico):
        if servico == "banho":
            return 30 + 30  # Adicionando R$30
        elif servico == "tosa":
            return 20 + 30  # Adicionando R$30
        elif servico == "medico":
            return 50 + 30  # Adicionando R$30
        return 0


animais = []


def cadastrar_animal():
    nome = input("Digite o nome do animal: ")
    idade = input("Digite a idade do animal: ")
    especie = input("Digite a espécie do animal (cachorro, gato, passaro): ").lower()

    if especie == "cachorro":
        animal = Cachorro(nome, idade, especie)
    elif especie == "gato":
        animal = Gato(nome, idade, especie)
    elif especie == "passaro":
        animal = Passaro(nome, idade, especie)
    else:
        print("Espécie inválida! Tente novamente.")
        return

    animais.append(animal)
    print(f"{nome} cadastrado com sucesso!")


def consultar_animal():
    nome = input("Digite o nome do animal que deseja consultar: ")
    for animal in animais:
        if animal._nome == nome:
            print(f"Nome: {animal._nome}, Idade: {animal._idade}, Espécie: {animal._especie}")
            return
    print("Animal não encontrado!")


def calcular_preco_servico():
    nome = input("Digite o nome do animal para calcular o preço do serviço: ")
    servico = input("Digite o tipo de serviço (banho, tosa, medico): ").lower()
    for animal in animais:
        if animal._nome == nome:
            preco = animal.calcular_preco_servico(servico)
            if preco > 0:
                print(f"O preço do serviço {servico} para {animal._nome} é R${preco:.2f}")
            else:
                print("Serviço inválido! Tente novamente.")
            return
    print("Animal não encontrado!")


def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar animal")
        print("2. Consultar animal")
        print("3. Calcular preço de serviço")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_animal()
        elif opcao == '2':
            consultar_animal()
        elif opcao == '3':
            calcular_preco_servico()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Iniciar o menu
menu()
