from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_register_candidate, \
    step_create_pass_candidate, step_permission_candidate, step_phone_candidate, step_resend_code, \
    step_verify_code_cand, step_names_candidate
from src.services.catalogs import data_user


def register_onboarding_candidate(enviroment):
    try:
        name, last_name, _, birth_date, _ = data_user(enviroment)

        headers, email_candidate = step_register_candidate()
        print('se manda registroCand')
        print(email_candidate)

        step_create_pass_candidate(headers)
        print("se manda la contraseña")

        step_permission_candidate(headers)
        print('se mandan los legales')

        step_phone_candidate(headers)
        print('se manda telefono')

        step_resend_code(headers)
        print('volver a pedir mensaje')

        step_verify_code_cand(headers)
        print('se verifica el codigo correcto')

        step_names_candidate(headers, name, last_name, birth_date)
        print("se mandan los nombres")
        print('\nSe realizo el registro de candidato correctamente')
        return 'se realiza el registro de onboarding del candidato', email_candidate
    except Exception as e:
        print('No se realizo el registro de candidato', e)
        return 'No se realizo el registro de candidato '



