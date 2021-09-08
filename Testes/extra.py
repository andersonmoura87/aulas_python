"""

num1 = int(input("Número um: "))
num2 = int(input("Número dois: "))
num3 = int(input("Número três: "))

if num1 > num2 and num3:
    print ("Número um é o maior numero!")
elif num2 > num1 and num3:
    print ("Número dois é o maior numero")
elif num3 > num1 and num2:
    print ("Número três é o maior numero")

maior = 5
menor = 10

print ('Maior:  %d ' %maior)
print ('Menor:  %d ' %menor)

"""
from tkinter import *

root = Tk()
root.geometry("500x400") 
a = Label(root, text ="Digite o seu email")
b = Button(root, text="ENTRAR")
e = Entry(root)
a.pack()
b.pack()
e.pack()

root.mainloop()

# Python tkinter hello world program
  
from tkinter import *

root = Tk()
root.geometry("500x400") 
a = Label(root, text ="Digite o seu email")
b = Button(root, text="ENTRAR")
e = Entry(root)
a.pack()
e.pack()
b.pack()

root.mainloop()
