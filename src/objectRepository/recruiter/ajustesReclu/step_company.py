from src.services.catalogs import foto, subir_archivo, nombres
from src.services.peticiones_HTTP import base, send_patch


def photo_company(headers):
    try:
        url_foto = base + 'files/upload/bussines-logo?recruiterId=2c9f8a0a8ece6eea018ece999b60000a&type=BUSSINES_LOGO'
        ruta = foto()
        print(ruta)
        subir_archivo(ruta, url_foto, headers, 200)
        print('Se subio la foto de la empresa')
        return 'Se subio corretamente la imagen de la empresa'
    except Exception as e:
        print('no se pudo subir la foto de la empresa', {e})
        return 'no se pudo subir la foto de empresa'


def company(headers):
    try:
        nombre = nombres()
        my_body = [
            {
                "op": "replace",
                "path": "/businessName",
                "value": nombre
            },
            {
                "op": "replace",
                "path": "/companySize",
                "value": "DE51A250"
            },
            {
                "op": "replace",
                "path": "/industry",
                "value": {
                    "industryId": "40288088798a3b0501798a58ca500059",
                    "name": "Software",
                    "sector": {
                        "sectorId": "4028808879868679017986ac3c45000a",
                        "name": "Tecnología y telecomunicaciones"
                    }
                }
            },
            {
                "op": "replace",
                "path": "/typeCompany",
                "value": {
                    "catalogSystemId": "4028818e8e337efb018e33801eba0007",
                    "name": "Nacional",
                    "type": "typeCompany",
                    "level": None,
                    "status": True
                }
            },
            {
                "op": "replace",
                "path": "/country",
                "value": {
                    "countryId": "2c9f936481969f0aaaa996a00e090002",
                    "capital": "Madrid",
                    "currency": "EUR",
                    "currencySymbol": "€",
                    "iso2": "ES",
                    "iso3": "ESP",
                    "latitude": 40.4165,
                    "longitude": -3.70256,
                    "name": "España",
                    "nameNative": "España",
                    "phoneCode": "+34",
                    "region": "Europe",
                    "subregion": "Southern Europe",
                    "tld": ".es",
                    "flagCountry": "https://flagcdn.com/w20/es.png"
                }
            }
        ]
        photo_company(headers)
        url = base + 'user/company'
        send_patch(url, headers, my_body, 200)
        print('\n se hicieron los cambios de la empresa')
        return 'Se hiceiron los cambios de la empresa'
    except Exception as e:
        print('\n no se pudieron subir los cambios de la empresa', {e})
        return 'no se subieron los cambios de la empresa'

