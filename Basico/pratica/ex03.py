# simulação de alimentação de dados

nome = input("Digite o nome, ")
idade = input("Digite a idade, ")
casado = input("Você é casado, ")
tamanho = input("Digite o seu tamanho, ")

print(type(nome))
print(type(idade))
print(type(casado))
print(type(tamanho))
##### Errei ######

##### Explicação Correta #####
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
casado = bool(input("Você é casado: "))
tamanho = float(input("Digite o seu tamanho: "))

print(type(nome))
print(type(idade))
print(type(casado))
print(type(tamanho))

##### Explicações Extras do Prof. Nicolas #####
# print(test)
# teste = False # case-sensitive
