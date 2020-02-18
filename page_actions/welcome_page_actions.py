from config.logger import ConsoleLogger
from page_actions.webdriver_actions import WebDriverActions
from page_locators.welcome_page_locators import WelcomePageObjects


class WelcomePageActions(WebDriverActions):

    log = ConsoleLogger.get_logger("WelcomePageActions")

    @classmethod
    def welcome_page_title(cls, driver):
        return cls.get_title(driver)

    @classmethod
    def sign_in_action(cls, driver, uid, pwd):
        cls.log.info("sign in action")
        try:
            cls.enter_text(driver, WelcomePageObjects.USER_NAME_FIELD, uid)
            cls.enter_text(driver, WelcomePageObjects.PASSWORD_FIELD, pwd)
            cls.click_element(driver, WelcomePageObjects.SIGN_IN_BTN)
        except Exception as e:
            cls.log.info("exception in  sign in action")
            print("Exception in sign_in_action--" + str(e))
            exit(-1)

    @classmethod
    def navigate_to_reg_page(cls, driver):
        cls.log.info("navigating to the reg page :: navigate_to_reg_page")
        try:
            cls.click_element(driver, WelcomePageObjects.REGISTER_LINK)
        except Exception as e:
            cls.log.error("Exception in navigate_to_reg_page --" + str(e))
            exit(-1)
