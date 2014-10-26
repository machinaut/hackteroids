__author__ = 'Joe'
import mpcfetch
import json
import ephem
from datetime import timedelta
from datetime import datetime
from math import cos, sin


data_output = []

timestep = timedelta(days=10)
max_ast = 6
enddate = datetime(2015, 1, 1, 0, 0, 0)
earth = ephem.Mars()


pi = 3.14159
rad2deg = 180/pi


raw = mpcfetch.load_dataset('Soft03CritList.txt')
if len(raw) > max_ast:
    raw = raw[:max_ast]

for raw_entry in raw:
    crit, raw_entry = raw_entry.split(' ', 1)
    ast = mpcfetch.read_db(raw_entry)
    print ast.name
    date = datetime(2013, 1, 1, 0, 0, 0)
    pos = []
    while date < enddate:
        date += timestep
        ast.compute(date.strftime('%Y/%m/%d'))
        earth.compute(date.strftime('%Y/%m/%d'))

        ast_pos = mpcfetch.get_xzy(ast)
        earth_pos = mpcfetch.get_xzy(earth)
        earth_pos = mpcfetch.get_relative_pos(earth_pos, ast_pos)
        print earth_pos

        pos.append({'date': date.strftime('%Y-%m-%d'), 'lat': earth_pos['lat']*rad2deg, 'lon': earth_pos['long']*rad2deg, 'alt': ast.earth_distance})

    entry = {'name': ast.name, 'pos': pos, 'crit': crit}
    data_output.append(entry)

with open('Soft03CritList_earth.js', 'w') as outfile:
    outfile.write('var data=')
    json.dump(data_output, outfile)
    outfile.write(';')
