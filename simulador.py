# import json
# from core.motor import simular_jugadas
# from adaptadores import shooter # suponiendo que el tipo es shooter

# # def simular_varias(config, adaptador, cantidad=10):
# #     resultados = []
# #     for i in range(cantidad):
# #         resultado = simular_jugadas(config, i, adaptador)
# #         resultados.append(resultado)
# #     return resultados

# # if __name__ == "__main__":
# #     with open("config/config.json") as f:
# #         config = json.load(f)

# #     cantidad = 10
# #     resultados = simular_varias(config, shooter, cantidad)

# #     for r in resultados:
# #         print(r)



# import random 
# import pandas as pd
# import json


# def cargar_config(path='config.json'):
#     with open(path, "r") as file:
#         return json.load(file)

# import random
# import copy

# def simular_json(config, id):
#     # 1. Selecciona un perfil al azar
#     perfil = random.choice(config["player_profiles"])
#     acciones = list(perfil["probabilidades"].keys())
#     pesos = list(perfil["probabilidades"].values())
    
#     # 2. Elige una acción según probabilidad
#     accion_elegida = random.choices(acciones, weights=pesos, k=1)[0]
    
#     # 3. Obtiene definición del evento
#     definicion = config["event_definitions"].get(accion_elegida)
    
#     # 4. Copia el estado inicial para modificarlo sin afectar el original
#     estado = copy.deepcopy(config["estado_inicial"])
    
#     # 5. Aplica efecto si hay definición
#     if definicion:
#         objetivo = definicion["afecta"]
#         atributo = definicion["modifica"]
#         valor = definicion["valor"]
        
#         # Aplica el cambio al estado
#         if objetivo in estado and atributo in estado[objetivo]:
#             estado[objetivo][atributo] += valor
    
#     # 6. Retorna estructura de resultado
#     return {
#         "id": id,
#         "player_id": perfil["id"],
#         "accion_elegida": accion_elegida,
#         "estado_resultante": estado,
#         "evento_aplicado": definicion
#     }



# # def simular_partida(config , id):
    
# #         jugador = random.choice(config['jugadores']),
# #         acciones =  random.choice(config['acciones']),
# #         resultado = random.choices(
# #         population=list(config["probabilidades"].keys()),
# #         weights=list(config["probabilidades"].values())) [0]
 
# #         return {
        
# #             "id": id,
# #             "jugador":  jugador,
# #             "accion": acciones,
# #             "resultado": resultado
# #         }

# def correr_simulaciones(cantidad):
#     config = cargar_config()
#     datos= [simular_json(config ,i) for i in range (cantidad)]
#     df= pd.DataFrame(datos)
#     df.to_csv('resultados/simulaciones.csv', index=False)
#     print(f"Simulaciones guardadas en 'simulaciones.csv' con {cantidad} partidas.")

