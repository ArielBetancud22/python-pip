import requests

def get_razas():
    r = requests.get('https://dog.ceo/api/breeds/list')
    print(r.status_code)
    #print(r.text)
    #print(type(r.text))  #Vemos de que tipo es el texto, puede ser un string
    #En este caso es: es un string por el text, pero aquí
    #encontramos un diccionario con listas
    razas = r.json()
    for raza  in razas.values():#Utilizamos la función para los valores
        print(f"Raza de los perritos: {raza[5]}") #Estamos recorriendo los valores del diccionario