#### README

Parse-log processes a json file to get the success rate for each application/version

Expected json format is defined in schema.json

#### Requirements
     Uses Python3

     pip install jsonschema
     schema.json 
     parse-log.py
     status.txt (json file parsing)

     Tested on Python 3.4

#### How to modify
     Update the schema.json file with your desired format
     Replace status.txt with your input
     If using different dictionary keys, update parse-log.py accordingly

#### How to Run
     python3.4 parse-log.py [--log=DEBUG]

     Logging uses generic python logger.  

#### Input/Output
     Reads status information from: 
         status.txt

     Writes computer output to: 
         output.txt
         this file will be overwritten each time

     Human readable output is sent to stdout

     Log is:
         parser.log

