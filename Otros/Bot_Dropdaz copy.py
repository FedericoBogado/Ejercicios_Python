import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\dakra\Documents\chromedriver.exe")
        

    def login(self):
        self.driver.get("https://dropdaz.com/")
        actions = ActionChains(self.driver)

        time.sleep(5)

        login = self.driver.find_element_by_xpath("/html/body/div/section[3]/div/div[2]/div/div[3]/div/div/div/a[2]/div[2]/span[1]")
        actions.context_click(login).perform()


    def tearDown(self):
        self.driver.close()
    

if __name__ == "__main__":    #access point
    unittest.main()