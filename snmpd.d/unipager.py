#!/usr/bin/env python3
import requests
import argparse
import json

parser = argparse.ArgumentParser(description='Get Unipager JSON Status as SNMP')
parser.add_argument('--oid',
                    help='The OID to give out')
parser.add_argument('--value',
                    help='The JSON describer of the value to give out')
parser.add_argument('--datatype',
                    help='The Datatype of the SNMP answer to give out')

args = parser.parse_args()

oid = args.oid
value = args.value
datatype = args.datatype

response = requests.get('http://localhost:8073/status')
data = response.json()
print ("%s\n%s\n%s" %(oid, datatype, data[value]))
