from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.modules.Reclutador.loginRecruiter import login_recruiter
from src.modules.Reclutador.perfilReclu import new_client, settings
from src.modules.Reclutador.registerReclu import register_recruiter

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month)+ " a las " + str(now.hour) + ':' + str(now.minute.real)


def generar_informe_registro_pdf(nombre_archivo, reporte_registro, reporte_login, reporte_cliente, reporte_ajustes):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe del registro crearReportesRecruiter completo")
    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha + " del 2024")
    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de registro crearReportesRecruiter completo")
    c.drawString(72, 670, reporte_registro),
    c.drawString(72, 640, reporte_login)
    c.drawString(72, 610, reporte_cliente)
    c.drawString(72, 580, reporte_ajustes)

    c.save()


def report_register_recruiter():
    try:
        reporte_registro, correo = register_recruiter()
        print('\n')
        reporte_login, headers, _ = login_recruiter(correo)
        reporte_cliente = new_client(headers)
        reporte_ajustes = settings(headers)
        nombre_archivo = "reports/Registro_completo " + fecha + ".pdf"
        generar_informe_registro_pdf(nombre_archivo, reporte_registro, reporte_login, reporte_cliente, reporte_ajustes)
        print('se genera un reporte con los resultados del registro del crearReportesRecruiter', correo)
        return 'Se hizo correctamente el registroCand'
    except Exception as e:
        print(' No se creo el reporte del registro crearReportesRecruiter', e)
        return 'No se hizo el reporte'







