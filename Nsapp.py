import requests
import xmltodict

def station_request():
    Input = input('Voer het station in waar u de vertrektijden van wilt weten: ')
    global api_url
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + Input

def vertrektijden_inlezen(locatie):
    with open('huidige_vertrektijden.xml', 'w') as vertrektijden:
        response = requests.get(api_url, auth=auth_details)
        vertrektijden.write(response.text)

#def station_check():


auth_details = ('mitch.dejong@student.hu.nl', 'PtV3-OziiNaKuf2NRxagb95jlK8WZZx8lcBGHht_GkIJM-n8Md3BTw')

station_request()

response = requests.get(api_url, auth=auth_details)

vertrektijden_inlezen(response)




