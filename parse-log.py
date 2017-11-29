#!/usr//bin/python3.4

"""
 This is code to parse a json file and manipulate the data using nested distionaries

 The example here calculates the success rate for each application/version combo in the original status.txt file
"""

"""
 Needed libraries.   
 opening files, reading json, validating json, logging
"""
import json
import jsonschema
from jsonschema import validate
from pprint import pprint
import logging

"""
 Set debug level
"""
logging.basicConfig(filename='parser.log',level=logging.INFO)
logger = logging.getLogger(__name__)

"""
 Grab schema once
"""
schema = open("schema.json").read()
myschema =  json.loads(schema)

"""
 initialize dict that will be used for output 
"""
Combined_data = {}

"""
 Grab each line of json
 validate it
 parse it
 calculate success rate
"""
with open('status.txt', "r") as data_file:    
    data = json.load(data_file)
    logger.debug( data )

    for item in data:
        try:
             validate(item,myschema)
        except jsonschema.ValidationError as e:
             logger.error("Validation error", e.message)
        except jsonschema.SchemaError as e:
             logger.error("Schema error", e)
        app = item.get("Application")
        logger.debug(app)
        ver = item.get("Version")
        logger.debug(ver)
        if app not in Combined_data:
             Combined_data[app] = {}
        if ver not in Combined_data[app]:
             Combined_data[app][ver] = {'reqs': 0, 'succ': 0, 'success_rate': 0}

        Combined_data[app][ver]['reqs'] += int(item.get("Request_Count"))
        Combined_data[app][ver]['succ'] += int(item.get("Success_Count"))
        if  Combined_data[app][ver]['reqs'] > 0:
             Combined_data[app][ver]['success_rate'] = Combined_data[app][ver]['succ']/Combined_data[app][ver]['reqs']
        else:
             Combined_data[app][ver]['success_rate'] = 0

"""
 When done print human readable standard out ; computer parsable to output.txt
"""
pprint(Combined_data)
with open('output.txt', 'w') as f:
    json.dump(Combined_data, f, ensure_ascii=False)

