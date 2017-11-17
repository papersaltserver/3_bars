import json
import sys
from math import sqrt


def get_distance_to_bar(point_lon, point_lat, bar_lon, bar_lat):
    distance_to_bar = sqrt((point_lon - bar_lon) ** 2
                           + (point_lat - bar_lat) ** 2)
    return distance_to_bar


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)['features']
    return json_data


def get_biggest_bar(all_bars_data):
    biggest_bar = max(
        all_bars_data,
        key=lambda bar_item: bar_item['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(all_bars_data):
    smallest_bar = min(
        all_bars_data,
        key=lambda bar_item: bar_item['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(all_bars_data, longitude, latitude):
    closest_bar = min(all_bars_data,
                      key=lambda bar_item:
                      get_distance_to_bar(
                          longitude,
                          latitude,
                          bar_item['geometry']['coordinates'][0],
                          bar_item['geometry']['coordinates'][1]))
    return closest_bar


if __name__ == '__main__':
    bars_data = load_data(sys.argv[1])
    user_lon = float(sys.argv[2])
    user_lat = float(sys.argv[3])
    biggest_bar_name = get_biggest_bar(
        bars_data)['properties']['Attributes']['Name']
    print("Самый большой бар: {}".format(biggest_bar_name))
    smallest_bar_name = get_smallest_bar(
        bars_data)['properties']['Attributes']['Name']
    print("Самый маленький бар: {}".format(smallest_bar_name))
    nearest_bar_name = get_closest_bar(
        bars_data, user_lon, user_lat)['properties']['Attributes']['Name']
    print("Ближайший, к указанным координатам, бар: {}".format(nearest_bar_name))
