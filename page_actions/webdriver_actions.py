from selenium.webdriver.common.keys import Keys

from config.logger import ConsoleLogger


class WebDriverActions:
    """ This method contains webdriver common actions """

    log = ConsoleLogger.get_logger("WebDriverActions")

    @classmethod
    def click_element(cls, driver, locator):
        try:
            driver.find_element(*locator).click()
        except Exception as e:
            cls.log.error("native click failed due to - " + str(e))
            exit(-1)

    @classmethod
    def click_using_js(cls, driver, locator):
        try:
            element = driver.find_element(*locator)
            driver.execute_script('arguments[0].click();', element)
        except Exception as e:
            cls.log.error("JavaScript click failed due to - " + str(e))
            exit(-1)

    @classmethod
    def enter_text(cls, driver, locator, text):
        try:
            element = driver.find_element(*locator)
            element.clear()
            element.send_keys(text + Keys.TAB)
        except Exception as e:
            cls.log.error("entering text failed due to - " + str(e))
            exit(-1)

    @classmethod
    def is_element_exist(cls, driver, locator):
        try:
            element = driver.find_element(*locator)
            if element.size != 0:
                return True
            else:
                return False
        except Exception as e:
            cls.log.error("checking is_element exist is failed - " + str(e))
            exit(-1)

    @classmethod
    def is_element_displayed(cls, driver, locator):
        try:
            element = driver.find_element(*locator)
            if element.is_displayed():
                return True
            else:
                return False
        except Exception as e:
            cls.log.error("checking is_element_displayed is failed - " + str(e))
            exit(-1)
