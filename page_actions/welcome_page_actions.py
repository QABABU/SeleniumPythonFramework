from config.logger import ConsoleLogger
from page_locators.welcome_page_locators import WelcomePageObjects


class WelcomePageActions:

    log = ConsoleLogger.get_logger("WelcomePageActions")

    # def __init__(, driver):
    #     a = "welcome page"
    #     driver = driver

    @classmethod
    def welcome_page_title(cls, driver):
        return driver.title

    @classmethod
    def sign_in_action(cls, driver, uid, pwd):
        try:
            driver.find_element(*WelcomePageObjects.USER_NAME_FIELD).send_keys(uid)
            driver.find_element(*WelcomePageObjects.PASSWORD_FIELD).send_keys(pwd)
            driver.find_element(*WelcomePageObjects.SIGN_IN_BTN).click()
        except Exception as e:
            print("Exception in sign_in_action--" + str(e))
            exit(-1)

    @classmethod
    def navigate_to_reg_page(cls, driver):
        try:
            driver.find_element(*WelcomePageObjects.REGISTER_LINK).click()
        except Exception as e:
            print("Exception in navigate_to_reg_page --" + str(e))
            exit(-1)
