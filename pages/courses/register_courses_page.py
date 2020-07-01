from time import sleep
from base.selenium_driver import SeleniumDriver





class coursesPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver_=driver


    # Locators
    _login_link = "//div[@id='navbar']//a[@class='navbar-link fedora-navbar-link']"
    _email_field = "user_email"
    _password_filed = "user_password"
    _login_button = 'commit'
    _search_course = 'search-courses'
    _course_1= '//div[@title="JavaScript Masterclass"]'
    _course_2= '//div[@title="JavaScript for beginners"]'
    _desired_course = '//div[@title="JavaScript for beginners"]'
    _enroll_button = "enroll-button-top"
    _creditcard_number = '//*[@id="root"]//input[@name="cardnumber"]'
    _creditcard_expdate = '//*[@id="root"]//input[@name="exp-date"]'
    _creditcard_cvc = '//*[@id="root"]//input[@name="cvc"]'
    _agree_terms = 'agreed_to_terms_checkbox'
    _postal_code= '//*[@id="root"]//input[@name="postal"]'
    _purchase_button= "confirm-purchase"
    _another_Frame_1 = "__privateStripeFrame16"
    _another_Frame_2 = "__privateStripeFrame17"
    _another_Frame_3 = "__privateStripeFrame18"
    _another_Frame_4 = "__privateStripeFrame19"
    _invalid_creditcard= '//div[@id="new_card"]//div[contains(text(), "The card number is not a valid credit card number.")]'


    def clickLoginLink(self):
        self.clickElement(self._login_link, locatorType='xpath')
        sleep(14)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_filed)

    def clickLoginButton(self):
        self.clickElement(self._login_button, locatorType='name')


    def login(self, username, password): #Ovde je prerbaceno iz MOJ testcase loginlink, username, userpass, loginbutton
        # loginLink = self.driver_.find_element(By.XPATH, "//div[@id='navbar']//a[@class='navbar-link fedora-navbar-link']")
        # loginLink.click()
        self.clickLoginLink()

        self.enterEmail(username)

        self.enterPassword(password)
        sleep(1)

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

    def selectCourse(self):
        result = self.clickElement(self._desired_course, 'xpath')

    def clickEnroll(self):
        result = self.clickElement(self._enroll_button)

    def switchFrame1(self):
        result= self.switchToFrame(self._another_Frame_1, 'name')

    def switchFrame2(self):
        result= self.switchToFrame(self._another_Frame_2, 'name')

    def switchFrame3(self):
        result = self.switchToFrame(self._another_Frame_3, 'name')

    def switchFrame4(self):
        result = self.switchToFrame(self._another_Frame_4, 'name')

    def defaultIFrame(self):
        result = self.returnDefaultFrame()


    def creditCardCredentials(self, cardNumber, cardExpdate, cardCvcNum, postalCode):
        anotherFrame1 = self.switchFrame1()
        cardNum= self.sendKeys(cardNumber, self._creditcard_number, 'xpath' )
        defIFrame = self.defaultIFrame()
        anotherFrame2 = self.switchFrame2()
        cardExp= self.sendKeys(cardExpdate, self._creditcard_expdate, 'xpath')
        defIFrame= self.defaultIFrame()
        anotherFrame2 = self.switchFrame3()
        cardCvc= self.sendKeys(cardCvcNum, self._creditcard_cvc, 'xpath')
        defIFrame = self.defaultIFrame()
        anotherFrame2 = self.switchFrame4()
        cardCvc = self.sendKeys(postalCode, self._postal_code, 'xpath')
        defIFrame = self.defaultIFrame()
        checkTermsAndPolicy= self.agreeTermsAndPolicy()
        purchaseButton = self.clickElement(self._purchase_button)

    def verifyDemandedCourses(self):
        course1=self.isElementPresent(self._course_1, 'xpath')
        course2 = self.isElementPresent(self._course_2, 'xpath')
        return course1, course2

    def invalidCreditcardMessage(self):
        result = self.isElementPresent(self._invalid_creditcard, 'xpath')
        return result

    def agreeTermsAndPolicy(self):
        result = self.clickElement(self._agree_terms)

    def verifyEnrollCannotbeDone(self):
        result = self.isEnabled(locator=self._purchase_button, locatorType='id',
                                info="Enroll Button is disabled "
                                            "since all the required fields are not completed")
        return not result

    def creditCardCredentialsWithoutPurchase(self, cardNumber, cardExpdate, cardCvcNum, postalCode):
        anotherFrame1 = self.switchFrame1()
        cardNum= self.sendKeys(cardNumber, self._creditcard_number, 'xpath' )
        defIFrame = self.defaultIFrame()
        anotherFrame2 = self.switchFrame2()
        cardExp= self.sendKeys(cardExpdate, self._creditcard_expdate, 'xpath')
        defIFrame= self.defaultIFrame()
        anotherFrame2 = self.switchFrame3()
        cardCvc= self.sendKeys(cardCvcNum, self._creditcard_cvc, 'xpath')
        defIFrame = self.defaultIFrame()
        anotherFrame2 = self.switchFrame4()
        cardCvc = self.sendKeys(postalCode, self._postal_code, 'xpath')
        defIFrame = self.defaultIFrame()
        checkTermsAndPolicy= self.agreeTermsAndPolicy()





