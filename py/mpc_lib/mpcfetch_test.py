__author__ = 'Joe'

import unittest
import mpcfetch
# import ephem

class TestSequenceFunctions(unittest.TestCase):

    # def test_shuffle(self):
    #     request = {
    #         'order_by_desc': 'spin_period',
    #         'limit': '10',
    #         'json': '1',
    #     }
    #     ast = mpcfetch.get(request)
    #     print ast[0]
    #
    #
    # def test_Eros(self):
    #     request = {
    #         'name': 'Eros',
    #         'json': '1',
    #     }
    #     ast = mpcfetch.get(request)
    #     print ast[0]['property']['name']
    #
    # def test_2008_TC3(self):
    #     request = {
    #         'designation': '2008 TC3',
    #         'json': '1',
    #     }
    #     ast = mpcfetch.get(request)
    #     body = mpcfetch.get_body(ast[0]['property'])
    #
    # def test_2014_AA(self):
    #     request = {
    #         'designation': '2014 AA',
    #         'json': '1',
    #     }
    #     ast = mpcfetch.get(request)
    #     print ast[0]['property']['period']

    def test_loadDataset(self):
        raw = mpcfetch.load_dataset('Soft03CritList.txt')
        ast = mpcfetch.read_db(raw[0])

        ast.compute('2003/4/11')
        print("%s %s" % (ast.ra, ast.dec))

        ast.compute('2004/4/11')
        print("%s %s" % (ast.ra, ast.dec))


if __name__ == '__main__':
    unittest.main()
