# Criar um dicionario vazio
# capturar email e senha
# Adicione os dados no dicionario
# Pedir para o usuario digitar tudo 
# Criar uma condição que vai verificar se os valores estão corretos

# dicionario de usuarios 
users = {}

# informações de cadastro
email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ")

# salvando as informações de cadastro no dicionario
users[email] = senha

# capturando as informações de login
email_login = input("Digite seu e-mail: ")
senha_login = input("Digite sua senha: ")

# Verificar se o usario existe
if email_login in users and senha_login == users[email_login]:
    print("Login ok!")

else:
    print("Informações de login invalidas")