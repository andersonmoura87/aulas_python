lista_de_nomes = []

print("-"*15)
print("Lista de Chamada")
print("_"*15)

num = 0

while num < 5:
    num += 1
    nome = input("Digite o seu nome: ")
    lista_de_nomes.append(nome)


print(lista_de_nomes)
print(lista_de_nomes[3])