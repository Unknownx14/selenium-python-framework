from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#from pages.homepage.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_page import coursesPage


# class practicetwo():
#
#     def testy(self):
#         baseurl = "https://letskodeit.teachable.com/"
#         driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
#         # driver = webdriver.Firefox()
#         driver.maximize_window()
#         # driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
#         driver.get(baseurl)
#         driver.implicitly_wait(5)
#
#         loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@class='navbar-link fedora-navbar-link']")
#         loginLink.click()
#         username = driver.find_element(By.ID, "user_email")
#         username.send_keys("test@email.com")
#         userpass= driver.find_element(By.ID, "user_password")
#         userpass.send_keys("abcabc")
#         sleep(3)
#         loginbutton=driver.find_element(By.NAME, 'commit')
#         loginbutton.click()
#         sleep(5)
#
#         searchPlace=driver.find_element(By.ID, "search-courses")
#         searchPlace.send_keys("JavaScript")
#         driver.find_element(By.XPATH, '//*[@id="search-course-button"]//i').click()
#         sleep(3)
#
#         selectCourse=driver.find_element(By.XPATH, '//div[@title="JavaScript for beginners"]')
#         selectCourse.click()
#
#         #Maybe new window or frame?
#
#         enrollCourse=driver.find_element(By.ID, "enroll-button-top")
#         enrollCourse.click()
#         sleep(3)
#
#         driver.execute_script(" window.scrollBy(0, 1555); ")
#         anotherFrame = driver.switch_to.frame(driver.find_element(By.NAME, "__privateStripeFrame9"))
#         cardNum=driver.find_element(By.XPATH, '//*[@id="root"]//input[@name="cardnumber"]')
#         cardNum.send_keys("123456788787")
#         expDate=driver.find_element(By.XPATH, '//*[@id="root"]//input[@name="exp-date"]')
#         expDate.send_keys("1022")
#         driver.switch_to.default_content()
#         anotherFrame1 = driver.switch_to.frame(driver.find_element(By.NAME, "__privateStripeFrame10"))
#         cvcNum=driver.find_element(By.XPATH, '//*[@id="root"]//input[@name="cvc"]')
#         cvcNum.send_keys("123")
#         sleep(3)
#         driver.switch_to.default_content()
#         confirmButton= driver.find_element(By.CLASS_NAME, "spc__primary-submit")
#         confirmButton.click()
#         sleep(10)
#
#
#
#
# DelBoy= practicetwo()
# DelBoy.testy()






#####
class coursesTests(unittest.TestCase):

    @pytest.mark.run(order=2)
    def test_validCourses(self):

        baseurl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
        #driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.get(baseurl)
        driver.implicitly_wait(5)

        coursespazh = coursesPage(driver)
        tstatus= TestStatus(driver)


        coursespazh.login("test@email.com", 'abcabc')
        sleep(1)

        searchPlace=coursespazh.verifyLoginSuccessful()
        tstatus.mark(searchPlace, 'Login to Course page successful')
        #assert

        entercourse= coursespazh.searchCourse('JavaScript')

        coursesExist= coursespazh.verifyDemandedCourses()
        tstatus.mark(coursesExist, 'All demanded courses are present' )
        # assert

        pickCourse= coursespazh.selectCourse()

        enrollClick = coursespazh.clickEnroll()
        sleep(3)
        coursespazh.scrollDown()
        sleep(3)

        ccData= coursespazh.creditCardCredentials('1234567890123456', '1022', '7878', '11080')
        coursespazh.takeScreenShot()
        sleep(5)

        errorCreditcard= coursespazh.invalidCreditcardMessage()
        tstatus.markFinal('test_validCourses', errorCreditcard, 'Error Creditcard message present')
        sleep(5)

    @pytest.mark.run(order=1)
    def test_validCoursesEnabledDisabled(self):

        baseurl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
        # driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.get(baseurl)
        driver.implicitly_wait(5)

        coursespazh = coursesPage(driver)
        tstatus = TestStatus(driver)

        coursespazh.login("test@email.com", 'abcabc')
        sleep(1)

        searchPlace = coursespazh.verifyLoginSuccessful()
        tstatus.mark(searchPlace, 'Login to Course page successful')
        # assert

        entercourse = coursespazh.searchCourse('JavaScript')


        coursesExist = coursespazh.verifyDemandedCourses()
        tstatus.mark(coursesExist, 'All demanded courses are present')
        # assert

        pickCourse = coursespazh.selectCourse()

        enrollClick = coursespazh.clickEnroll()
        sleep(3)
        coursespazh.scrollDown()
        sleep(3)

        enrollClickDisabledByDefault = coursespazh.verifyEnrollCannotbeDone()
        tstatus.markFinal('test_validCoursesEnabledDisabled', enrollClickDisabledByDefault,
                          "Cannot click on the Enroll button, all the required fields "
                          "must be completed ")
        sleep(3)
        #

        # enrollClickDisabledByDefault = coursespazh.verifyEnrollCannotbeDone()
        # tstatus.mark(enrollClickDisabledByDefault, "Cannot click on Enroll button without all the "
        #                                            "required fields")
        # sleep(3)
        #
        # ccData = coursespazh.creditCardCredentialsWithoutPurchase('1234567890123456', '1022', '7878', '11080')
        # coursespazh.takeScreenShot()
        # sleep(5)
        #
        #
        # enrollClickEnabled = coursespazh.verifyEnrollCannotbeDone()
        # tstatus.markFinal('test_validCoursesEnabledDisabled', enrollClickEnabled, 'All the required fields are'
        #                                                             'filled and the course can be purchased' )
        # sleep(5)



