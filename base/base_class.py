import pytest

from base.page_object_manager import PageObjectManager
from config.logger import ConsoleLogger
from config.global_variable import BROWSER_TYPE, APP_URL
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BaseClass:
    """ This base page class contains common webdriver methods  """

    log = ConsoleLogger.get_logger("BaseClass")

    welcome_page_obj = None

    @pytest.fixture(scope="class")
    def pom_init(self):
        self.log.info('initializing the welcome page obj')
        if BaseClass.welcome_page_obj is None:
            BaseClass.welcome_page_obj = PageObjectManager.get_welcome_page_obj()
        yield BaseClass.welcome_page_obj

    @pytest.fixture(scope="function")
    def get_driver(self):
        self.log.info('Initializing the browser')
        if BROWSER_TYPE == "chrome":
            self.log.info('initializing the chrome browser--')
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif BROWSER_TYPE == "firefox":
            self.log.info('initializing the ff browser')
            driver = webdriver.Chrome(executable_path=GeckoDriverManager().install())
        else:
            self.log.info('The selected browser type is not supported, choose the correct one')
            raise ValueError("The selected browser type is not supported, choose the correct one")
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(15)
        self.log.info('launching the application url')
        driver.get(APP_URL)
        yield driver
        driver.quit()
