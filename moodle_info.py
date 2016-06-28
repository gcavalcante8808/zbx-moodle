#!/usr/bin/env python

# This Module allow zabbix and other solutions to inspect
# moodle api.
import requests
import argparse
import pdb

def get_nested_elements(info, elements):
    # Function to traverse dictionaries and print when value is 
    # not a dict (instead it's a str)
    if isinstance(elements, str):
        keys = elements.split('.')

    if isinstance(info, dict) and len(keys) > 1:
        keys.pop(0)
        for key in keys:
            value = info[key]
            if isinstance(value, dict):
                keys.pop(0)
                if keys:
                    get_nested_elements(value, keys)
            elif value:
                print(value)
            else:
                return('Not Encountered Value')
    else:
        print(info)

def inspect_ws(**kwargs):
    # Get Params and try to pick a result from the server.
    server = kwargs.pop('server')
    token = kwargs.pop('token')
    function = kwargs.pop('function')
    data = kwargs.pop('data')
    ssl = kwargs.pop('ssl')

    if ssl:
       prefix = 'https://'
    else:
       prefix = 'http://'
    
    wsdata = { 'moodlewsrestformat': 'json',
               'wsfunction': function.split('.')[0],
               'wstoken': token
    }

    if data:
        wsdata += data

    result = requests.post(url=prefix+server+'/webservice/rest/server.php',
                           data=wsdata).json()

    if isinstance(result, dict) and 'errorcode' not in result.keys():
       get_nested_elements(result, function)
    elif isinstance(result, str) or isinstance(result, int):
       print(result)
    elif isinstance(result,list):
       for value in result:
           get_nested_elements(value, function)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', type=str, required=True)
    parser.add_argument('--token', type=str, required=True)
    parser.add_argument('--function', type=str, required=True)
    parser.add_argument('--data', type=dict, required=False)
    parser.add_argument('--ssl', type=bool, required=False, default=False)

    args = parser.parse_args()

    inspect_ws(server=args.server, token=args.token,
               function=args.function, data=args.data, 
               ssl=args.ssl)

