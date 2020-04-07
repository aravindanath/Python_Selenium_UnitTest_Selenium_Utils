from selenium.webdriver.common.by import By
from selenium_utils import element
from Pages1.Locators import Locator


class Home(object):

    def __init__(self, driver):
        self.driver = driver

# home page locators defining
        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.sign_on = driver.find_element(By.XPATH, Locator.sign_on)
        self.contact = driver.find_element(By.XPATH, Locator.contact)
        self.support = driver.find_element(By.XPATH, Locator.support)
        self.register = driver.find_element(By.XPATH, Locator.register)

    def getLogo(self, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.logo, page_header_pixels)
        return self.logo

    def getSignOn(self, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.sign_on, page_header_pixels)
        return self.sign_on

    def getContact(self, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.contact, page_header_pixels)
        return self.contact

    def getSupport(self, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.support, page_header_pixels)
        return self.support

    def getRegister(self, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.register, page_header_pixels)
        return self.register