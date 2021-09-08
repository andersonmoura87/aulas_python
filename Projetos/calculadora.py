def mais(num1, num2):
    result = num1 + num2
    print("O resultado é: " +str(result))

def menos(num1, num2):
    result = num1 - num2
    print("O resultado é: " +str(result))

def vezes(num1, num2):
    result = num1 * num2
    print("O resultado é: " +str(result))

def dividir(num1, num2):
    result = num1 / num2
    print("O resultado é: " +str(result))

while True:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    conta = input("Qual operação você deseja fazer? ")

    if conta == "adição":
       mais(num1 , num2)
    
    elif conta == "subtração":
        menos(num1 , num2)
    
    elif conta == "multiplicação":
        vezes(num1 , num2)
    
    elif conta == "divisão":
        dividir(num1 , num2)

    else:
        print("Operação invalida")

        
