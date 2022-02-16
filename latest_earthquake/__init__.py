"""
Date: 13 Februari 2022
Time: 17:12:16 WIB
Magnitude: 5.0
Depth: 10 km
Location:
    Lat=5.94 LU - Long=125.59 BT
Center: 247 km BaratLaut MELONGUANE-SULUT
Descripition: tidak berpotensi TSUNAMI
"""
import requests
import latest_earthquake
from bs4 import BeautifulSoup


def data_extraction():
    try:
        content = requests.get('https://www.bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        print(content.text)
    #    soup = BeautifulSoup(content)
        result_data = dict()
        result_data['date'] = '13 February 2022'
        result_data['time'] = '17:12:16 WIB'
        result_data['mag'] = 5.0
        result_data['location'] = {
            'lat': 5.94, 'long': 125.59
        }
        result_data['center'] = '247 km Barat Laut MELONGUANE-SULUT'
        result_data['desc'] = 'Tidak berpotensi Tsunami'

        return result_data
    else:
        return None

def show_data(result):
    if result is None:
        print('Cannot find the data')
        return
    print('Source: BMKG.co.id')
    print(f'Date: {result["date"]}')
    print(f'Time: {result["time"]}')
    print(f'Magnitude: {result["mag"]}')
    print(f'Location: lat={result["location"]["lat"]} long={result["location"]["long"]}')
    print(f'Center: {result["center"]}')
    print(f'Description: {result["desc"]}')


if __name__ == '__main__':
    print('Latest Earthquake Detection App')
    result = latest_earthquake.data_extraction()
    latest_earthquake.show_data(result)
