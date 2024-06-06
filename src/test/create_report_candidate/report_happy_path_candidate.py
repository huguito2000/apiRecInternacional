from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.modules.Candidate.loginCand import login_cand
from src.modules.Candidate.postulacion import postulacion_candidato
from src.modules.Candidate.registerMyCV import register_cv
from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.modules.Candidate.registro_de_candidato_full_CV import register_complete_full_cv
from src.modules.Candidate.testDatosNoValidos import candidate_data_invalid
from src.services.catalogs import obtener_fecha

fecha = obtener_fecha()

def generar_informe_happy_path_candidate_pdf(nombre_archivo, reporte_register_onboarding_candidate,
                                             reporte_register_my_cv,
                                             reporte_register_full_cv,
                                             reporte_postulacion, reporte_test_datos_no_validos,
                                             reporte_login_candidato):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe del Happy path")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha)

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de Happy path del candidato")
    c.drawString(72, 640, reporte_register_onboarding_candidate)
    c.drawString(72, 610, reporte_register_my_cv)
    c.drawString(72, 580, reporte_register_full_cv)
    c.drawString(72, 550, reporte_postulacion)
    c.drawString(72, 520, reporte_test_datos_no_validos)
    c.drawString(72, 490, reporte_login_candidato)

    c.save()


def happypath_test_candidate(enviroment):
    try:
        print('\n')
        reporte_register_onboarding_candidate, email = register_onboarding_candidate(enviroment)
        print('\n', email)
        reporte_register_my_cv = register_cv(email)
        print('\n')
        reporte_register_full_cv = register_complete_full_cv(enviroment)
        print('\n')
        reporte_postulacion = postulacion_candidato(email)
        print('\n')
        reporte_test_datos_no_validos = candidate_data_invalid(enviroment)
        print('\n')
        reporte_login_candidato, _, _ = login_cand(email)
        print('\n')
        nombre_archivo = "reports/Registro HappyPath candidato " + fecha + ".pdf"

        print('\n')
        generar_informe_happy_path_candidate_pdf(nombre_archivo, reporte_register_onboarding_candidate,
                                                 reporte_register_my_cv, reporte_register_full_cv,
                                                 reporte_postulacion, reporte_test_datos_no_validos,
                                                 reporte_login_candidato)
        print('Se genera el reporte con los resultados del Happy Path')
        return 'Se hizo correctamente el happy path'
    except Exception as e:
        print('No se hizo el happy path del candidato', {e})
        return 'No se hizo el happy path'
