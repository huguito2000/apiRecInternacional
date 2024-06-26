import tkinter as tk
from tkinter import ttk
from src.modules.Candidate.postulacion import postulacion_candidato, delete_postulation_candidate, postulacion_video
from src.modules.Candidate.registro_de_candidato_full_CV import register_complete_full_cv
from src.modules.recruiter.create_vacancy_recruiter import create_manual_vacant
from src.modules.recruiter.login_recruiter import login_recruiter
from src.modules.recruiter.profile_recruiter import canje_cupon
from src.modules.recruiter.register_recruiter import register_recruiter


email_reclutador = None  # Variable global para almacenar el email del reclutador
email_candidate = None   # Variable global para almacenar el email del candidato

def gui_candidate_prueba_demo():

    def registro_reclutador_demo():
        global email_reclutador
        print('Inicia el registro del reclutador\n')
        _, email_reclutador = register_recruiter()
        _, headers, _ = login_recruiter(email_reclutador)
        canje_cupon(headers)
        print(email_reclutador)
        return email_reclutador

    def create_vacant():
        print('Se inicia la creación de la vacante\n')
        if email_reclutador is None:
            print("No se ha registrado un reclutador.\n")
            return
        _, headers, recruiter_id = login_recruiter(email_reclutador)
        create_manual_vacant(headers, recruiter_id)

    def register_complete_full_cv_demo():
        global email_candidate
        print('Se inicia el registro de candidato con full cv\n')
        _, email_candidate, _, _ = register_complete_full_cv()
        return email_candidate

    def postulacion_candidato_demo():
        global email_reclutador
        print(email_reclutador)
        _, email_candidate2, _, _ = register_complete_full_cv()
        print('Se inicia postulacion del candidato', email_candidate2)
        _, _, _, _, _ = postulacion_candidato(email_candidate2, email_reclutador)

    def postulacion_5_candidatos_demo():
        for _ in range(6):
            _, email_candidate, _, _ = register_complete_full_cv()
            _, _, _, _, _ = postulacion_candidato(email_candidate, email_reclutador)

    def postulacion_video_demo():
        for _ in range(6):
            _, email_candidate, _, _ = register_complete_full_cv()
            _, postulation_id, headers, _, _ = postulacion_candidato(email_candidate, email_reclutador)
            postulacion_video(email_candidate, postulation_id, headers)

    def candidatos_eliminan_postulación():
        for _ in range(6):
            _, email_candidate, _, _ = register_complete_full_cv()
            _, postulation_id, headers, _, _ = postulacion_candidato(email_candidate, email_reclutador)
            delete_postulation_candidate(headers, postulation_id)


    def cancelar():
        ventana.destroy()  # Cierra la ventana

    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Mi demo Involve")
    ventana.geometry("500x600")

    # Marco para los botones
    marco_botones = ttk.Frame(ventana, padding="20")
    marco_botones.grid(row=0, column=0, sticky="new")

    # Etiqueta de título
    etiqueta_titulo = ttk.Label(marco_botones, text="Demo Involve", font=("Helvetica", 16, "bold"))
    etiqueta_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Botones
    boton_postulacion = ttk.Button(marco_botones, text="Registro de reclutador", command=registro_reclutador_demo)
    boton_postulacion.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

    boton_postulacion = ttk.Button(marco_botones, text="Crear vacante", command=create_vacant)
    boton_postulacion.grid(row=1, column=1, padx=10, pady=5, sticky=tk.E)

    boton_datos_invalidos = ttk.Button(marco_botones, text="Registro de candidato", command=register_complete_full_cv_demo)
    boton_datos_invalidos.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="Postulación", command=postulacion_candidato_demo)
    boton_buscador.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="Postulación 5 candidatos", command=postulacion_5_candidatos_demo)
    boton_buscador.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="Postulación 5 candidatos con video", command=postulacion_video_demo)
    boton_buscador.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="Postulacion eliminada", command=candidatos_eliminan_postulación)
    boton_buscador.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

    # Centrar el botón de cancelar
    boton_cancelar = ttk.Button(marco_botones, text="Cancelar", command=cancelar)
    boton_cancelar.grid(row=5, column=0, columnspan=2, pady=20)

    # Asegurarse de que las columnas se expandan uniformemente
    ventana.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(1, weight=1)

    ventana.mainloop()
