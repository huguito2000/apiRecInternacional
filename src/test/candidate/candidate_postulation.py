import requests
import json
import random
from json import loads
from dotenv import dotenv_values

env = dotenv_values("etc/.env")

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json'
}

def get_vacancy(vacancy_id):
  response = requests.get(env["URL_SERVER"] + "vacancy/search-vacant/"+vacancy_id)
  vacancy = loads(response.text)
  return vacancy


def addCandidateArea(token, vacancy):
    area = vacancy["areasVacant"][0]["area"]
    speciality = area["specialties"][random.randint(0, len(area["specialties"])-1)]
    area["specialties"] = []
    area["specialties"].append(speciality)
  
    response = requests.post(env["URL_SERVER"] + "user/candidate/area", headers=headers, json=area)

def postulation():
  response = requests.post(
        env["URL_SERVER"] + "/user/candidate/postulation?vacantId="+"f60a3c37-c57f-4838-9663-745900ff8931", headers=headers, json=json_data)

#/user/candidate/postulation/question?page=0&size=100&processId=ccefcbf8-7fd2-4861-8da4-156f8966aadb&questionnaire=AREA_SPECIALTY



'''
/user/candidate/area

[
  {
    "areaId": "402881948dfc3ddd018dfc43ff38019b",
    "name": "Arte y cultura",
    "specialties": [
      {
        "specialtyId": "402881948dfc3ddd018dfc44019d019d",
        "name": "Animación",
        "areaId": "402881948dfc3ddd018dfc43ff38019b"
      }
    ]
  }
]
'''