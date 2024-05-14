import requests, os
import json


def Edamam_API_call(comida, ingredintes, tipo, tiempo):
    url='https://api.edamam.com/api/recipes/v2'
    params={
        'type':'any',
        'app_id':'f93b1901',
        'app_key':'c5695c359ddf80efb745044e4f9b1184',
        'q':f'{comida}',
        'ingr':f'{ingredintes}',
        'mealType':f'{tipo}',
        'time':f'{tiempo}'
    }
    headers={"Content-Language":"es"}

    response_food=requests.get(url, params=params, headers=headers)
    data_dict = response_food.json()

    # Imprimir solo lo que sigue después de cada clave de interés
    if 'hits' in data_dict:
        for hit in data_dict['hits']:
            recipe = hit['recipe']
            os.system('cls')
            print(f'Tus ingreientes fueron: {comida}')
            print("\nTítulo de la receta:", recipe['label'])
            print("Ingredientes:")
            for ingredient in recipe['ingredients']:
                print("- ", ingredient['text'])
                
def get_food():
    pass

def main():
    meal=input('Inserte que ingreientes quiere que haya (use espacio para separar los ingredintes): ')
    ingr=int(input('Inserte la cantidad maxima de ingredientes que queire que haya: '))
    type=input('Inserte el tipo de comida que quiere (Breakfast, Dinner, Lunch, Snack, Teatime): ')
    time=int(input('Inserte el tiempo paximo que tiene para preparse su comida: '))
    Edamam_API_call(meal, ingr, type, time)

main()