from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.modules.recruiter.login_recruiter import login_recruiter
from src.modules.recruiter.settings_recruiter import new_client, settings
from src.modules.recruiter.register_recruiter import register_recruiter
from src.services.catalogs import obtener_fecha

fecha = obtener_fecha()


def generar_informe_registro_pdf(nombre_archivo, reporte_registro, reporte_login, reporte_cliente, reporte_ajustes):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe del registro create_report_recruiter completo")
    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha)
    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de registro create_report_recruiter completo")
    c.drawString(72, 670, reporte_registro),
    c.drawString(72, 640, reporte_login)
    c.drawString(72, 610, reporte_cliente)
    c.drawString(72, 580, reporte_ajustes)

    c.save()


def report_register_recruiter():
    try:
        reporte_registro, email = register_recruiter()
        print('\n')
        reporte_login, headers, _ = login_recruiter(email)
        reporte_cliente = new_client(headers)
        reporte_ajustes = settings(headers)
        nombre_archivo = "reports/Registro completo del reclutador " + fecha + ".pdf"
        generar_informe_registro_pdf(nombre_archivo, reporte_registro, reporte_login, reporte_cliente, reporte_ajustes)
        print('se genera un reporte con los resultados del registro del create_report_recruiter', email)
        return 'Se hizo correctamente el registroCand'
    except Exception as e:
        print(' No se creo el reporte del registro create_report_recruiter', e)
        return 'No se hizo el reporte'







