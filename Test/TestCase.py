from Pages1.HomePage import Home
from Pages1.RegistrationPage import Register
from Utility.ReadExcel import readExcel
from Utility.BrowserDebugger import debug_request
import unittest
from selenium_utils import screenshot
import json
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class RegistrationTest(unittest.TestCase):

    def setUp(self):

        if readExcel('../Data/data.xlsx', 'Browser_Conf', 'A2') == "Yes":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_search_in_python_org(self):


        driver = self.driver
        with open('../Data/data.json') as json_file:
            data = json.load(json_file)
            driver.get('http://demo.guru99.com/test/newtours/')
            # debug_request(driver)
            driver.save_screenshot('./ScreenShots/sc1.png')
            driver.set_page_load_timeout(20)
            m = Home(driver)
            m.getRegister().click()
            r = Register(driver)
            r.setFirstName(data['firstname'], driver)
            r.setLastName(data['lastname'], driver)
            r.setPhone(data['mobileno'], driver)
            r.setCountry(data['country'], driver)
            r.setEmail(data['emailid'], driver)
            r.setUserName(data['lastname'], driver)
            r.setPassword(data['password'], driver)
            r.setConfirmPassword(data['password'], driver)
            r.submitRegistration(driver)
            screenshot.resize_to_page_size(driver)
            screenshot.get_screenshot(driver, "screenshot.png")

