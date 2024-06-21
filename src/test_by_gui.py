import tkinter as tk
from tkinter import ttk
from dotenv import dotenv_values

from src.modules.Candidate.busquedaVacantes import search_vacancy
from src.test.create_report_candidate.report_data_no_valid import data_no_valid_candidate
from src.test.create_report_candidate.report_happy_path_candidate import happypath_test_candidate
from src.test.create_report_candidate.report_postulation import postulacion_test_candidate
from src.test.create_report_candidate.report_search import buscador_test_candidate


def gui_candidate():
    def reporte_datos_no_validos():
        data_no_valid_candidate()

    def reporte_happy_path():
        happypath_test_candidate()

    def busqueda_vacantes():
        buscador_test_candidate()

    def reporte_postulacion():
        postulacion_test_candidate()

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
    boton_postulacion = ttk.Button(marco_botones, text="Reporte Postulacion", command=reporte_postulacion)
    boton_postulacion.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

    boton_datos_invalidos = ttk.Button(marco_botones, text="Reporte datos no validos", command=reporte_datos_no_validos)
    boton_datos_invalidos.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

    boton_happy_path = ttk.Button(marco_botones, text="Reporte happy path", command=reporte_happy_path)
    boton_happy_path.grid(row=2, column=0, padx=10, pady=5)

    boton_buscador = ttk.Button(marco_botones, text="reporte buscador", command=busqueda_vacantes)
    boton_buscador.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

    # Centrar el botón de cancelar
    boton_cancelar = ttk.Button(marco_botones, text="Cancelar", command=cancelar)
    boton_cancelar.grid(row=3, column=0, columnspan=2, pady=20)

    # Asegurarse de que las columnas se expandan uniformemente
    ventana.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(1, weight=1)

    ventana.mainloop()
