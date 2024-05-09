from objetos.funciones import sendPatch, base
from test.login import login

#respuesta, headers, recruiterID = login()
def paso2(vacantId, headers):
    try:
        url = base + 'vacancy/management/' + vacantId
        print(url)
        mybody = [
          {
            "op": "replace",
            "path": "/mission",
            "value": "se prueba los objetivos del puesto"
          },
          {
            "op": "replace",
            "path": "/functions",
            "value": "* prueba de las funciones"
          },
          {
            "op": "replace",
            "path": "/typePositionId",
            "value": "40288086796be11e01796c18ec210069"
          },
          {
            "op": "replace",
            "path": "/contractId",
            "value": "4028818e8e3e1d59018e3e20928c0002"
          },
          {
            "op": "replace",
            "path": "/peopleCharge",
            "value": "1"
          },
          {
            "op": "replace",
            "path": "/schedule",
            "value": "8:00 a 17:00"
          },
          {
            "op": "replace",
            "path": "/allNationality",
            "value": "true"
          },
          {
            "op": "replace",
            "path": "/workingDay",
            "value": {
              "catalogSystemId": "4028818e8e337efb018e33804ce40018",
              "name": "De lunes a viernes",
              "type": "workingDay",
              "level": None,
              "status": True
            }
          },
          {
            "op": "replace",
            "path": "/contractCountry",
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
          },
          {
            "op": "replace",
            "path": "/steps",
            "value": "2"
          }
        ]
        sendPatch(url, headers, mybody, 200)
        print('\n Se hizo el segundo paso de la creación de la vacante')
        return 'Se hizo el segundo paso de la creación de la vacante'
    except Exception as e:
        print('No se hizo el segundo paso de la creación de la vacante', e)
        return 'No se hizo el segundo paso de la creación de la vacante'




