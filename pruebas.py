from src.modules.recruiter.change_cupon import change_cupon_client
from src.modules.recruiter.clients import customer_section
from src.modules.recruiter.create_vacancy_recruiter import create_manual_vacant, create_vacant_ia
from src.modules.recruiter.i_forgot_my_pass_recruiter import i_forgot_pass_my_recruiter
from src.modules.recruiter.login_recruiter import login_recruiter, email, pass_email
from src.modules.recruiter.register_recruiter import register_recruiter
from src.modules.recruiter.settings_recruiter import settings
from src.object_repository.recruiter.ajustesReclu.step_recruiting_team import recruiting_team

from src.object_repository.recruiter.step_i_forgot_pass_recruiter import i_forgot_password_recruiter, \
    confirm_restore_pass_recruiter
from src.services.catalogs import generate_report_graphs, obtener_fecha, env
from src.test.create_report_recruiter.create_graphs_recruiter import report_complete_recruiter

fecha = obtener_fecha()
reports = env["DIR_REPORTS"]

report_complete_recruiter()

