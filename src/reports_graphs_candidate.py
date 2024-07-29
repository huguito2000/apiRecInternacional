import tkinter as tk
from tkinter import ttk
from src.modules.Candidate.i_forgot_my_pass import i_forgot_password_candidate
from src.modules.Candidate.loginCand import login_cand, email_candidate, pass_email
from src.modules.Candidate.my_data_profile import my_data_profile
from src.modules.Candidate.postulacion import postulacion_candidato
from src.modules.Candidate.registro_de_candidato_full_CV import register_complete_full_cv
from src.modules.Candidate.settings_candidate import settings_candidate
from src.modules.Candidate.testDatosNoValidos import candidate_data_invalid
from src.services.catalogs import generate_report_graphs, obtener_fecha, env
from src.test.create_report_candidate.create_graphs import report_graphs_complete

fecha = obtener_fecha()
reports = env["DIR_REPORTS"]


def gui_candidate_graphs():

    def reporte_i_forgot_password_candidate():
        print('reporte de olvide mi contraseña')
        _, total, function_results = i_forgot_password_candidate()
        generate_report_graphs(total, function_results, 'Resultado de i_forgot_password_candidate',
                               f'{reports}/olvide mi contraseña {fecha}.pdf')

    def reporte_login_cand():
        print('reporte de inicio de sesión del candidato')
        _, _, _, total, function_results = login_cand(email_candidate, pass_email)
        generate_report_graphs(total, function_results, 'Resultado de login_cand',
                               f'{reports}/reporte login candidato {fecha}.pdf')

    def reporte_register_complete_full_cv():
        print('reporte de registro de candidato con full cv')
        _, email_candidate, total, function_results = register_complete_full_cv()
        generate_report_graphs(total, function_results, 'Resultado de register_complete_full_cv',
                               f'{reports}/registro con full cv {fecha}.pdf')

    def reporte_postulacion_candidato():
        print('reporte postulacion del candidato')

        _, _, _, total, function_results = postulacion_candidato(email_candidate)
        generate_report_graphs(total, function_results, 'Resultado de postulacion_candidato',
                               f'{reports}/postulación {fecha}.pdf')

    def reporte_mis_datos():
        _, total, function_results = my_data_profile()
        generate_report_graphs(total, function_results, 'Resultado de my_data_profile',
                               f'{reports}/mis datos {fecha}.pdf')

    def reporte_search_vacancy():
        print('reporte de busqueda de vacantes')

    def reporte_configuraciones():
        _, total, function_results = settings_candidate()
        generate_report_graphs(total, function_results, 'Resultado de settings_candidate',
                               f'{reports}/configuración {fecha}.pdf')

    def reporte_datos_no_validos():
        _, total, function_results = candidate_data_invalid()
        generate_report_graphs(total, function_results, 'Resultado de candidate_data_invalid',
                               f'{reports}/reporte candidato datos invalidos {fecha}.pdf')

    def reporte_happy_path_completo():
        report_graphs_complete()

    def cancelar():
        ventana.destroy()  # Cierra la ventana

    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Mi aplicación")
    ventana.geometry("500x400")

    # Marco para los botones
    marco_botones = ttk.Frame(ventana, padding="20")
    marco_botones.grid(row=0, column=0, sticky="new")

    # Etiqueta de título
    etiqueta_titulo = ttk.Label(marco_botones, text="Generar reportes de los test cases", font=("Helvetica", 16, "bold"))
    etiqueta_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Botones
    boton_postulacion = ttk.Button(marco_botones, text="Reporte olvide mi contraseña", command=reporte_i_forgot_password_candidate)
    boton_postulacion.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

    boton_datos_invalidos = ttk.Button(marco_botones, text="Reporte iniciar sesión", command=reporte_login_cand)
    boton_datos_invalidos.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

    boton_happy_path = ttk.Button(marco_botones, text="Reporte registro completo", command=reporte_register_complete_full_cv)
    boton_happy_path.grid(row=2, column=0, padx=10, pady=5)

    boton_buscador = ttk.Button(marco_botones, text="reporte postulación", command=reporte_postulacion_candidato)
    boton_buscador.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte busqueda de vacantes", command=reporte_search_vacancy)
    boton_buscador.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte mis datos", command=reporte_mis_datos)
    boton_buscador.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte datos no validos", command=reporte_datos_no_validos)
    boton_buscador.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte configuración ", command=reporte_configuraciones)
    boton_buscador.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte happy path", command=reporte_happy_path_completo)
    boton_buscador.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

    # Centrar el botón de cancelar
    boton_cancelar = ttk.Button(marco_botones, text="Cancelar", command=cancelar)
    boton_cancelar.grid(row=5, column=1, columnspan=2, pady=20)

    # Asegurarse de que las columnas se expandan uniformemente
    ventana.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(1, weight=1)

    ventana.mainloop()
