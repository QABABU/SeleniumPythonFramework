import pytest
from base.base_class import BaseClass
from base.page_object_manager import PageObjectManager
from config.logger import ConsoleLogger


@pytest.mark.usefixtures("pom_init")
class TestsHomePage(BaseClass):
    """ Home Page Tests"""

    log = ConsoleLogger.get_logger("TestsHomePage")

    def test_valid_login(self, get_driver):
        self.log.info("executing test script :: test_valid_login  ")
        driver = get_driver
        self.welcome_page_obj.sign_in_action(driver, 'admin', 'admin')
        signon_page_obj = PageObjectManager.get_signon_page_obj()
        signon_page_obj.verify_signon_page(driver)

    def test_invalid_login(self, get_driver):
        self.log.info("executing test script :: test_invalid_login")
        driver = get_driver
        self.welcome_page_obj.sign_in_action(driver, 'admin', 'admin')

    def test_not_valid_login(self, get_driver):
        self.log.info("test_not_valid_login")
        driver = get_driver
        print(self.welcome_page_obj.welcome_page_title(driver))
