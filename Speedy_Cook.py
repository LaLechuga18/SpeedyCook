import os
import sys
import io
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import tkinter as tk
from tkinter import filedialog, Label, Button, messagebox
from PIL import Image, ImageTk
from googletrans import Translator
import requests


# Set encoding to utf-8 for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Optional: disable oneDNN custom operations messages
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

longitud, altura = 150, 150
modelo = 'D:/5 SEMESTRE/PROJECT Speedy Cook/modelo/modelo.h5'
pesos_modelo = 'D:/5 SEMESTRE/PROJECT Speedy Cook/modelo/pesos.weights.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

# Optional: compile the model if you need to evaluate or train it later
# cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

def predict(file):
    x = load_img(file, target_size=(longitud, altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = cnn.predict(x)
    result = array[0]
    answer = np.argmax(result)
    prediction = ""
    if answer == 0:
        prediction = "Huevo"
    elif answer == 1:
        prediction = "Lechuga"
    elif answer == 2:
        prediction = "Queso"
    return prediction

def open_file():
    global prediction
    file_path = filedialog.askopenfilename()
    if file_path:
        prediction = predict(file_path)
        show_result(prediction)

def show_result(prediction):
    result_window = tk.Toplevel(root)
    result_window.title("Resultado de la Predicción")

    result_label = Label(result_window, text="La predicción de la imagen es: {}".format(prediction), font=("Helvetica", 16))
    result_label.pack(pady=20)

    # Llamar a la API de Edamam y mostrar los resultados
    result_text = Edamam_API_call(prediction)
    result_label = Label(result_window, text=result_text, font=("Helvetica", 16), justify="left")
    result_label.pack(pady=20)

def window_predict():
    root = tk.Tk()
    root.title("Seleccionar Imagen")
    root.geometry("300x200")

    label = Label(root, text="Selecciona la imagen de un alimento")
    label.pack(pady=20)

    button = Button(root, text="Seleccionar Imagen", command=open_file)
    button.pack()

    root.mainloop()

def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height))

# Modificación de Edamam_API_call para devolver resultados en lugar de imprimir
def Edamam_API_call(food):
    url = 'https://api.edamam.com/api/recipes/v2'
    params = {
        'type': 'public',
        'app_id': 'f93b1901',
        'app_key': 'c5695c359ddf80efb745044e4f9b1184',
        'q': f'{food}',
        'ingr': '6',
        'mealType': 'Breakfast',
        'time': '30'
    }

    response_food = requests.get(url, params=params)
    data_dict = response_food.json()
    
    translator = Translator()
    result_text = ""

    # Imprimir solo lo que sigue después de cada clave de interés
    if 'hits' in data_dict:
        for hit in data_dict['hits']:
            recipe = hit['recipe']
            title_translated = translator.translate(recipe['label'], dest='es').text
            result_text += f"\nTítulo de la receta: {title_translated}\n"
            
            result_text += "Ingredientes:\n"
            for ingredient in recipe['ingredients']:
                ingredient_translated = translator.translate(ingredient['text'], dest='es').text
                result_text += f"- {ingredient_translated}\n"
    return result_text

# Set up the main GUI
####################
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
label_image.pack(pady=120, padx=100)  # pady y padx para añadir un poco de espacio alrededor de la imagen

label_text = tk.Label(frame_left, text="SpeedyCook", bg="#41C9E2", fg="white", font=("Segoe UI Semibold", 40))
label_text.pack()
label_textm = tk.Label(frame_left, text="Sebastian C.\n Jair R. \n Alan", bg="#41C9E2", fg="white", font=("Segoe UI Semibold", 20))
label_textm.pack()

label_text2 = tk.Label(frame_right, text="Bienvenido! \n\n Presiona el boton para empezar a generar las recetas", bg="white", font=("Segoe UI Semibold", 30), pady=100)
label_text2.pack()

buttonj = tk.Button(frame_right, text="Empezar", font=("Segoe UI Semibold", 20), bg="#41C9E2", command=window_predict)
buttonj.pack()

root.mainloop()
