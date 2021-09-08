# tratamentos de erros

def somar_cinco():
    num = int(input("Digite um numero: "))
    print("{} + 5 = {}".format(num, num + 5))


while True:
    try:
        somar_cinco()

    except:
        print("Digite apenas numeros")

    finally:
        break

print("Chegou no fim")
