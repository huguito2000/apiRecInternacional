from src.services.catalogs import data_user
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.createPassInvalido import \
    create_pass_invalido_cand
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.legalesInvalido import \
    step_send_all_combinations_legals
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.loginNoValido import \
    login_no_valido_cand, login_cand_bloqueado
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.namesInvalidos import \
    step_names_invalid_cand
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.registro_invalido import \
    register_invalid_candidate
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.telefonoNoValido import \
    step_phone_invalid_candidate, step_verify_code_invalido_cand


def candidate_data_invalid(enviroment):
    try:
        name, last_name, _, birth_date, correo = data_user(enviroment)
        login_no_valido_cand()
        login_cand_bloqueado()
        _, headers, _ = register_invalid_candidate(correo)
        create_pass_invalido_cand(headers)
        step_send_all_combinations_legals(headers)
        step_phone_invalid_candidate(headers)
        step_verify_code_invalido_cand(headers)
        step_names_invalid_cand(headers, name, last_name, birth_date)
        print('Se manda las pruebas de candidato con datos invalidos')
        return 'Se hicieron las pruebas de candidato con datos incorrectos de manera exitosa'
    except Exception as e:
        print('No pasaron los datos invalidos del candidato', e)
        return 'No pasaron las pruebas de los datos invalidos del candidato'
