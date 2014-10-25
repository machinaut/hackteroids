__author__ = 'Joe'

import unittest
import mpcfetch

class TestSequenceFunctions(unittest.TestCase):

    def test_shuffle(self):
        request = {
            'order_by_desc': 'spin_period',
            'limit': '10',
            'json': '1',
        }
        ast = mpcfetch.get(request)
        print ast


if __name__ == '__main__':
    unittest.main()
