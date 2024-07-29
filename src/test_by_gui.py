import tkinter as tk
from tkinter import ttk
from src.reports_graphs_candidate import gui_candidate_graphs
from src.reports_graphs_recruiter import gui_recruiter_graphs


def gui_report():
    def gui_recruiter():
        gui_recruiter_graphs()

    def gui_candidate():
        gui_candidate_graphs()

    def cancelar():
        ventana.destroy()  # Cierra la ventana

    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Mi aplicación")
    ventana.geometry("500x400")

    # Marco para los botones
    marco_botones = ttk.Frame(ventana, padding="20")
    marco_botones.grid(row=0, column=0, sticky="nsew")

    # Etiqueta de título
    etiqueta_titulo = ttk.Label(marco_botones, text="Interfaz de test cases", font=("Helvetica", 16, "bold"))
    etiqueta_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Botones
    boton_postulacion = ttk.Button(marco_botones, text="Reportes Reclutador", command=gui_recruiter)
    boton_postulacion.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

    boton_datos_invalidos = ttk.Button(marco_botones, text="Reporte Candidato ", command=gui_candidate)
    boton_datos_invalidos.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)


    # Centrar el botón de cancelar
    boton_cancelar = ttk.Button(marco_botones, text="Cancelar", command=cancelar)
    boton_cancelar.grid(row=2, column=0, columnspan=2, pady=20)

    # Asegurarse de que las columnas se expandan uniformemente
    ventana.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(1, weight=1)

    ventana.mainloop()
