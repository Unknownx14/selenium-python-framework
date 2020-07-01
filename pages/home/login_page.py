from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.selenium_driver import SeleniumDriver
import logging   # this one is for logging
import utilities.custom_logger as cl   # this one is fot the use of the custom_logger.py


class LoginPage(SeleniumDriver): # U zagardu se stavlja koja se klasa Inherit-uje iz selenium_driver.py

    log = cl.customLogger(logging.DEBUG)   # ubaceno je prvo u selenium_driver.py pa onda i ovde da bi se videlo
    # da iz login_page.py se upisuje u logovanje

    def __init__(self, driver): #Ovo je potrebno da bi se svi find.element and send.keys prebacili u PAGE class
        super().__init__(driver) # Ovo kad se import SeleniumDriver
        self.driver_=driver

    # Locators
    _login_link="//div[@id='navbar']//a[@class='navbar-link fedora-navbar-link']"
    _email_field="user_email"
    _password_filed="user_password"
    _login_button='commit'
    _search_course='search-courses'

    # Ovo su metode koje rade isto sto i login(self, username, password): metoda, tj NALAZE(return) ELEMENTE
    # samo sto koriste Locators i ako se nesto promeni na sajtu, promenimo samo kod Locators
    # def getLoginLink(self):
    #     return self.driver_.find_element(By.XPATH, self._login_link)
    # def getEmailField(self):
    #     return self.driver_.find_element(By.ID, self._email_field)
    # def getPasswordField(self):
    #     return self.driver_.find_element(By.ID, self._password_filed)
    # def getLoginButton(self):
    #     return self.driver_.find_element(By.NAME, self._login_button)

    # ovo su metode koje vrse odredjene AKCIJE sa PRONADJENIM ELEMENTIMA
    def clickLoginLink(self):
        #self.getLoginLink().click()
        self.clickElement(self._login_link, locatorType='xpath') # Red iznad je promenjen da glasi kao ovaj
        # kao i one 4 metode iznad koje su sad zakomentarisane
        sleep(14)
    def enterEmail(self, email):
        #self.getEmailField().send_keys(email)
        self.sendKeys(email, self._email_field)
    def enterPassword(self, password):
        #self.getPasswordField().send_keys(password)
        self.sendKeys(password, self._password_filed)
    def clickLoginButton(self):
        #self.getLoginButton().click()
        self.clickElement(self._login_button, locatorType='name')


    def login(self, username, password): #Ovde je prerbaceno iz MOJ testcase loginlink, username, userpass, loginbutton
        # loginLink = self.driver_.find_element(By.XPATH, "//div[@id='navbar']//a[@class='navbar-link fedora-navbar-link']")
        # loginLink.click()
        self.clickLoginLink() # Ovo menja ona dva red odmah iznad
        # userEmail = self.driver_.find_element(By.ID, "user_email")
        # userEmail.send_keys(username)
        self.enterEmail(username)
        # userpass = self.driver_.find_element(By.ID, "user_password")
        # userpass.send_keys(password)
        self.enterPassword(password)
        sleep(1)
        # loginbutton = self.driver_.find_element(By.NAME, 'commit')
        # loginbutton.click()
        self.clickLoginButton()


    def verifyLoginSuccessful(self):
        result = self.isElementPresent('search-courses')
        return  result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='alert alert-danger']", 'xpath')
        return  result


    def searchCourse(self, courseName):   # ovo sam se ja igrao
        result= self.sendKeys(courseName, self._search_course)
        sleep(3)
        self.clickElement('//*[@id="search-course-button"]//i', 'xpath')

    def verifySearchButton(self):   # ovo sam se ja igrao
        result = self.isElementPresent('//*[@id="search-course-button"]//i', 'xpath')
        return result

    def takeScreenShot(self):   # ovo se ja igram
        self.screenShot(resultMessage="ScreenShot")