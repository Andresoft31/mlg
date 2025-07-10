import customtkinter as ctk
import tkinter as tk
import threading
import json

from core.motor import simular_varias
from adaptadores.shooter import ShooterAdapter
import pandas as pd

ctk.set_appearance_mode("system")  # o "light", "dark"
ctk.set_default_color_theme("green")  # opcional, tu color preferido

class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Game Studio Simulator")
        self.geometry("600x500")

        # Título
        self.label = ctk.CTkLabel(self, text="Game Studio Simulator", font=("Arial", 24))
        self.label.pack(pady=20)

        # Input de cantidad
        self.input_label = ctk.CTkLabel(self, text="Enter number of simulations")
        self.input_label.pack(pady=10)

        self.input = ctk.CTkEntry(self, placeholder_text="Number of Simulations")
        self.input.pack(pady=10)

        # Botón de simulación
        self.run_button = ctk.CTkButton(self, text="Run Simulation", command=self.run_simulation)
        self.run_button.pack(pady=10)

        # Output
        self.output_box = ctk.CTkTextbox(self, width=500, height=200)
        self.output_box.pack(pady=20)

    def run_simulation(self):
        def tarea():
            try:
                cantidad = int(self.input.get())

                with open("config/config.json") as f:
                    config = json.load(f)
                
                adaptador = ShooterAdapter()
                resultados = simular_varias(config, adaptador, cantidad)

                # Mostrar confirmación en la interfaz
                self.output_box.insert(tk.END, "✅ Simulación completada. Revisa el archivo 'salida.xlsx'.\n")

                # Intentar abrir el Excel automáticamente (macOS o Windows)
                import os
                import platform

                ruta_excel = os.path.abspath("salida.xlsx")
                if platform.system() == "Darwin":  # macOS
                    os.system(f"open '{ruta_excel}'")
                elif platform.system() == "Windows":
                    os.startfile(ruta_excel)

            except ValueError:
                self.output_box.insert(tk.END, "❌ Ingresa un número válido.\n")
            except FileNotFoundError:
                self.output_box.insert(tk.END, "❌ No se encontró el archivo config/config.json.\n")
            except Exception as e:
                self.output_box.insert(tk.END, f"❌ Error inesperado: {str(e)}\n")

        threading.Thread(target=tarea).start()


if __name__ == "__main__":
    app = App()
    app.mainloop()
