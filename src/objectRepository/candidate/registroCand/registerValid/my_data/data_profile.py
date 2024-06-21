
from src.objectRepository.candidate.registroCand.registerValid.my_cv.stepCVFull import upload_photo
from src.services.catalogs import foto, subir_archivo, get_area_catalogs, data_user, salary_max, get_ramdom_city, env
from src.services.peticiones_HTTP import send_delete_sin_body, send_post_headers, send_put_body, send_get_headers

phone = env["PHONE_ESP"]
phone2 = env["PHONE_OTHER"]


def delete_photo(headers):
    try:
        print('Inicia la eliminacion de la foto de perfil\n')
        upload_photo(headers)
        url = env["URL_SERVER"] + 'files/upload/delete-file?typeFile=URL_PHOTO'
        resultado = send_delete_sin_body(url, headers, 200)
        if resultado != 0:
            print('se hace la eliminacion de la photo del candidato correctamente\n')
            return 'Se elimina foto de perfil corrrectmaente', 1
        else:
            print('No se pudo elimina la foto de perfil del candidato \n')
            return 'No se elimino la foto de perfil del candidato', 0
    except Exception as e:
        print('No se pudo elimina la foto de perfil del canditato \n', e)
        return 'No se elimino la foto de perfil del candidato', 0


def change_photo_profile(headers):
    try:
        print('Se cambia la foto de perfil del candidato \n')
        url = env["URL_SERVER"] + 'files/upload/uploadFile?typeFile=URL_PHOTO'
        ruta = foto()
        resultado = subir_archivo(ruta, url, headers, 201)
        if resultado != 0:
            print('Se cambia la foto de perfil :)\n', resultado)
            return 'Se cambia la foto de perfil', 1
        else:
            print('No se cambio la foto de perfil :(\n')
            return 'No se cambio la foto de perfil', 0
    except Exception as e:
        print('No se cambio la foto de perfil :(\n', e)
        return 'No se cambio la foto de perfil', 0


def get_profile_search(headers):
    try:
        print('Verifica si hay ofertas de empleo\n')
        url = env["URL_SERVER"] + 'user/candidate/profile-search'
        respuesta = send_get_headers(url, headers, 200)
        if respuesta != 0:
            search_id = respuesta[0]['candidateProfileSearchId']
            print(search_id)
            url = env["URL_SERVER"] + 'user/candidate/profile-search?profileSearchId=' + search_id
            resultado = send_delete_sin_body(url, headers, 200)
            if resultado != 0:
                if resultado != 0:
                    print('Se encontro una oferta pero\n')
                    print('se ya elimino la oferta de empleo\n')
                else:
                    print('No se elimino la oferta\n')
        else:
            print('No hay ofertas de trabajo')
    except Exception as e:
        print('No se pudo hacer la comprobación de las oferta de trabajo\n', e)


def profile_search(headers):
    try:
        print('Inicia ofertas de empleo\n')
        get_profile_search(headers)
        city = get_ramdom_city()
        url = env["URL_SERVER"] + 'user/candidate/profile-search'

        my_body = {
            "city": city,
            "isCompleteRequiment": True
        }
        respuesta = send_post_headers(url, headers, my_body, 201)
        if respuesta != 0:
            search_id = respuesta["candidateProfileSearchId"]
            print('Se agrega ofertas de empleo correctamente\n')
            return 'Sea agrega la oferta de empleo correctamente', search_id, 1
        else:
            print('No se agrego la orferta de empleo\n')
            return 'No se agrego la oferta de empleo', None, 0
    except Exception as e:
        print('No se agrego la orferta de empleo\n', e)
        return 'No se agrego la oferta de empleo', None, 0


def delete_profile_search(headers):
    try:
        print('Se inicia la eliminacion de oferta de trabajo\n')
        _, search_id, _ = profile_search(headers)
        url = env["URL_SERVER"] + 'user/candidate/profile-search?profileSearchId=' + search_id
        resultado = send_delete_sin_body(url, headers, 200)
        if resultado != 0:
            print('Se elimina la oferta de empleo\n')
            return 'Se elimino la oferta de empleo', 1
        else:
            print('No se elimino la oferta\n')
            return 'No se elimino la oferta', 0
    except Exception as e:
        print('No se elimino la oferta\n', e)
        return 'No se elimino la oferta', 0


def change_profile(headers):
    try:
        print('Se inica el cambio en los datos de perfil\n')
        name, last_name, second_last_name, birth_date, _ = data_user(env)
        birth_date = str(birth_date)
        area = get_area_catalogs(headers)
        salary = salary_max()
        url = env["URL_SERVER"] + 'user/candidate/about-me'
        my_body = {
            "name": name,
            "lastName": last_name,
            "secondLastName": second_last_name,
            "dateBirth": birth_date,
            "areaId": area,
            "salary": salary,
            "currencyId": "2c9f9364867665940186849ddb990010",
            "periodicitySalaryId": "4028818e8e337efb018e338018c20004",
            "changeResidence": True,
            "nationalityId": "40288086796ba27001796bbcf9770000",
            "cityResidenceId": "2c9f936481969f0cccc996a00e090001",
            "urlGitHub": "https://github.com/",
            "urlLinkedIn": "https://www.linkedin.com/",
            "urlBehance": "https://www.behance.net/",
            "urlFolder": "www.google.com"
        }
        respuesta = send_put_body(url, headers, my_body, 200)
        if respuesta != 0:
            print(f'paso el cambio de perfil {respuesta} \n')
            return 'Se cambiaron los datos de perfil del candidato', 1
        else:
            print('No se cambiaron los datos del perfil\n')
            return 'No se cambiaron los datos del peril', 0
    except Exception as e:
        print('No se cambiaron los datos del perfil\n', e)
        return 'No se cambiaron los datos del peril', 0

