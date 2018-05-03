from page_objects import PageObject, PageElement
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasePage(PageObject):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self,driver,url):
        self.driver = driver
        self.driver.get(url)
        
class EBHome(BasePage):
    
    """Selects option from dropdown menu"""
    def Select_Option(self, option):
        select = Select(self.driver.find_element_by_id('location'))
        select.select_by_visible_text(option)

    """Passes Keyword into search field"""
    def Input_Keyword(self, key):
        keyword = self.driver.find_element_by_id('keyword')
        keyword.clear()
        keyword.send_keys(key)
        keyword.send_keys(Keys.ENTER)

    """Choose Alphabetical order"""
    def Choose_Alpha(self):
        self.driver.find_element_by_link_text('Alphabetical').click()

    """Choose Ranked order"""
    def Choose_Ranked(self):
        self.driver.find_element_by_link_text('Ranked').click()
    
    """Verifies that CS is in the prefix of all elements in the table"""
    def CS_Prefix(self):
        for count in range(3, 18): #there are 15 elements in the table on the first page
            site = '/html/body/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[3]/tbody/tr[' + str(count) + ']/td/a'
            if 'CS' not in (self.driver.find_element_by_xpath(site).text):
                return False
        return True

    """Verifies that “Computer Science, B.S.”, “Computer Science, M.S.” and “Computer Science Minor” are on first page"""
    def Program_programming(self):
        keywords = ['Computer Science, B.S.','Computer Science, M.S.','Computer Science Minor']
        for count in range(3):
            flag = False
            for row in range(3,18):
                site = '/html/body/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[' + str(row) + ']/td/a'
                if keywords[count] in (self.driver.find_element_by_xpath(site).text):
                    flag = True
            if flag == False:
                return False
        return True
        
