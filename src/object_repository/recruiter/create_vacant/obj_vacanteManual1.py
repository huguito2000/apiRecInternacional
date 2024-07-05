from src.object_repository.recruiter.ajustesReclu.step_clients import get_client
from src.services.catalogs import position, salary_min, salary_max, env
from src.services.peticiones_HTTP import send_post_headers


def position_title(headers):
    try:
        print('Inicia la creacion de la vacante')
        client_id = get_client(headers)

        puesto = position()

        minimo: str = salary_min()

        maximo: str = salary_max()
        url = env["URL_SERVER"] + 'vacancy/management'
        print('la url es:', url)
        my_body = {
            "specialty": "automatizado",
            "client": {
                "clientId": client_id,
                "name": "hugo",
                "industry": {
                    "industryId": "40288088798a3b0501798a4fd00b001b",
                    "name": "Aeroespacial",
                    "sector": {
                        "sectorId": "4028808879868679017986ac352d0004",
                        "name": "Industrial"
                    }
                },
                "creationDate": "2024-04-11 19:48:58",
                "typeCompany": {
                    "catalogSystemId": "4028818e8e337efb018e3380223e0008",
                    "name": "Internacional / Transnacional",
                    "type": "typeCompany",
                    "level": None,
                    "status": True
                },
                "employees": "DE11A50",
                "company": {
                    "companyId": "2c9f8a0a8ece6eea018ece999b5f0008",
                    "name": "involver",
                    "businessName": "Lucio",
                    "rfc": None,
                    "pathLogo": "https://s3.eu-south-2.amazonaws.com/es-involve-resources-prod/COMPANY/2c9f8a0a8ece6eea018ece999b5f0008/BUSSINES_LOGO_jpeg",
                    "industry": {
                        "industryId": "40288088798a3b0501798a58ca500059",
                        "name": "Software",
                        "sector": {
                            "sectorId": "4028808879868679017986ac3c45000a",
                            "name": "Tecnología y telecomunicaciones"
                        }
                    },
                    "typeCompany": {
                        "catalogSystemId": "4028818e8e337efb018e33801eba0007",
                        "name": "Nacional",
                        "type": "typeCompany",
                        "level": None,
                        "status": True
                    },
                    "companySize": "DE51A250",
                    "country": {
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
                    },
                    "colorTextButton": None,
                    "colorText": None,
                    "pathLogoEmail": "https://involve-resources.s3.amazonaws.com/res-involve/company-avatar.png",
                    "colorButton": None,
                    "website": None,
                    "description": None,
                    "totalCoins": 30,
                    "vacancyApprove": "NEVER",
                    "invoiceNotification": True,
                    "invoiceCounter": None
                },
                "payments": [],
                "isMine": False,
                "isActive": True,
                "pathLogo": "https://s3.eu-south-2.amazonaws.com/es-involve-resources-prod/CLIENT/2c9f8a0a8ece6eea018eceb4c94d0054/descarga.png",
                "country": {
                    "countryId": "ff8080818ec330e3018ec87ca55f00cf",
                    "capital": "Bogotá",
                    "currency": "COP",
                    "currencySymbol": "$",
                    "iso2": "CO",
                    "iso3": "COL",
                    "latitude": 4.570868,
                    "longitude": -74.297333,
                    "name": "Colombia",
                    "nameNative": "Colombia",
                    "phoneCode": "+57",
                    "region": "Americas",
                    "subregion": "South America",
                    "tld": ".co",
                    "flagCountry": "https://flagcdn.com/w20/co.png"
                },
                "currency": {
                    "currencyId": "2c9f9364867665940186849ddb990012",
                    "codeStripe": "USD",
                    "description": "Dólar",
                    "iconCountry": "https://flagcdn.com/w20/us.png",
                    "symbol": "$"
                },
                "stripeCustomerId": "cus_Pwshh0g63DyLpN",
                "legalId": None,
                "legalName": "hugo",
                "address": "dsdad",
                "zipCode": "56615"
            },
            "typeSalary": {
                "catalogSystemId": "4028818e8e337efb018e33800d190102",
                "name": "Neto",
                "type": "typeSalary",
                "level": None,
                "status": True
            },
            "periodicitySalary": {
                "catalogSystemId": "4028818e8e337efb018e338018c20004",
                "name": "Quincena",
                "type": "periodicitySalary",
                "level": None,
                "status": True
            },
            "currency": {
                "currencyId": "2c9f9364867665940186849ddb990011",
                "codeStripe": "EUR",
                "description": "Euro",
                "iconCountry": "https://flagcdn.com/w20/es.png",
                "symbol": "€"
            },
            "commissions": False,
            "confidential": False,
            "salaryShow": True,
            "benefitsInvolve": [
                {
                    "benefitId": "ff8081817b837f74017b838928f60010"
                }
            ],
            "vacancyOrigin": "MANUAL",
            "city": {
                "cityId": "2c9f936481969f0cccc996a00e092521",
                "name": "Provincia de Madrid",
                "stateCode": "ES-MD",
                "countryCode": "ES",
                "latitude": 40.40225,
                "longitude": -3.71029,
                "state": {
                    "stateId": "2c9f936481969f0bbbb996a00e090048",
                    "name": "Comunidad de Madrid",
                    "countryCode": "ES",
                    "fipsCode": "29",
                    "iso2": "ES-MD",
                    "latitude": 40.42526,
                    "longitude": -3.69063,
                    "country": {
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
            },
            "modality": {
                "catalogSystemId": "4028818e8e337efb018e3380476c0016",
                "name": "Hibrido",
                "type": "modalityWork",
                "level": None,
                "status": True
            },
            "salaryMaximum": maximo,
            "salaryMinimum": minimo,
            "salaryExactly": None,
            "position": {
                "position": puesto
            }
        }

        resultado = send_post_headers(url, headers, my_body, 200)
        if resultado != 0:
            vacant_id = resultado['vacantId']
            print('Se creo el titulo de vacante :) \n')
            return 'Se creo el titulo de vacante', vacant_id, 1
        else:
            print('No se creo el titulo de la vacante :(\n')
            return 'No se creo el titulo de la vacante :(', 0
    except Exception as e:
        print('No se crea el primer paso :(\n', e)
        return 'No se crea el primer paso', 0
