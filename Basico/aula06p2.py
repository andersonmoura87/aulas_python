# revisando listas

emails = []

email1 = input("Digite seu E-mail: ")
email2 = input("Digite seu E-mail: ")

emails.append(email1)
emails.append(email2)

print(emails[0])
emails.remove(email2)
print(emails)

