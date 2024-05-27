from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from src.modules.Candidate.loginCand import correo
from src.modules.Reclutador.loginRecruiter import login_recruiter
from src.objectRepository.recruiter.crearVacante.obj_vacanteIA import publicar_ia

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month) + " a las " + str(now.hour) + ':' + str(now.minute.real)


def generar_informe_crear_vacante_manual_pdf(nombre_archivo, reporte_login, reporte_crear_vancante_ia):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe de creación de vacante con IA")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha + " del 2024")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en la creacion de vacante con IA")
    c.drawString(72, 640, reporte_login)
    c.drawString(72, 610, reporte_crear_vancante_ia)

def crear_vacante_ia_test():
    try:
        reporte_login, headers, recruiterID = login_recruiter(correo)
        print('\n')
        reporte_crearVancanteIA = publicar_ia(headers)
        print('\n')
        nombre_archivo = "reportes/Crear_VacanteIA " + fecha + ".pdf"
        generar_informe_crear_vacante_manual_pdf(nombre_archivo, reporte_login, reporte_crearVancanteIA)
        return reporte_crearVancanteIA
    except Exception as e:
        print('\n No se creo la vacante manual', {e})
        return 'No se creo la vacante manual'

