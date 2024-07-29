from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from src.modules.Candidate.loginCand import login_cand, pass_email
from src.modules.Candidate.registro_de_candidato_full_CV import register_complete_full_cv
from src.object_repository.candidate.postulacion.step_postulacion import postulacion, exp_laboral_cuestionario, \
    habilidad_profesional, habilidad_blandas, expectativa_salarial, condiciones_de_contratacion, seleccion_de_permisos
from src.services.catalogs import obtener_fecha

fecha = obtener_fecha()
print(fecha)


def generar_informe_happy_path_candidate_pdf(nombre_archivo,  reporte_registro_cand, reporte_postulacion,
                                             reporte_exp_laboral_cuestionario, reporte_habilidad_profesional,
                                             reporte_habilidad_blanda, reporte_expectativa_salarial,
                                             reporte_condiciones_de_contratacion, reporte_seleccion_de_permisos):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe de la postulacion del candidato")
    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha)
    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la prueba de la postulación de un candidato")
    c.drawString(72, 640, reporte_registro_cand)
    c.drawString(72, 610, reporte_postulacion)
    c.drawString(72, 580, reporte_exp_laboral_cuestionario)
    c.drawString(72, 550, reporte_habilidad_profesional)
    c.drawString(72, 520, reporte_habilidad_blanda)
    c.drawString(72, 490, reporte_expectativa_salarial)
    c.drawString(72, 460, reporte_condiciones_de_contratacion)
    c.drawString(72, 430, reporte_seleccion_de_permisos)

    c.save()


def postulacion_test_candidate():
    try:
        reporte_registro_cand, correo = register_complete_full_cv()
        print(correo)
        _, headers, _ = login_cand(correo, pass_email)
        print('\n')
        reporte_postulacion, postulation_id = postulacion(headers)
        print('\n')
        reporte_exp_laboral_cuestionario = exp_laboral_cuestionario(headers, postulation_id)
        print('\n')
        reporte_habilidad_profesional = habilidad_profesional(headers, postulation_id)
        print('\n')
        reporte_habilidad_blanda = habilidad_blandas(headers, postulation_id)
        print('\n')
        reporte_expectativa_salarial = expectativa_salarial(headers, postulation_id)
        print('\n')
        reporte_condiciones_de_contratacion = condiciones_de_contratacion(headers, postulation_id)
        print('\n')
        reporte_seleccion_de_permisos = seleccion_de_permisos(headers, postulation_id)
        nombre_archivo = "reports/postulacion del candidato  " + fecha + ".pdf"
        generar_informe_happy_path_candidate_pdf(nombre_archivo, reporte_registro_cand, reporte_postulacion,
                                                 reporte_exp_laboral_cuestionario, reporte_habilidad_profesional,
                                                 reporte_habilidad_blanda, reporte_expectativa_salarial,
                                                 reporte_condiciones_de_contratacion, reporte_seleccion_de_permisos)
        print('\nSe genera el reporte con los resultados de la postulación del candidato :)')
        return 'Se genera el reporte con los resultados de la postulación del candidato'
    except Exception as e:
        print('\nNo se genera el reporte con los resultados de la postulación del candidato :(', e)
        return 'No se genera el reporte con los resultados de la postulación del candidato'
