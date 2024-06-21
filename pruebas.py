from src.modules.Candidate.my_data_profile import my_data_profile
from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.modules.Candidate.registro_de_candidato_full_CV import register_complete_full_cv
from src.modules.Candidate.settings_candidate import settings_candidate
from src.modules.recruiter.login_recruiter import login_recruiter, pass_email
from src.modules.recruiter.profile_recruiter import new_client
from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_create_pass_candidate, \
    step_register_candidate
from src.objectRepository.recruiter.ajustesReclu.step_clients import step_new_client
from src.objectRepository.recruiter.stepj_login_recruiter import step_login_recruiter
from src.test.create_report_candidate.create_graphs import all_report_graphs, report_graphs_complete

#all_report_graphs()
#register_onboarding_candidate()
#register_complete_full_cv()

#report_graphs_complete()

email = "huguito.reclutador.es@yopmail.com"
for i in range(11):
    _, headers, recruiter = login_recruiter(email)
    step_new_client(headers)







