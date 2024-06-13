from dotenv import dotenv_values

from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_register_candidate, \
    step_create_pass_candidate, step_permission_candidate, step_phone_candidate, step_resend_code, \
    step_verify_code_cand, step_names_candidate
from src.services.catalogs import data_user

env = dotenv_values("etc/.env")


def register_onboarding_candidate():
    try:
        name, last_name, _, birth_date, _ = data_user(env)

        headers, email_candidate = step_register_candidate()

        print('con el email', email_candidate)

        step_create_pass_candidate(headers)

        step_permission_candidate(headers)

        step_phone_candidate(headers)

        step_resend_code(headers)

        step_verify_code_cand(headers)

        step_names_candidate(headers, name, last_name, birth_date)
        print('\nSe realizo el registro de candidato correctamente :)')
        return 'se realiza el registro de onboarding del candidato', email_candidate
    except Exception as e:
        print('No se realizo el registro de candidato :(\n', e)
        return 'No se realizo el registro de candidato'



