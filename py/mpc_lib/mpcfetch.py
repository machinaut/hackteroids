import requests
import yaml
import ephem
from math import cos, sin, atan, sqrt, atan2

URL = 'http://mpcdb1.cfa.harvard.edu/ws/search'


def get(params):
    r = requests.post(URL, params, auth=('mpc_ws', 'mpc!!ws'))
    data = yaml.load(r.content)
    return data

def load_dataset(filename):
    database = []
    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith('#'):
                database.append(line)
    return database

def read_db(dataline):
    return ephem.readdb(dataline)

def get_body(properties):
    print properties['period']

    entry = "{0},{1},{2},166.2194,128.8232,242.5695,0.0002609,0.99705756,0.0000,04/13.2508/2003,2000,g  6.5,4.0".format(
        properties['designation'],
        'e',
        )

    print entry
    yh = ephem.readdb(entry)
    yh.compute('2003/4/11')
    print("%s %s" % (yh.ra, yh.dec))


def get_xzy(ast):
        ast_z = sin(ast.hlat)*ast.sun_distance
        ast_r = cos(ast.hlat)*ast.sun_distance
        ast_x = cos(ast.hlong)*ast_r
        ast_y = sin(ast.hlong)*ast_r

        return (ast_x, ast_y, ast_z)

def get_relative_pos(earth, ast):
    rel = (ast[0]-earth[0], ast[1]-earth[1], ast[2]-earth[2])
    long = atan2(rel[1], rel[0])
    r= sqrt(rel[0]*rel[0]+rel[1]*rel[1])
    lat = atan2(rel[2], r)
    return {'lat': lat, 'long': long}






