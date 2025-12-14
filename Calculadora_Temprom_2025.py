import tkinter as tk
from tkinter import messagebox

# Función promedio
def promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Obtener datos y mostrar promedio
def calcular():
    try:
        temperaturas = []
        for entrada in entradas:
            temperaturas.append(float(entrada.get()))

        resultado = promedio(temperaturas)
        etiqueta_resultado.config(
            text=f"Promedio semanal: {resultado:.2f} °C"
        )

    except ValueError:
        messagebox.showerror("Error", "Ingrese solo números")

# INTERFAZ GRÁFICA
ventana = tk.Tk()
ventana.title("Promedio Semanal")
ventana.geometry("300x380")

tk.Label(ventana, text="Ingrese las temperaturas de la semana",
         font=("Arial", 10, "bold")).pack(pady=10)

frame = tk.Frame(ventana)
frame.pack()

entradas = []
for i in range(7):
    tk.Label(frame, text=f"Día {i+1}:").grid(row=i, column=0)
    e = tk.Entry(frame, width=8)
    e.grid(row=i, column=1)
    entradas.append(e)

tk.Button(ventana, text="Calcular Promedio", command=calcular).pack(pady=15)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 11, "bold"))
etiqueta_resultado.pack()

ventana.mainloop()
