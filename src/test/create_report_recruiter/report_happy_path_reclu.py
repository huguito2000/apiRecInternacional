from src.modules.recruiter.create_vacancy_recruiter import create_manual_vacant, create_vacant_ia
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.modules.recruiter.login_recruiter import *
from src.modules.recruiter.profile_recruiter import new_client, settings
from src.objectRepository.recruiter.ajustesReclu.step_clients import change_cupon
from src.services.catalogs import obtener_fecha
from src.modules.recruiter.register_recruiter import register_recruiter

fecha = obtener_fecha()


def generar_informe_happy_path_reclu_pdf(nombre_archivo, reporte_login, reporte_cliente, reporte_canje_cupon,
                                         reporte_ajustes,
                                         reporte_crear_vacante_manual, reporte_crear_vacante_ia):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe del Happy path")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha)

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de Happy path")
    c.drawString(72, 640, reporte_login)
    c.drawString(72, 610, reporte_cliente)
    c.drawString(72, 580, reporte_ajustes)
    c.drawString(72, 550, reporte_crear_vacante_manual)
    c.drawString(72, 520, reporte_crear_vacante_ia)

    c.save()


def happypath_test_reclu():
    try:
        _, email = register_recruiter()
        print('\n')
        reporte_login, headers, recruiter_id = login_recruiter(email)
        print('\n')
        reporte_cliente = new_client(headers)
        print('\n')
        reporte_canje_cupon = change_cupon(headers)
        print('\n')
        reporte_ajustes = settings(headers)
        print('\n')
        reporte_crear_vacante_manual = create_manual_vacant(headers, recruiter_id)
        print('\n')
        reporte_crear_vacante_ia = create_vacant_ia(headers)
        print('\n')
        nombre_archivo = "reports/Registro HappyPath del reclutador" + fecha + ".pdf"
        print('\n')
        generar_informe_happy_path_reclu_pdf(nombre_archivo, reporte_login, reporte_cliente, reporte_canje_cupon,
                                             reporte_ajustes, reporte_crear_vacante_manual, reporte_crear_vacante_ia)
        print('Se genera el reporte con los resultados del Happy Path')
        return 'Se hizo correctamente el happy path'
    except Exception as e:
        print('No se hizo el happy path', {e})
        return 'No se hizo el happy path'
