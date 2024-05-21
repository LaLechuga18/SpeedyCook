import requests
import json
from googletrans import Translator

def Edamam_API_call(food):
    url = 'https://api.edamam.com/api/recipes/v2'
    params = {
        'type': 'public',
        'app_id': 'f93b1901',
        'app_key': 'c5695c359ddf80efb745044e4f9b1184',
        'q': f'{food}',
        'ingr': '4',
        'mealType': 'Breakfast',
        'time': '30'
    }

    response_food = requests.get(url, params=params)
    data_dict = response_food.json()
    
    translator = Translator()

    # Imprimir solo lo que sigue después de cada clave de interés
    if 'hits' in data_dict:
        for hit in data_dict['hits']:
            recipe = hit['recipe']
            title_translated = translator.translate(recipe['label'], dest='es').text
            print("\nTítulo de la receta:", title_translated)
            
            print("Ingredientes:")
            for ingredient in recipe['ingredients']:
                ingredient_translated = translator.translate(ingredient['text'], dest='es').text
                print("- ", ingredient_translated)

def main():
    Edamam_API_call()

main()
