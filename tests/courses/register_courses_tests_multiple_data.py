from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#from pages.homepage.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_page import coursesPage
from ddt import ddt, data, unpack   # korsiti se za ddt



#####
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.mark.run(order=1)
    @data(('JavaScript', '//div[@title="JavaScript for beginners"]', '1234567890123456', '1022', '7878', '11080' ),
          ('JavaScript', '//div[@title="JavaScript Masterclass"]', '1234567890123456', '1022', '5555', '11080'))
    @unpack
    def test_validCourses(self, courseName, desiredCourse, ccNum, ccDate, ccCVV, zip):

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

        entercourse= coursespazh.searchCourse(courseName)

        coursesExist= coursespazh.verifyDemandedCourses()
        tstatus.mark(coursesExist, 'All demanded courses are present' )
        # assert

        #pickCourse= coursespazh.selectCourse()
        pickCourse = coursespazh.clickElement(desiredCourse, 'xpath')

        enrollClick = coursespazh.clickEnroll()
        sleep(3)
        coursespazh.scrollDown()
        sleep(3)

        ccData= coursespazh.creditCardCredentialsWithoutPurchase(ccNum, ccDate, ccCVV, zip)
        coursespazh.takeScreenShot()
        sleep(5)

        errorCreditcard= coursespazh.invalidCreditcardMessage()
        tstatus.markFinal('test_validCourses', errorCreditcard, 'Error Creditcard message present')
        sleep(3)

        # coursespazh.scrollUp()
        # backToSearchBar = coursespazh.clickElement('//a[@class="navbar-brand header-logo"]', 'class')

    # @pytest.mark.run(order=1)
    # def test_validCoursesEnabledDisabled(self):
    #
    #     baseurl = "https://letskodeit.teachable.com/"
    #     driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
    #     # driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     # driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
    #     driver.get(baseurl)
    #     driver.implicitly_wait(5)
    #
    #     coursespazh = coursesPage(driver)
    #     tstatus = TestStatus(driver)
    #
    #     coursespazh.login("test@email.com", 'abcabc')
    #     sleep(1)
    #
    #     searchPlace = coursespazh.verifyLoginSuccessful()
    #     tstatus.mark(searchPlace, 'Login to Course page successful')
    #     # assert
    #
    #     entercourse = coursespazh.searchCourse('JavaScript')
    #
    #
    #     coursesExist = coursespazh.verifyDemandedCourses()
    #     tstatus.mark(coursesExist, 'All demanded courses are present')
    #     # assert
    #
    #     pickCourse = coursespazh.selectCourse()
    #
    #     enrollClick = coursespazh.clickEnroll()
    #     sleep(3)
    #     coursespazh.scrollDown()
    #     sleep(3)
    #
    #     enrollClickDisabledByDefault = coursespazh.verifyEnrollCannotbeDone()
    #     tstatus.markFinal('test_validCoursesEnabledDisabled', enrollClickDisabledByDefault,
    #                       "Cannot click on the Enroll button, all the required fields"
    #                       "must be filled in ")
    #     sleep(3)




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



