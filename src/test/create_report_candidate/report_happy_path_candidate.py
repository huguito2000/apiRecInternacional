from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from src.modules.Candidate.busquedaVacantes import search_vacancy
from src.modules.Candidate.loginCand import login_cand
from src.modules.Candidate.postulacion import postulacion_candidato
from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.modules.Candidate.registro_de_candidato_full_CV import register_complete_full_cv
from src.modules.Candidate.testDatosNoValidos import candidate_data_invalid
from src.modules.recruiter.create_vacancy_recruiter import create_manual_vacant
from src.modules.recruiter.login_recruiter import login_recruiter, email
from src.services.catalogs import obtener_fecha

fecha = obtener_fecha()

def generar_informe_happy_path_candidate_pdf(nombre_archivo, reporte_register_onboarding_candidate,
                                             reporte_register_full_cv, reporte_postulacion,
                                             reporte_test_datos_no_validos, reporte_login_candidato, reporte_buscador):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe del Happy path")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha)

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de Happy path del candidato")
    c.drawString(72, 640, reporte_register_onboarding_candidate)
    c.drawString(72, 610, reporte_register_full_cv)
    c.drawString(72, 580, reporte_postulacion)
    c.drawString(72, 550, reporte_test_datos_no_validos)
    c.drawString(72, 520, reporte_login_candidato)
    c.drawString(72, 490, reporte_buscador)
    c.save()


def happypath_test_candidate(enviroment):
    try:
        nombre_archivo = "reports/Registro HappyPath candidato " + fecha + ".pdf"
        print('\nInicia el registro del onboarding del usuario candidato')
        reporte_register_onboarding_candidate, _ = register_onboarding_candidate(enviroment)
        print('\nInicia el registro del candidato con CV completo ')
        reporte_register_full_cv, email_candidate = register_complete_full_cv(enviroment)
        print('\nSe hace login de reclutador para creacion de una vacante')
        _, headers, recruiter_id = login_recruiter(email)
        print('\nInicia el proceso de la creacion de la vacante manual')
        create_manual_vacant(headers, recruiter_id)
        print('\nSe postula a la vacante')
        reporte_postulacion = postulacion_candidato(email_candidate)
        print('\nSe inicia las pruebas de datos invalidos')
        reporte_test_datos_no_validos = candidate_data_invalid(enviroment)
        print('\nSe hace el login del candidato')
        reporte_login_candidato, _, _ = login_cand(email_candidate)
        print('\nSe inicia las pruebas de buscador de vacantes')
        reporte_buscador = search_vacancy()
        generar_informe_happy_path_candidate_pdf(nombre_archivo, reporte_register_onboarding_candidate,
                                                 reporte_register_full_cv, reporte_postulacion,
                                                 reporte_test_datos_no_validos, reporte_login_candidato,
                                                 reporte_buscador)
        print('Se genera el reporte con los resultados del Happy Path:) \n')
        return 'Se hizo correctamente el happy path'
    except Exception as e:
        print('No se hizo el happy path del candidato :( \n', e)
        return 'No se hizo el happy path'
