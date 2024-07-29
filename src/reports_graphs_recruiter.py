import tkinter as tk
from tkinter import ttk
from src.modules.recruiter.change_cupon import change_cupon_client
from src.modules.recruiter.clients import customer_section
from src.modules.recruiter.create_vacancy_recruiter import create_manual_vacant, create_vacant_ia
from src.modules.recruiter.i_forgot_my_pass_recruiter import i_forgot_pass_my_recruiter
from src.modules.recruiter.login_recruiter import login_recruiter, email, pass_email
from src.modules.recruiter.register_recruiter import register_recruiter
from src.modules.recruiter.settings_recruiter import settings
from src.services.catalogs import obtener_fecha, env, generate_report_graphs
from src.test.create_report_recruiter.create_graphs_recruiter import report_complete_recruiter_graphs

fecha = obtener_fecha()
reports = env["DIR_REPORTS"]


def gui_recruiter_graphs():

    def report_login_recruiter():
        print('reporte de inicio de sesión del candidato')
        _, _, _, total, function_results = login_recruiter(email, pass_email)
        generate_report_graphs(total, function_results, 'Resultado de login_recruiter',
                               f'{reports}/reporte login reclutador {fecha}.pdf')

    def report_i_forgot_recruiter():
        _, total, function_results = i_forgot_pass_my_recruiter()
        generate_report_graphs(total, function_results, 'Resultado de i_forgot_pass_my_recruiter',
                               f'{reports}/reporte olvide mi contraseña reclutador {fecha}.pdf')

    def report_register_recruiter():
        _, total, function_results = register_recruiter()
        generate_report_graphs(total, function_results, 'Resultado de registro reclutador',
                               f'{reports}/reporte registro reclutador {fecha}.pdf')


    def report_clients():
        _,  total, function_results = customer_section()
        generate_report_graphs(total, function_results, 'Resultado de customer_section',
                               f'{reports}/reporte seccion de clientes {fecha}.pdf')

    def report_change_cupon():
        _,  total, function_results = change_cupon_client()
        generate_report_graphs(total, function_results, 'Resultado de change_cupon_client',
                               f'{reports}/reporte seccion de canje de cupon {fecha}.pdf')

    def report_settings_recruiter():
        _, total, function_results = settings()
        generate_report_graphs(total, function_results, 'Resultado de settings_recruiter',
                               f'{reports}/reporte seccion de ajustes del reclutador {fecha}.pdf')

    def report_create_vacant():
        _, total, function_results = create_manual_vacant()
        generate_report_graphs(total, function_results, 'Resultado de create_vacant',
                               f'{reports}/reporte seccion de crear vacante manual {fecha}.pdf')

    def report_create_vacant_IA():
        _, total, function_results = create_vacant_ia()
        generate_report_graphs(total, function_results, 'Resultado de create_vacant_IA',
                               f'{reports}/reporte seccion de crear vacante IA {fecha}.pdf')

    def report_happy_path_recruiter():
        report_complete_recruiter_graphs()



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
    etiqueta_titulo = ttk.Label(marco_botones, text="Generar reportes de los test cases reclutador",
                                font=("Helvetica", 16, "bold"))
    etiqueta_titulo.grid(column=0, row=0, columnspan=2, pady=10)

    # Botones
    boton_postulacion = ttk.Button(marco_botones, text="Reporte olvide mi contraseña",
                                   command=report_i_forgot_recruiter)
    boton_postulacion.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

    boton_datos_invalidos = ttk.Button(marco_botones, text="Reporte iniciar sesión", command=report_login_recruiter)
    boton_datos_invalidos.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

    boton_happy_path = ttk.Button(marco_botones, text="Reporte registro reclutador",
                                  command=report_register_recruiter)
    boton_happy_path.grid(row=2, column=0, padx=10, pady=5)

    boton_buscador = ttk.Button(marco_botones, text="reporte crear cliente", command=report_clients)
    boton_buscador.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte canje de cupón", command=report_change_cupon)
    boton_buscador.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte ajustes", command=report_settings_recruiter)
    boton_buscador.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte crear vacante", command=report_create_vacant)
    boton_buscador.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte crear vacante IA ", command=report_create_vacant_IA)
    boton_buscador.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

    boton_buscador = ttk.Button(marco_botones, text="reporte happy path reclutador", command=report_happy_path_recruiter)
    boton_buscador.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

    # Centrar el botón de cancelar
    boton_cancelar = ttk.Button(marco_botones, text="Cancelar", command=cancelar)
    boton_cancelar.grid(row=5, column=1, columnspan=2, pady=20)

    # Asegurarse de que las columnas se expandan uniformemente
    ventana.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(0, weight=1)
    marco_botones.grid_columnconfigure(1, weight=1)

    ventana.mainloop()

