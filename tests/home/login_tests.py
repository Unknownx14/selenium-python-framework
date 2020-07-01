from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages.home.login_page import LoginPage
import unittest #ovo se importuje da bi se napravili testcasevi
import pytest   # za orderovanje koji ce test prvi da se izvrsi
from utilities.teststatus import TestStatus   # za koriscenje TestStatus classe za vise od jednog assert-ovanja


class loginTests(unittest.TestCase): # u zagradu se upusije kad se importuje unittest
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        baseurl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
        # driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.get(baseurl)
        driver.implicitly_wait(5)

        tstatus = TestStatus(driver)   # tstatus je dobio klasu TestStatus iz teststatus.py
        loginpazh = LoginPage(driver) #loginpazh je dobio klasu LoginPage iz login_page.py
        loginpazh.login("test@email.com", "abcabc")


        # searchPlace=driver.find_element(By.ID, 'search-courses')
        # if searchPlace is not None:
        #     print("Login Successful, Fuck Yeah")
        # else:
        #     print("Login has Failed")
        searchPlace=loginpazh.verifyLoginSuccessful()   # kad se napravi ova metoda verifyLoginSuccessful onda
        # se ovo iznad ne koristi vise
        #assert searchPlace == True   # umesto assert se sad koriste metode iz TestStatus classe
        tstatus.mark(searchPlace,"Login was successful")

        searchButton= loginpazh.verifySearchButton()
        #assert searchButton == True   # umesto assert se sad koriste metode iz TestStatus classe
        tstatus.markFinal("test_validLogin", searchButton, "SearchButton was verified")


        searchCourse=loginpazh.searchCourse('JavaScript')   # ovo menja ove linije koda ispod
        # searchPlace.send_keys('JavaScript')
        # driver.find_element(By.XPATH, '//*[@id="search-course-button"]//i').click()
        loginpazh.takeScreenShot() # moj kod
        sleep(5)
        driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        baseurl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
            # driver = webdriver.Firefox()
        driver.maximize_window()
            # driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.get(baseurl)
        driver.implicitly_wait(5)

        loginpazh = LoginPage(driver)  # loginpazh je dobio klasu LoginPage iz login_page.py
        loginpazh.login("test@email.com", "abcabc123")

        loginpazh.takeScreenShot() # moj kod
        sleep(3)
        searchPlace = loginpazh.verifyLoginFailed()
        assert searchPlace == True

        loginpazh.takeScreenShot() # moj kod
        sleep(3)
        driver.quit()


        # DelBoy vise ne treba kad se importuje unittest
# DelBoy= loginTests()
# DelBoy.test_validLogin()