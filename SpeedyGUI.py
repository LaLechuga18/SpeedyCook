import tkinter as tk
from PIL import Image, ImageTk

# Función para redimensionar la imagen
def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height))

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
image_path = "logo.png"  # Ruta de tu imagen
original_image = Image.open(image_path)
resized_image = resize_image(original_image, 250, 250)  # Redimensionar la imagen

photo = ImageTk.PhotoImage(resized_image)

label_image = tk.Label(frame_left, image=photo, bg="#41C9E2")
label_image.image = photo  # Mantener una referencia a la imagen para evitar que se elimine de la memoria
label_image.pack(pady=150, padx=100)  # pady y padx para añadir un poco de espacio alrededor de la imagen

label_text = tk.Label(frame_left, text="SpeedyCook", bg="#41C9E2", fg="white", font=("Segoe UI Semibold", 40))
label_text.pack()

label_text2 = tk.Label(frame_right, text="Bienvenido! \n\n Seleccione una imagen para comenzar", bg="white", font=("Segoe UI Semibold", 30), pady=250)
label_text2.pack()

button = tk.Button(frame_right, text="Seleccionar", font=("Segoe UI Semibold", 20), bg="#41C9E2")
button.pack()

root.mainloop()
