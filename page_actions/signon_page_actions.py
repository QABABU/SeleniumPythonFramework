from configuration.logger import ConsoleLogger
from page_actions.webdriver_actions import WebDriverActions
from page_locators.signon_page_locators import SignOnPageLocators


class SignOnPageActions(WebDriverActions):
    """ This page contains action methods of SignOnPage"""

    log = ConsoleLogger.get_logger("SignOnPageActions")

    @classmethod
    def verify_signon_page(cls, driver):
        cls.log.info('verifying SIGN-ON page')
        return cls.is_element_displayed(driver, SignOnPageLocators.SIGN_ON_LINK)

