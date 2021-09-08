nomes_conhecidos = ["Anderson", "Nicolas"]

nome = input("Digite seu nome: ")

if (nome in nomes_conhecidos):   
    print("Ola bem vindo de volta {}".format(nome))

else:
    print("Ola {} é um prazer te conhecer".format(nome))
    nomes_conhecidos.append(nome)

nome = input("Digite seu nome: ")

if (nome in nomes_conhecidos):   
    print("Ola bem vindo de volta {}".format(nome))

else:
    print("Ola {} é um prazer te conhecer".format(nome))
    nomes_conhecidos.append(nome)
