__author__ = 'Joe'
import mpcfetch
import json
from datetime import timedelta
from datetime import datetime


data_output = []

timestep = timedelta(days=10)
enddate = datetime(2015, 1, 1, 0, 0, 0)
pi = 3.14159
rad2deg = 180/pi

raw = mpcfetch.load_dataset('Soft03CritList.txt')
print len(raw)
for raw_entry in raw:
    ast = mpcfetch.read_db(raw_entry)
    print ast.name

    date = datetime(2005, 1, 1, 0, 0, 0)
    pos = []
    while date < enddate:
        date += timestep
        ast.compute(date.strftime('%Y/%m/%d'))
        pos.append({'date': date.strftime('%Y-%m-%d'), 'lat': ast.hlat*rad2deg, 'lon': ast.hlong*rad2deg, 'altitude': ast.earth_distance})

    entry = {'name': ast.name, 'pos': pos}
    data_output.append(entry)

with open('Soft03CritList.json', 'w') as outfile:
    json.dump(data_output, outfile)

# ast.compute('2003/4/11')
# print("%s %s" % (ast.ra, ast.dec))
#
# ast.compute('2004/4/11')
# print("%s %s" % (ast.ra, ast.dec))
# print dir(ast)
# print ast.earth_distance
# print ast.hlat
# print ast.hlong