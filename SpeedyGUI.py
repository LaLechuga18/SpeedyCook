import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog

# Función para redimensionar la imagen
def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height))


def mostrar(dato1, dato2):
    # Esta función se llama cuando se hace clic en el botón
    valor_dato1 = dato1.get()
    valor_dato2 = dato2.get()
    messagebox.showinfo("Valores", f"Dato 1: {valor_dato1} \n Dato2: {valor_dato2}")

def datos_ingredientes():
    root.destroy()
    window = tk.Tk()
    window.geometry("450x200+500+250")
    window.title("Ingredientes")
    window.configure(bg="#ACE2E1")


    # Crear etiqueta y campo de entrada para el primer dato
    msg = tk.Label(window, text="Ingrese el numero de ingredientes disponibles", bg="#ACE2E1", font=("Segoe UI Semibold", 14))
    msg.pack()
    dato1 = tk.Entry(window)
    dato1.pack()

    # Crear etiqueta y campo de entrada para el segundo dato
    msg2 = tk.Label(window, text="Ingrese el tipo de comida", bg="#ACE2E1", font=("Segoe UI Semibold", 14))
    msg2.pack()
    dato2 = tk.Entry(window)
    dato2.pack()

    # Crear un botón para mostrar los datos ingresados
    btn = tk.Button(window, text="Mostrar", command=lambda: mostrar(dato1, dato2), font=("Segoe UI Semibold", 14))
    btn.pack(pady=30)

    btn = tk.Button(window, text="Cerrar", command=window.destroy, font=("Segoe UI Semibold", 14))
    btn.pack()

    window.mainloop()




# Crear la ventana principal
root = tk.Tk()
root.geometry("400x300+500+250")
root.title("SpeedyCook")

# Dividir la ventana en dos marcos
frame_left = tk.Frame(root, bg="#41C9E2", width=200, height=300)
frame_right = tk.Frame(root, bg="white", width=200, height=300)

# Colocar los marcos en la ventana
frame_left.pack(side="left", fill="both", expand=True)
frame_right.pack(side="right", fill="both", expand=True)

# Agregar imagen al lado izquierdo
image_path = "logo.png"  # TENER DESCARGADA LA IMAGEN EN LA MISMA CARPETA PARA QUE FUNCIONE 
original_image = Image.open(image_path)
resized_image = resize_image(original_image, 250, 250)  # Redimensionar la imagen

photo = ImageTk.PhotoImage(resized_image)

label_image = tk.Label(frame_left, image=photo, bg="#41C9E2")
label_image.image = photo  # Mantener una referencia a la imagen para evitar que se elimine de la memoria
label_image.pack(pady=120, padx=100)  # pady y padx para añadir un poco de espacio alrededor de la imagen

label_text = tk.Label(frame_left, text="SpeedyCook", bg="#41C9E2", fg="white", font=("Segoe UI Semibold", 40))
label_text.pack()
label_textm = tk.Label(frame_left, text="Sebastian C.\n Jair R. \n Alan", bg="#41C9E2", fg="white", font=("Segoe UI Semibold", 20))
label_textm.pack()

label_text2 = tk.Label(frame_right, text="Bienvenido! \n\n Presiona el boton para empezar a generar las recetas", bg="white", font=("Segoe UI Semibold", 30), pady=250)
label_text2.pack()

button = tk.Button(frame_right, text="Empezar", font=("Segoe UI Semibold", 20), bg="#41C9E2", command=datos_ingredientes)
button.pack()


root.mainloop()
