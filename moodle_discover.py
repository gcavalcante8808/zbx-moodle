#!/usr/bin/env python

# This Module allow zabbix and other solutions to inspect
# moodle api.
import requests
import argparse
import json
import pdb

def inspect_ws(**kwargs):
    # Get Params and try to pick a result from the server.
    server = kwargs.pop('server')
    token = kwargs.pop('token')
    ssl = kwargs.pop('ssl')

    if ssl:
       prefix = 'https://'
    else:
       prefix = 'http://'
    
    wsdata = { 'moodlewsrestformat': 'json',
               'wsfunction': 'core_course_get_courses',
               'wstoken': token
    }


    result = requests.post(url=prefix+server+'/webservice/rest/server.php',
                           data=wsdata).json()
#    pdb.set_trace()
    courses = [ {'#MDLCOURSENAME': course['shortname'], 
                '#MDLCOURSEID': course['id'] } for course in result ]

    
    print(json.dumps({'data': courses}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', type=str, required=True)
    parser.add_argument('--token', type=str, required=True)
    parser.add_argument('--ssl', type=bool, required=False, default=False)

    args = parser.parse_args()

    inspect_ws(server=args.server, token=args.token,
               ssl=args.ssl)

