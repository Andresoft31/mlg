import random 

import pandas as pd

import json

def cargar_config(path='config.json'):
    with open(path, "r") as file:
        return json.load(file)



def simular_partida(config , id):
    
    
        
        jugador = random.choice(config['jugadores']),
        acciones =  random.choice(config['acciones']),
        resultado = random.choices(
              population=list(config["probabilidades"].keys()),
              weights=list(config["probabilidades"].values())) [0]
               
        return {
         

            "id": id,
            "jugador":  jugador,
            "accion": acciones,
            "resultado": resultado
        }

def correr_simulaciones(cantidad):
    config = cargar_config()
    datos= [simular_partida(config ,i) for i in range (cantidad)]
    df= pd.DataFrame(datos)
    df.to_csv('resultados/simulaciones.csv', index=False)
    print(f"Simulaciones guardadas en 'simulaciones.csv' con {cantidad} partidas.")

