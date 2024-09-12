from api import wather_api as wap
from toolz import curry,pipe,partial,reduce
from models import pilot,aircrapt,target
import math
from reposetory import json_reposetory as j_r
api_key = "0dc98b234ef438fbe7ded0743c52cc90"

city_list = [ "Damascus","Beirut", "Amman", "Cairo","Baghdad","Tehran", "Riyadh", "Tripoli", "Ankara", "Khartoum", "Gaza City", "Sanaa", "Manama", "Kuwait City", "Doha"]
request_location =lambda citys_list: pipe(
    citys_list,
    partial(map,lambda x:location_city(x),
            list
    )
)

request_wathers =lambda citys_list: pipe(
    citys_list,
    partial(map,lambda x:wather_city(x),
            list
    )
)
def location_city(city):
    return wap.make_request(f'https://api.openweathermap.org/geo/1.0/direct?q={city}teheran&appid={api_key}')
def wather_city(city):
    return wap.make_request( f'https://api.openweathermap.org/data/2.5/forecast?q={city}yemen&appid={api_key}')
def convert_from_json_to_pilot(json):
    return pilot(name=json["name"],skill=json["skill"])

def convert_from_json_to_aircraft(json):
    return aircrapt(
        type=json["type"],
        speed=json["speed"],
        fuel_capacity=json["fuel_capacity"])

def convert_from_json_to_target(json):
    return target(
        name=json["Target City"],
        priority=json["Priority"],
        let=json["let"],
        lon=json["lon"]
    )
def distances(target_list):
    jerosalem_location =haversine_distance(
        location_city("Jerusalem")[0]["let"],
        location_city("Jerusalem")[0]["lon"])

    distance = pipe(
        target_list,
        partial(map,lambda x: location_city(x)),
        partial(filter,lambda x:x[0]),
        partial(map,lambda x:{f'{x["name"]}':jerosalem_location(x["let"],x["lon"])}),
        dict
    )
    return distance

# Function to calculate the distance between two coordinates using the Haversine formula
@curry
def haversine_distance(lat1, lon1, lat2, lon2):
 r = 6371.0 # Radius of the Earth in kilometers
 # Convert degrees to radians
 lat1_rad = math.radians(lat1)
 lon1_rad = math.radians(lon1)
 lat2_rad = math.radians(lat2)
 lon2_rad = math.radians(lon2)
 # Calculate differences between the coordinates
 dlat = lat2_rad - lat1_rad
 dlon = lon2_rad - lon1_rad
 # Apply Haversine formula
 a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /
2)**2
 c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
 # Calculate the distance
 distance = r * c
 return distance