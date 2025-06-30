import customtkinter as ctk
from simulador import correr_simulaciones

ctk.set_appearance_mode("system")  # default
ctk.set_appearance_mode("green")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Game Studio Simulator")
        self.geometry("600x400")

        self.label = ctk.CTkLabel(self, text="Game Studio Simulator", font=("Arial", 24))
        self.label.pack(pady=20)



        self.input = ctk.CTkLabel (self, text="Enter number of simulations", width=200)
        self.input.pack(pady=10)

        self.input = ctk.CTkEntry(self, placeholder_text="Number of Simulations")
        self.input.pack(pady=10)

        self.run_button = ctk.CTkButton(self, text="Run Simulation", command=self.run_simulation)
        self.run_button.pack(pady=10)

    def run_simulation(self):

        cantidad  = int(self.input.get())
        correr_simulaciones(cantidad)

if __name__ == "__main__":
    app = App()
    app.mainloop()