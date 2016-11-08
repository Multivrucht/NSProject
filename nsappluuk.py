import xmltodict
import requests

auth_details = ('mitch.dejong@student.hu.nl','PtV3-OziiNaKuf2NRxagb95jlK8WZZx8lcBGHht_GkIJM-n8Md3BTw')

def station_request():
    Input = input('Voer het station in waar u de vertrektijden van wilt weten: ')
    global api_url
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + Input

def vertrektijden_inlezen(locatie):
    with open('huidige_vertrektijden.xml', 'w') as vertrektijden:
        response = requests.get(api_url, auth=auth_details)
        vertrektijden.write(response.text)

def inlezen_xml(filename):
    with open(filename) as treinritten:
        treinritten = treinritten.read()
        treinritten = xmltodict.parse(treinritten)
        rittenDict = treinritten['ActueleVertrekTijden']['VertrekkendeTrein']
        print('{} - {}'.format(' Tijd', 'eindbestemming'))
        for rit in rittenDict:
            vertrektijd = rit['VertrekTijd'].split('T')
            vertrektijd = vertrektijd[1].split(':')
            print('{}:{} - {}'.format(vertrektijd[0], vertrektijd[1], rit['EindBestemming']))

def station_check():
    station_api = 'http://webservices.ns.nl/ns-api-stations-v2'
    srequest = requests.get(station_api,  auth=auth_details)
    with open('alle_stations.xml', 'w', encoding='utf-8') as stations:
        stations.write(srequest.text)
    with open('alle_stations.xml', 'r') as alle_stations:
        alle_stations = alle_stations.read()
        alle_stations = xmltodict.parse(alle_stations)
        stationsDict = alle_stations['Stations']['Station']
        stationLijst = []
        for station in stationsDict:
            stationLijst.append(station['Namen']['Kort'])
            stationLijst.append(station['Namen']['Middel'])
            stationLijst.append(station['Namen']['Lang'])
    while True:
        Input = input('Voer het station in waar u de vertrektijden van wilt weten: ')
        if Input not in stationLijst:
            print('Dit is geen geldig station. Voer een geldig station in')
        else:
            return Input
            break



#station_check()
station_request()
vertrektijden_inlezen(api_url)
inlezen_xml('huidige_vertrektijden.xml')
