import unittest
from TAFA232TESTCASE import TAFA232

suite = unittest.TestSuite()

suite.addTest(TAFA232('test_TAFA232_CT001'))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)