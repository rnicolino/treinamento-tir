import unittest
from ACDA080TESTCASE import ACDA080

suite = unittest.TestSuite()

suite.addTest(ACDA080('test_ACDA080_CT002'))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)