from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging   # this one is for logging
import utilities.custom_logger as cl   # this one is fot the use of the custom_logger.py
import time   # potrebno za Screenshots
import os   # potrebno za Screenshots


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)   # kad se ovo ubaci onda umesto print() ide  self.log.info

    def screenShot(self, resultMessage):
        fileName= resultMessage + "." + str(round(time.time() *1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName= screenshotDirectory + fileName
        currentDirectory= os.path.dirname(__file__)
        destinationFile= os.path.join(currentDirectory, relativeFileName)
        destinationDirectory= os.path.join(currentDirectory, screenshotDirectory )

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver_.save_screenshot(destinationFile)   # this line saves a screenshot
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("### Exception occured")
            print_stack()


    def __init__(self, driver):
        #self.switch_to = driver1
        self.driver_=driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType== 'xpath':
            return  By.XPATH
        elif locatorType== 'name':
            return  By.NAME
        elif locatorType== 'css':
            return  By.CSS_SELECTOR
        elif locatorType== 'class':
            return  By.CLASS_NAME
        elif locatorType== 'link':
            return  By.LINK_TEXT
        else:
            self.log.info('Type ' + locatorType +' is not supported')
            return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType=locatorType.lower()
            byType= self.getByType(locatorType)
            element= self.driver_.find_element(byType, locator)
            self.log.info('The element has been found with locator: ' +locator + ' and locatorType: ' + locatorType)
        except:
            self.log.info('!!!RED FLAG - The element has NOT been found with locator: ' +locator + ' and locatorType: ' + locatorType)
        return element


    def getElementList(self, locator, locatorType='id'):
        element = None
        try:
            locatorType=locatorType.lower()
            byType= self.getByType(locatorType)
            element= self.driver_.find_elements(byType, locator)
            self.log.info('The element has been found with locator: ' +locator + ' and locatorType: ' + locatorType)
        except:
            self.log.info('!!!RED FLAG - The element has NOT been found with locator: ' +locator + ' and locatorType: ' + locatorType)
        return element


    def clickElement(self, locator, locatorType='id'):
        try:
            element= self.getElement(locator, locatorType)
            element.click()
            self.log.info('Clicked on the element with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
        except:
            self.log.info('!!!RED FLAG - Cannot click on the element with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
            print_stack()

    def sendKeys(self, data,  locator, locatorType='id'):
        try:
            element= self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info('Sent data ' + data + ' on the element with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
        except:
            self.log.info('!!!RED FLAG - Cannot send data ' + data + ' on the element with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
            print_stack()



    # def clickElement(self, locator, locatorType='id'):
    #     try:
    #         element = self.getElement(locator, locatorType)
    #         element.click()
    #         self.log.info("Clicked on the element with locator:" + locator + " and locator type:" + locatorType)
    #     except:
    #         self.log.info("Cannot click on the element with locator:" + locator + " and locator type:" + locatorType)
    #         print_stack()

    # def sendKeys(self, data,  locator, locatorType='id'):
    #     try:
    #         element = self.getElement(locator, locatorType)
    #         element.send_keys(data)
    #         self.log.info("Sent data on the element with locator:" + locator + " and locator type:" + locatorType)
    #     except:
    #         self.log.info("Cannot send data on the element with locator:" + locator + " and locator type:" + locatorType)
    #         print_stack()

    def isElementPresent(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info('Element is present with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
                return True
            else:
                return False
        except:
            self.log.info('Element is NOT present with the locator: ' + locator+ ' and  locatorType: ' + locatorType )
            return False

    def elementPresenceCheck(self, locator, byType):
        try:

            elementList = self.driver_.find_elements(byType, locator)
            if len(elementList)>0:
                self.log.info('Element(s) is/are present')
                return True
            else:
                self.log.info('Element(s) is/are NOT present')
                return False
        except:
            self.log.info('Element is NOT present')
            return False


    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def switchToFrame(self, locator, locatorType='id'):
        try:
            anotherFrame = self.driver_.switch_to.frame(self.getElement(locator, locatorType))
            self.log.info('Switched to another IFrame with the locator - ' + locator)

        except:
            self.log.info('!!! RED ALERT - Has not switched to another IFrame with the locator - ' + locator)
            print_stack()


    def returnDefaultFrame(self):
        defaultFrame=self.driver_.switch_to.default_content()

    def scrollDown(self):
        result = self.driver_.execute_script(" window.scrollBy(0, 1555); ")

    def scrollUp(self):
        result = self.driver_.execute_script(" window.scrollBy(0, -1555); ")



    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled












