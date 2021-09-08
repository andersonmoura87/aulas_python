# Fazer uma função que perguta para a pessoa:
#qual a cor do carro?
# se o carro for vermelho é a cro do amor
# se o carro for amarelo é a cor da amizade
# se o carro for verde cor do ciumes
# else: seu carro tem uma cor bonita!

def cor_do_carro():
    cor = input("Digite a cor de um carro: ")

    if cor == "vermelho":
        print("Cor do amor")

    elif cor == "amarelo":
        print("Cor da amizade")

    elif cor == "verde":
        print("Cor da inveja")

    else:
        print("Seu carro tem uma cor bonita!")

cor_do_carro()