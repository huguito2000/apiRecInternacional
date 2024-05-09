import random
from objetos.funciones import base, sendPostHeaders, sendPut
#from test.login import login
#respuesta, headers, recruiterID = login()
def sueldoMin():
    sueldoMIN = str(random.randint(200, 25000))
    print(sueldoMIN)
    return sueldoMIN

def sueldoMax():
    sueldoMAX = str(random.randint(25001, 45000))
    print(sueldoMAX)
    return sueldoMAX

def puestos():
    puesto = ['abogado', 'desarrollador', 'medico', 'contador', 'Filósofo', 'Profesor', 'Periodista', 'Enfermero']
    aleatorio = random.choice(puesto)
    print(aleatorio)
    return aleatorio


puesto = puestos()

min: str = sueldoMin()

max: str = sueldoMax()

def vacanteIA(headers):
    try:
        url = 'https://assistant.stage.ia.involverh.es/api/v1/vacancy/'
        myBody = {
            "client": {
                "clientId": "2c9f8a0a8ece6eea018ece9c00a40014",
                "name": "involve",
                "industry": {
                    "industryId": "40288088798a3b0501798a58c52b0055",
                    "name": "Electrónica y electrodomésticos",
                    "sector": {
                        "sectorId": "4028808879868679017986ac3c45000a",
                        "name": "Tecnología y telecomunicaciones"
                    }
                },
                "creationDate": "2024-04-11 19:21:54",
                "typeCompany": {
                    "catalogSystemId": "4028818e8e337efb018e33801eba0007",
                    "name": "Nacional",
                    "type": "typeCompany",
                    "level": None,
                    "status": True
                },
                "employees": "DE51A250",
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
                    "totalCoins": 29,
                    "vacancyApprove": "NEVER",
                    "invoiceNotification": True,
                    "invoiceCounter": None
                },
                "payments": [],
                "isMine": False,
                "isActive": True,
                "pathLogo": "https://s3.eu-south-2.amazonaws.com/es-involve-resources-prod/CLIENT/2c9f8a0a8ece6eea018ece9c00a40014/descarga.png",
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
                "currency": {
                    "currencyId": "2c9f9364867665940186849ddb990011",
                    "codeStripe": "EUR",
                    "description": "Euro",
                    "iconCountry": "https://flagcdn.com/w20/es.png",
                    "symbol": "€"
                },
                "stripeCustomerId": "cus_PuHmWajHZPtjtB",
                "legalId": "A123456789999",
                "legalName": "sdasdasdad",
                "address": "asdsadasasd",
                "zipCode": "44444"
            },
            "typeSalary": {
                "catalogSystemId": "4028818e8e337efb018e33800d190102",
                "name": "Neto",
                "type": "typeSalary",
                "level": None,
                "status": True
            },
            "periodicitySalary": {
                "catalogSystemId": "4028818e8e337efb018e33801b680005",
                "name": "Mes",
                "type": "periodicitySalary",
                "level": None,
                "status": True
            },
            "commissions": False,
            "confidential": False,
            "salaryShow": True,
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
            "peopleCharge": 0,
            "currency": {
                "currencyId": "2c9f9364867665940186849ddb990011",
                "codeStripe": "EUR",
                "description": "Euro",
                "iconCountry": "https://flagcdn.com/w20/es.png",
                "symbol": "€"
            },
            "salaryMaximum": max,
            "salaryMinimum": min,
            "salaryExactly": None,
            "position": {
                "position": puesto
            }
        }
        resultado = sendPostHeaders(url, headers, myBody, 200)
        vacantId = resultado['vacantId']
        print('Se creo la vacante con IA')
        return 'Se creo la vacante con IA', vacantId
    except Exception as e:
        print('No se creo la vacante con IA', e)
        return 'No se creo la vacante con IA'



def publicarIA(headers):
    try:
        resultado, vacantId = vacanteIA(headers)
        url = base + 'vacancy/management/actived?vacantId=' + vacantId +'&approved=false'
        sendPut(url, headers, 200)
        print('Se publico la vacante con IA')
        return 'Se publico la vacante con IA'
    except Exception as e:
        print('No se publico la vacante con IA', e)
        return 'No se publico la vacante con IA'


