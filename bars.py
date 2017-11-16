import json
import sys
from math import sqrt


def get_distance_to_bar(user_lon, user_lat, bar_lon, bar_lat):
    distance_to_bar = sqrt((user_lon-bar_lon)**2+(user_lat-bar_lat)**2)
    return distance_to_bar

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)['features']
    return json_data


def get_biggest_bar(json_bar_data):
    biggest_bar = max(json_bar_data, key = lambda bar_item: bar_item['properties']['Attributes']['SeatsCount'])
    return biggest_bar['properties']['Attributes']['Name']


def get_smallest_bar(json_bar_data):
    smallest_bar = min(json_bar_data, key = lambda bar_item: bar_item['properties']['Attributes']['SeatsCount'])
    return smallest_bar['properties']['Attributes']['Name']


def get_closest_bar(json_bar_data, longitude, latitude):
    closest_bar = min(json_bar_data, key = lambda bar_item:
                        get_distance_to_bar(longitude,
                                            latitude,
                                            bar_item['geometry']['coordinates'][0],
                                            bar_item['geometry']['coordinates'][1]))
    return closest_bar['properties']['Attributes']['Name']


if __name__ == '__main__':
    json_data = load_data(sys.argv[1])
    user_lon = float(sys.argv[2])
    user_lat = float(sys.argv[3])
    print("Самый большой бар: {}".format(get_biggest_bar(json_data)))
    print("Самый маленький бар: {}".format(get_smallest_bar(json_data)))
    print("Ближайший, к указанным координатам, бар: {}".format(get_closest_bar(json_data, user_lon, user_lat)))
