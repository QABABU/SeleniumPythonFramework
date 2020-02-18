import pytest
from base.base_class import BaseClass
from base.page_object_manager import PageObjectManager
from config.logger import ConsoleLogger


@pytest.mark.usefixtures("pom_init")
class TestsHomePage(BaseClass):
    """ Home Page Tests"""

    log = ConsoleLogger.get_logger("TestsHomePage")

    @pytest.fixture(autouse=True)
    def set_up(self, get_driver):
        self.driver = get_driver

    def test_valid_login(self):
        self.log.info("executing test script :: test_valid_login  ")
        self.welcome_page_obj.sign_in_action(self.driver, 'admin', 'admin')
        signon_page_obj = PageObjectManager.get_signon_page_obj()
        signon_page_obj.verify_signon_page(self.driver)

    def test_invalid_login(self):
        self.log.info("executing test script :: test_invalid_login")
        self.welcome_page_obj.sign_in_action(self.driver, 'invalid_admin', 'invalid_admin')

    def test_not_valid_login(self, get_driver):
        self.log.info("test_not_valid_login")
        print(self.welcome_page_obj.welcome_page_title(self.driver))
