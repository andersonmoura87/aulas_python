# criar uma lista vazia
# criar um loop while para pedir ao menos 5 nomes
# cada nome digitado ser inserido na lista - append
# Criar um loop for para exibir cada valor da lista

estados = []
#while
while len(estados) < 5:
    estado = input("Digite o seu estado: ")
    estados.append(estado)

for item in estados:
    print(item)
