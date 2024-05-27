from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from src.modules.Candidate.loginCand import correo
from src.modules.Reclutador.loginRecruiter import login_recruiter
from src.objectRepository.recruiter.crearVacante.obj_vacanteManual1 import paso1
from src.objectRepository.recruiter.crearVacante.obj_vacanteManual2 import paso2
from src.objectRepository.recruiter.crearVacante.obj_vacanteManual3 import paso3
from src.objectRepository.recruiter.crearVacante.obj_vacanteManual4 import paso4, paso5, paso6, paso7

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month) + " a las " + str(now.hour) + ':' + str(now.minute.real)


def generar_informe_crear_vacante_manual_pdf(nombre_archivo, reporte_login, reporte_paso1, reporte_paso2, reporte_paso3,
                                             reporte_paso4, reporte_paso5, reporte_paso6, reporte_paso7):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe de creación de vacante manual")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha + " del 2024")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en la creacion de vacante manual")
    c.drawString(72, 640, reporte_login)
    c.drawString(72, 610, reporte_paso1)
    c.drawString(72, 580, reporte_paso2)
    c.drawString(72, 550, reporte_paso3)
    c.drawString(72, 520, reporte_paso4)
    c.drawString(72, 490, reporte_paso5)
    c.drawString(72, 460, reporte_paso6)
    c.drawString(72, 430, reporte_paso7)

    c.save()


def crear_vacante_manual_test():
    try:
        reporte_login, headers, recruiter_id = login_recruiter(correo)
        print('\n')
        reporte_paso1, vacant_id = paso1(headers)
        print('\n')
        reporte_paso2 = paso2(vacant_id, headers)
        print('\n')
        reporte_paso3 = paso3(vacant_id, headers)
        print('\n')
        reporte_paso4 = paso4(vacant_id, headers)
        print('\n')
        reporte_paso5 = paso5(vacant_id, headers)
        print('\n')
        reporte_paso6 = paso6(vacant_id, headers, recruiter_id)
        print('\n')
        reporte_paso7 = paso7(vacant_id, headers)
        print('\n')
        nombre_archivo = "reportes/Crear_vacanteManual " + fecha + ".pdf"
        generar_informe_crear_vacante_manual_pdf(nombre_archivo, reporte_login, reporte_paso1, reporte_paso2,
                                                 reporte_paso3, reporte_paso4, reporte_paso5, reporte_paso6,
                                                 reporte_paso7)
        return reporte_paso7
    except Exception as e:
        print('\n No se creo la vacante manual', e)
        return 'No se creo la vacante manual'
