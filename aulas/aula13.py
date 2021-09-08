# Bibliotecas no Python

from random import randint

numero_aleatorio = randint(1, 10)

contador = 0

while True:
    contador += 1

    if contador < 4:
        tentativa = int(input("Digite um numero de 1 a 10: "))

        if tentativa == numero_aleatorio:
            print("Parabéns, você acentou | tentativa: "+str(contador))
            exit()

        elif numero_aleatorio > tentativa:
            print("O numero é maior! Tente novamente!")
        
        elif numero_aleatorio < tentativa:
            print("O numero é menor! Tente novamente!")
    
    else:
        break

print("Você perdeu | o numero era: "+str(numero_aleatorio))
