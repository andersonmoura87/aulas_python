#Tabuada

num = int(input("Qual tabudada você quer saber? "))
print("-"*15)
print("TABUADA")
print("-"*15)

num1 = 0

while num1 < 10:
    num1 += 1
    resultado = num * num1
    print("{} X {} = {}".format(num, num1, resultado))
    
print("-"*15)
