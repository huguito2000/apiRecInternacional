from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.services.catalogs import obtener_fecha, data_user, env
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.createPassInvalido import \
    create_pass_invalido_cand
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.legalesInvalido import \
    step_send_all_combinations_legals
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.loginNoValido import \
    login_no_valido_cand, login_cand_bloqueado
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.namesInvalidos import \
    step_names_invalid_cand
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.registro_invalido import \
    register_invalid_candidate
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.telefonoNoValido import \
    step_phone_invalid_candidate, step_verify_code_invalido_cand


fecha = str(obtener_fecha())


def generar_informe_con_datos_no_validos_pdf(nombre_archivo, reporte_login_no_valido_cand,
                                             reporte_login_cand_bloqueado, reporte_register_invalid_candidate,
                                             reporte_create_pass_invalido_cand,
                                             reporte_step_send_all_combinations_legals,
                                             reporte_step_phone_invalid_candidate,
                                             reporte_step_verify_code_invalido_cand, reporte_step_names_invalid_cand):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(72, 750, "Informe de pruebas con datos no validos")

    c.setFont('Helvetica', 12)
    c.drawString(72, 720, "Fecha: " + fecha)

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de las pruebas con datos no validos del candidato")
    c.drawString(72, 640, reporte_login_no_valido_cand)
    c.drawString(72, 610, reporte_login_cand_bloqueado)
    c.drawString(72, 580, reporte_register_invalid_candidate)
    c.drawString(72, 550, reporte_create_pass_invalido_cand)
    c.drawString(72, 520, reporte_step_send_all_combinations_legals)
    c.drawString(72, 490, reporte_step_phone_invalid_candidate)
    c.drawString(72, 460, reporte_step_verify_code_invalido_cand)
    c.drawString(72, 430, reporte_step_names_invalid_cand)

    c.save()


def data_no_valid_candidate():
    try:
        name, last_name, _, birth_date, _ = data_user(env)
        reporte_login_no_valido_cand = login_no_valido_cand()

        print('\nPruebas de un candidato bloqueadon y desbloqueado')
        reporte_login_cand_bloqueado = login_cand_bloqueado()

        print('\nInicia el proseso de registro de un candidato con datos incorrectos')
        reporte_register_invalid_candidate, headers, email_candidate = register_invalid_candidate()

        print('\nInicia el registro con la contraseña invalida del candidato', email_candidate)
        reporte_create_pass_invalido_cand = create_pass_invalido_cand(headers)

        print('\nSe envia todas las conbinaciones de las notificaciones')
        reporte_step_send_all_combinations_legals = step_send_all_combinations_legals(headers)

        print('\nInica el registro de telefonos incorrectos')
        reporte_step_phone_invalid_candidate, _ = step_phone_invalid_candidate(headers)

        print('\nSe inicia el envio de codigos incorrectos')
        reporte_step_verify_code_invalido_cand = step_verify_code_invalido_cand(headers)

        print('\n Inicia el envio del formulario de onboarding')
        reporte_step_names_invalid_cand = step_names_invalid_cand(headers, name, last_name, birth_date)
        nombre_archivo = "reports/ Registro de pruebas datos no validos " + fecha + ".pdf"

        generar_informe_con_datos_no_validos_pdf(nombre_archivo, reporte_login_no_valido_cand,
                                                 reporte_login_cand_bloqueado, reporte_register_invalid_candidate,
                                                 reporte_create_pass_invalido_cand,
                                                 reporte_step_send_all_combinations_legals,
                                                 reporte_step_phone_invalid_candidate,
                                                 reporte_step_verify_code_invalido_cand,
                                                 reporte_step_names_invalid_cand)
        print('Se genera el reporte con los resultados con datos no validos')
        return 'Se hizo el reporte de los datos incorrectos'
    except Exception as e:
        print('No se hizo el reporte de datos incorrectos', e)
        return 'No se hizo el reporte de datos incorrectos'

