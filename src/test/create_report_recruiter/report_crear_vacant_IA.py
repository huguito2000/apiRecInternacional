from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.modules.recruiter.login_recruiter import login_recruiter, email
from src.objectRepository.recruiter.create_vacant.obj_vacanteIA import post_vacancy_ia
from src.services.catalogs import obtener_fecha

fecha = obtener_fecha()


def generar_informe_crear_vacante_manual_pdf(nombre_archivo, reporte_login, reporte_crear_vancante_ia):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe de creación de vacante con IA")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha)

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en la creacion de vacante con IA")
    c.drawString(72, 640, reporte_login)
    c.drawString(72, 610, reporte_crear_vancante_ia)


def crear_vacante_ia_test():
    try:
        reporte_login, headers, recruiterID = login_recruiter(email)
        print('\n')
        reporte_crearVancanteIA = post_vacancy_ia(headers)
        print('\n')
        nombre_archivo = "report/Crear_VacanteIA " + fecha + ".pdf"
        generar_informe_crear_vacante_manual_pdf(nombre_archivo, reporte_login, reporte_crearVancanteIA)
        return reporte_crearVancanteIA
    except Exception as e:
        print('\n No se creo la vacante manual', {e})
        return 'No se creo la vacante manual'

