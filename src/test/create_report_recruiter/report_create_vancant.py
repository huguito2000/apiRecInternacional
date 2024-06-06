from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.modules.recruiter.login_recruiter import login_recruiter, email
from src.objectRepository.recruiter.create_vacant.obj_vacanteManual1 import position_title
from src.objectRepository.recruiter.create_vacant.obj_vacanteManual2 import job_description
from src.objectRepository.recruiter.create_vacant.obj_vacanteManual3 import job_skills, contract_conditions
from src.objectRepository.recruiter.create_vacant.obj_vacanteManual4 import question_soft_skill, video_psicometricas, \
    review_vacant, post_vacancy
from src.services.catalogs import obtener_fecha

fecha = obtener_fecha()


def generar_informe_crear_vacante_manual_pdf(nombre_archivo, reporte_login, reporte_position_title,
                                             reporte_job_description, reporte_contract_conditions,
                                             reporte_job_skills, reporte_question_soft_skill,
                                             reporte_video_psicometricas, reporte_review_vacant, reporte_post_vacancy):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe de creación de vacante manual")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha)

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en la creacion de vacante manual")
    c.drawString(72, 640, reporte_login)
    c.drawString(72, 610, reporte_position_title)
    c.drawString(72, 580, reporte_job_description)
    c.drawString(72, 550, reporte_contract_conditions)
    c.drawString(72, 520, reporte_job_skills)
    c.drawString(72, 490, reporte_question_soft_skill)
    c.drawString(72, 460, reporte_video_psicometricas)
    c.drawString(72, 430, reporte_review_vacant)
    c.drawString(72, 400, reporte_post_vacancy)

    c.save()


def crear_vacante_manual_test():
    try:
        print('\n', email)
        reporte_login, headers, recruiter_id = login_recruiter(email)
        print('\n', email)
        reporte_position_title, vacant_id = position_title(headers)
        print('\n')
        reporte_job_description = job_description(vacant_id, headers)
        print('\n')
        reporte_contract_conditions = contract_conditions(vacant_id, headers)
        print('\n')
        reporte_job_skills = job_skills(vacant_id, headers)
        print('\n')
        reporte_question_soft_skill = question_soft_skill(vacant_id, headers)
        print('\n')
        reporte_video_psicometricas = video_psicometricas(vacant_id, headers)
        print('\n')
        reporte_review_vacant = review_vacant(vacant_id, headers, recruiter_id)
        print('\n')
        reporte_post_vacancy = post_vacancy(vacant_id, headers)
        print('\n')
        nombre_archivo = "reports/Crear vacanteManual " + fecha + ".pdf"
        generar_informe_crear_vacante_manual_pdf(nombre_archivo, reporte_login, reporte_position_title,
                                                 reporte_job_description, reporte_contract_conditions,
                                                 reporte_job_skills, reporte_question_soft_skill,
                                                 reporte_video_psicometricas, reporte_review_vacant,
                                                 reporte_post_vacancy)
        return reporte_post_vacancy
    except Exception as e:
        print('\n No se creo la vacante manual', e)
        return 'No se creo la vacante manual'
