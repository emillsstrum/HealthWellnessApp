import json
import os
from services.health_data import *

def write_out_json():
    # get Day objects in health_data{}, convert to list of dictionaries, write to json file
    json_data = [day.to_dict() for day in health_data.values()] # get list of dictionaries

    with open('health_data.json', 'w') as file: # write data to json file
        json.dump(json_data, file, indent=4)


