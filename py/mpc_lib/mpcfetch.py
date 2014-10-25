import requests
import yaml

URL = 'http://mpcdb1.cfa.harvard.edu/ws/search'


def get(params):
    r = requests.post(URL, params, auth=('mpc_ws', 'mpc!!ws'))
    data = yaml.load(r.content)
    return data






