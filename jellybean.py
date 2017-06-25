from bart_api import BartApi
from requests import get
import datetime
import os
import time

AC_TRANSIT_TOKEN = "token"
STOP_IDS = {'52': '57300', 'F': '57776', '51B': '55999'}
BART_STATION_KEY = 'DBRK'


def bart_info():
    """
    Returns a dictionary that maps trainline to color and departure times.

    e.g. {'Warm Spring': ('#ff9933', ['6', '26'])}
    """
    bart_station = BartApi().etd(BART_STATION_KEY)
    result = {}

    for train_line in bart_station:
        destination = train_line['destination']
        color = train_line['estimates'][0]['hexcolor']
        departure_info = [(train['minutes'], train['length']) for train in train_line['estimates']][0:2]
        value = (color, departure_info)
        result[destination] = value

    return result


def bus_info():
    stop_id = '51B'
    request_url = 'http://api.actransit.org/transit/stops/' + STOP_IDS[stop_id] + '/predictions/?token=' + AC_TRANSIT_TOKEN
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
    print(bart_info())
