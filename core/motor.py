from core.reglas import aplicar_evento
import pandas as pd
import copy

def simular_jugada(config, id, adaptador):
    estado = copy.deepcopy(config["estado_inicial"])

    accion = adaptador.elegir_accion(config)
    evento = config["event_definitions"].get(accion, None)
    nuevo_estado = aplicar_evento(estado, evento) if evento else estado

    return {

        "id": id,
        "player_id": adaptador.player_id,
        "accion_elegida": accion,
        "estado_resultante": nuevo_estado,
        "evento_aplicado": evento
        
    }
def simular_varias(config, adaptador, cantidad):
    resultados = [simular_jugada(config, i, adaptador) for i in range(cantidad)]
    df = pd.json_normalize(resultados)
    df.to_excel('salida.xlsx', index=False)
    return resultados  # opcional si querés mostrar en GUI

       

