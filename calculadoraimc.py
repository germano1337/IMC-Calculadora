import tkinter as tk
from tkinter import messagebox

calculadora = tk.Tk()
calculadora.title("Calculadora IMC")
calculadora.geometry("321x333")

def botaoCalcularClicado():
    if peso.get() != "" and altura.get() != "":
        p = round(2)(peso.get())
        a = round(2)(altura.get())
        imc = p / a **2 
        messagebox.showinfo("Resultado", "IMC: " + str(imc))

def botaoSairClicado():
    calculadora.quit()        
        
peso = tk.StringVar()
altura = tk.StringVar()

rotuloPeso = tk.Label(text="Peso: ", width= 25 , anchor=tk.W)
textoPeso = tk.Entry(textvariable = peso)
rotuloAltura = tk.Label(text="Altura: ", width= 25 , anchor=tk.W)
textoAltura = tk.Entry(textvariable = altura)

botaoCalcular = tk.Button(calculadora, text="Calcular", command=botaoCalcularClicado)
botaoSair = tk.Button(calculadora, text= "Sair", command= botaoSairClicado )


rotuloPeso.grid(row = 0, column =0)
textoPeso.grid(row = 0, column=1)
rotuloAltura.grid(row = 1, column=0)    
textoAltura.grid(row = 1, column=1)

botaoCalcular.grid(row = 2, column=0, columnspan=2)   
botaoSair.grid(row= 3, column = 0, columnspan= 3)


calculadora.mainloop()