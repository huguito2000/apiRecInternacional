# Proximamente
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.createPassInvalido import \
    create_pass_invalido_cand
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.legalesInvalido import \
    step_send_all_combinations
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.loginNoValido import \
    login_no_valido_cand, \
    login_cand_bloqueado
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.namesInvalidos import \
    step_names_invalid_cand
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.registro_invalido import \
    register_invalid_candidate
from src.objectRepository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.telefonoNoValido import \
    step_tel_invalido_cand, step_verify_code_invalido_cand

def candidate_data_invalid():
    try:
        login_no_valido_cand()
        login_cand_bloqueado()
        _, headers, _ = register_invalid_candidate()
        create_pass_invalido_cand(headers)
        step_send_all_combinations(headers)
        step_tel_invalido_cand(headers)
        step_verify_code_invalido_cand(headers)
        step_names_invalid_cand(headers)
        print('Se manda las pruebas de candidato con datos invalidos')
        return 'Se manda las pruebas de candidato con datos invalidos'
    except Exception as e:
        print('No pasaron los datos invalidos del candidato', e)
        return 'No pasaron los datos invalidos del candidato'
