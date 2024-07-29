from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.modules.Candidate.loginCand import login_cand
from src.object_repository.candidate.busqueda.busquedaDeVacantes import step_search_position, step_search_salary, \
    step_search_workday, step_search_modality, step_search_type_contract, step_search_type_company, step_search_time
from src.object_repository.candidate.obj_loginCand import email_candidate, pass_email
from src.services.catalogs import obtener_fecha

fecha = obtener_fecha()


def generar_informe_buscador_candidate_pdf(nombre_archivo, reporte_posicion, reporte_salario, reporte_jornada,
                                           reporte_modalidad, reporte_tipo_contrato, reporte_tipo_compania,
                                           reporte_fecha):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe del buscador de vacantes")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha)

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en el buscador de vacantes")
    c.drawString(72, 640, reporte_posicion)
    c.drawString(72, 610, reporte_salario)
    c.drawString(72, 580, reporte_jornada)
    c.drawString(72, 550, reporte_modalidad)
    c.drawString(72, 520, reporte_tipo_contrato)
    c.drawString(72, 490, reporte_tipo_compania)
    c.drawString(72, 460, reporte_fecha)
    c.save()


def buscador_test_candidate():
    try:
        nombre_archivo = "reports/Buscador candidato " + fecha + ".pdf"
        _, headers, _ = login_cand(email_candidate, pass_email)
        reporte_posicion = step_search_position(headers)
        reporte_salario = step_search_salary(headers)
        reporte_jornada = step_search_workday(headers)
        reprote_modalidad = step_search_modality(headers)
        reporte_tipo_contrato = step_search_type_contract(headers)
        reporte_tipo_compania = step_search_type_company(headers)
        reporte_fecha = step_search_time(headers)
        generar_informe_buscador_candidate_pdf(nombre_archivo, reporte_posicion, reporte_salario, reporte_jornada,
                                               reprote_modalidad, reporte_tipo_contrato, reporte_tipo_compania,
                                               reporte_fecha)
        print('Se genera el reporte con los resultados del buscador:) \n')
        return 'Se hizo correctamente el buscador'
    except Exception as e:
        print('No se paso buscador del candidato :( \n', e)
        return 'No se realizo pruebas del buscador'
