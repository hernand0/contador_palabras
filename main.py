import tkinter as tk
from tkinter import messagebox

def contar_palabras():
    texto = cuadro_texto.get("1.0", tk.END)  # Obtiene el texto del cuadro
    num_palabras = len(texto.split())  # Cuenta palabras
    num_caracteres = len(texto) - 1  # Cuenta caracteres, menos el último salto de línea
    num_espacios = texto.count(" ")  # Cuenta espacios
    num_lineas = texto.count("\n")  # Cuenta líneas
    
    resultado = f"Número de palabras: {num_palabras}\nNúmero de caracteres: {num_caracteres}\nNúmero de espacios: {num_espacios}\nNúmero de líneas: {num_lineas}"
    
    # Resultado en ventana emergente
    messagebox.showinfo("Resultado", resultado)

# Ventana
ventana = tk.Tk()
ventana.title("dH_ Contador de Palabras")

# Cuadro de texto
cuadro_texto = tk.Text(ventana, height=30, width=60)
cuadro_texto.pack(padx=10, pady=10)

# Botón
boton_contar = tk.Button(ventana, text="Contar", command=contar_palabras)
boton_contar.pack(pady=10)

# Ejecutar
ventana.mainloop()
