from bart_api import BartApi
from requests import get
import datetime
import os
import time

TOKEN = "token"
STOP_IDS = {'52':'57300','F':'57776','51B':'55999'}



def bart_info():
    bart = BartApi()
    dbrk = bart.etd("DBRK")
    result = {}

    for x in dbrk:
        destination = x['destination']
        value = (x['estimates'][0]['hexcolor'], [train['minutes'] for train in x['estimates']][0:2])
        result[destination] = value
    return result

def bus_info():
    stop_id = '51B'
    request_url = 'http://api.actransit.org/transit/stops/' + STOP_IDS[stop_id] + '/predictions/?token=' + TOKEN
    response = get(request_url)

    if response.status_code == 404:
        print("NO BUS")
    elif response.status_code == 200:
        json_list = response.json()
        for bus in json_list:
            print("Route Name:" + bus['RouteName'])
            bus_time = datetime.datetime.strptime(bus['PredictedDeparture'], '%Y-%m-%dT%X')
            current_time = datetime.datetime.now()
            time_diff = bus_time - current_time
            print(int(time_diff.seconds/60))

if __name__ == "__main__":
    bart_info()
