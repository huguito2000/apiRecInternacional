from src.modules.Candidate.loginCand import correo
from src.modules.Reclutador.createVacancyRecruiter import crear_vacante_manual, crear_vacante_ia
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from src.modules.Reclutador.loginRecruiter import login_recruiter
from src.modules.Reclutador.perfilReclu import new_client, settings

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month) + " a las " + str(now.hour) + ':' + str(now.minute.real)


def generar_informe_happy_path_reclu_pdf(nombre_archivo, reporte_login, reporte_cliente, reporte_ajustes, reporte_crear_vacante_manual, reporte_crear_vacante_ia):

    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe del Happy path")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha + " del 2024")

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
        print('\n')
        reporte_login, headers, recruiter_id = login_recruiter(correo)
        print('\n')
        reporte_cliente = new_client(headers)
        print('\n')
        reporte_ajustes = settings(headers)
        print('\n')
        reporte_crear_vacante_manual = crear_vacante_manual(headers, recruiter_id)
        print('\n')
        reporte_crear_vacante_ia = crear_vacante_ia(headers)
        print('\n')
        nombre_archivo = "reportes/Registro_HappyPath " + fecha + ".pdf"
        print('\n')
        generar_informe_happy_path_reclu_pdf(nombre_archivo, reporte_login, reporte_cliente, reporte_ajustes, reporte_crear_vacante_manual, reporte_crear_vacante_ia)
        print('Se genera el reporte con los resultados del Happy Path')
        return 'Se hizo correctamente el happy path'
    except Exception as e:
        print('No se hizo el happy path', {e})
        return 'No se hizo el happy path'

