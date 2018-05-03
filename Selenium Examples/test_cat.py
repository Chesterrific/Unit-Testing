import unittest
from page import *
from selenium import *
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class EastBayTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5) #give the pages time to load
        self.page = EBHome(self.driver,'http://catalog.csueastbay.edu/')
        
        
    """Tests for BIOL class in table in Alpha order"""
    def test_search_alpha(self):
        self.page.Select_Option('Courses')
        self.page.Input_Keyword('CS 4320')
        self.page.Choose_Alpha()
        element = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[3]/tbody/tr[3]/td/a').text
        self.assertEqual(element, 'BIOL 3011 - Foundational Biology')

        
    """"Tests for Best Match: CS 4320 - Software Testing and Quality Assurance in table in Ranked order"""
    def test_search_ranked(self):
        self.page.Select_Option('Courses')
        self.page.Input_Keyword('CS 4320')
        #self.page.Choose_Ranked()
        #self.assertTrue(self.page.Is_CS())
        element = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[3]/td/a').text
        self.assertEqual(element, 'Best Match: CS 4320 - Software Testing and Quality Assurance')

    """Tests that each element in the results table has CS as a prefix"""
    def test_CS_courses(self):
        self.page.Select_Option('Courses')
        self.page.Input_Keyword('CS 4320')
        #for this one, I couldn't get the correct length of the table, so I ended up hard coding for the length of the table on the first page.
        #elements = self.driver.find_elements_by_xpath('/html/body/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[3]/tbody/tr/td')
        #total_rows = len(elements)
        self.assertTrue(self.page.CS_Prefix())

    """Tests for proper output of options Programs and programming"""        
    def test_Programming_in_Programs(self):
        self.page.Select_Option('Programs')
        self.page.Input_Keyword('programming')
        self.assertTrue(self.page.Program_programming())
        
    
    """Tests 'zzz' input"""
    def test_zzz(self):
        self.page.Select_Option('Courses')
        self.page.Input_Keyword('zzz')
        element1 = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[3]/td').text
        self.assertEqual(element1, 'No matches.')
        element2 = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[3]/tbody/tr[3]/td').text
        self.assertEqual(element2, 'No matches.')
        element3 = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[4]/tbody/tr[2]/td').text
        self.assertEqual(element3, 'No results found.')

    """Tests no option given to dropdown"""
    def test_No_Option(self):
        self.page.Select_Option('Select an option')
        self.page.Input_Keyword('CS 4320')
        element = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[2]/td').text
        self.assertEqual(element, '')

if __name__ == "__main__":
    unittest.main()
