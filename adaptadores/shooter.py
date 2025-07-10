import random

class ShooterAdapter:
    def __init__(self):
        self.player_id = None

    def elegir_accion(self, config):
        perfil = random.choice(config["player_profiles"])
        self.player_id = perfil["id"]
        acciones = list(perfil["probabilidades"].keys())
        pesos = list(perfil["probabilidades"].values())
        return random.choices(acciones, weights=pesos)[0]

    def ejecutar_accion(self, config, accion):
        return config["event_definitions"].get(accion)