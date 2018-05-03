from unittest.mock import MagicMock
from bb import *
import zipfile
import unittest

class BBtest(unittest.TestCase):

    def setUp(self):
        "setup for the fakezipfile class and to mock the namelist function"
        fakezip = MagicMock()   #mock zipfile
        fakezip.namelist = MagicMock(return_value=['hello.txt','test.txt']) #namelist to contain these files
        fakezip.extract = MagicMock()   #mock zipfile extract function
        self.testMock = BBSubmission(fakezip)
        self.testMock.runTest = MagicMock() #runTest() Magic Mock

    def test_true_findFile(self):
        "Test to find hello.txt in testMock's namelist"
        self.assertTrue(self.testMock.findFile('hello.txt'))

    def test_false_findFile(self):
        "Test for when file isn't found"
        self.assertFalse(self.testMock.findFile('fail.txt'))

    def test_testSubmission_Pass(self):
        "Tests to see if runTest and extract was called"
        self.testMock.testSubmission('test.txt',self.testMock.archive.namelist,'result.txt')
        self.testMock.runTest.assert_any_call('test.txt')
        self.testMock.archive.extract.assert_any_call('test.txt')

    def test_testSubmission_Fail(self):
        "Tests case where file isn't found, should raise FileNotFoundError and not call runTest"
        with self.assertRaises(FileNotFoundError):
            self.testMock.testSubmission('nofile',self.testMock.archive.namelist,'result.txt')
        self.testMock.runTest.assert_not_called()
    
if __name__ == '__main__':
    unittest.main()
