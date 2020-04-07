from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium_utils import element

from Pages1.Locators import Locator


class Register(object):

    def __init__(self, driver):
        self.driver = driver

# registration page locators defining , you can directly call the WebElement from here
        self.regis_txt = driver.find_element(By.XPATH, Locator.regis_txt)
        self.firstName = driver.find_element(By.XPATH, Locator.firstName)
        self.lastName = driver.find_element(By.XPATH, Locator.lastName)
        self.phone = driver.find_element(By.XPATH, Locator.phone)
        self.email = driver.find_element(By.XPATH, Locator.email)
        self.country = driver.find_element(By.XPATH, Locator.country)
        self.userName = driver.find_element(By.XPATH, Locator.userName)
        self.password = driver.find_element(By.XPATH, Locator.password)
        self.confirmPassword = driver.find_element(By.XPATH, Locator.confirmPassword)
        self.submit = driver.find_element(By.XPATH, Locator.submit)


#you can return WebElement from method and call it also, and useful method with parameter you define here
    def getRegis_txt(self):
        return self.regis_txt

    def setFirstName(self,Name, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.firstName, page_header_pixels)
        self.firstName.clear()
        self.firstName.send_keys(Name)

    def setLastName(self, name, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.lastName, page_header_pixels)
        self.lastName.send_keys(name)

    def setPhone(self, phone, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.phone, page_header_pixels)
        self.phone.send_keys(phone)

    def setEmail(self, email, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.email, page_header_pixels)
        self.email.send_keys(email)

    def setCountry(self, country, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.country, page_header_pixels)
        select = Select(self.country)
        select.select_by_visible_text(country)

    def setUserName(self, username, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.userName, page_header_pixels)
        self.userName.send_keys(username)

    def setPassword(self, password, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.password, page_header_pixels)
        self.password.send_keys(password)

    def setConfirmPassword(self, confirmPassword , driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.confirmPassword, page_header_pixels)
        self.confirmPassword.send_keys(confirmPassword)

    def submitRegistration(self, driver):
        page_header_pixels = 200
        element.scroll_into_view(driver, self.submit, page_header_pixels)
        self.submit.click()
