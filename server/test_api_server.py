import unittest
import time
import sys
import random
import api_server


class TestApiServer(unittest.TestCase):
    def setUp(self):
        time.clock()
        pass

#    def test_api_0(self):
#        row_id = 'row_key'
#        statistic = api_server.STATISTIC.AVERAGE
#        period = 5
#        api_server.api_test1(row_id, "cf1", "total", statistic, period=period, time_from=0, time_to=0)
#    
    def test_api_1(self):
        time.clock()
        row_id = 'instance-00000001@pyw.novalocal'
        statistic = api_server.STATISTIC.AVERAGE
        period = 5
        time_from = 1332815400
        time_to = 0
        scf_str = 'total'
        cf_str = 'cpu'
        rs, lenrs = api_server.api_getdata(row_id, cf_str, scf_str, statistic, period=period, time_from=time_from, time_to=time_to)
        print lenrs, "results", 'spend', time.clock(), "seconds"
        print '-' * 60
    
    def test_api_statistic(self):
        time.clock()
        row_id = 'instance-00000001@pyw.novalocal'
        period = 5
        time_from = 1332833464
        time_to = 0
        scf_str = 'total'
        cf_str = 'cpu'
        
        statistic = api_server.STATISTIC.SUM
        api_server.api_statistic(row_id, cf_str, scf_str, statistic, period=period, time_from=time_from, time_to=time_to)
        print '-' * 60
        print "spend %f seconds" % time.clock()
        
        statistic = api_server.STATISTIC.MAXIMUM
        api_server.api_statistic(row_id, cf_str, scf_str, statistic, period=period, time_from=time_from, time_to=time_to)
        print '-' * 60
        print "spend %f seconds" % time.clock()
        
        statistic = api_server.STATISTIC.MINIMUM
        api_server.api_statistic(row_id, cf_str, scf_str, statistic, period=period, time_from=time_from, time_to=time_to)
        print '-' * 60
        print "spend %f seconds" % time.clock()
        
        statistic = api_server.STATISTIC.AVERAGE
        api_server.api_statistic(row_id, cf_str, scf_str, statistic, period=period, time_from=time_from, time_to=time_to)
        print '-' * 60
        print "spend %f seconds" % time.clock()
    def test_demo(self):
        self.assertTrue(True)

    def test_demo2(self):
        self.assertEqual(['vda', 'vdb'], ['vda', 'vdb'])

if __name__ == '__main__':
    unittest.main()