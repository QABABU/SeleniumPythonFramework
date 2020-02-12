from config.logger import ConsoleLogger
from page_actions.registration_page_actions import RegistrationPageActions
from page_actions.signon_page_actions import SignOnPageActions
from page_actions.welcome_page_actions import WelcomePageActions


class PageObjectManager:

    log = ConsoleLogger.get_logger("BaseClass")

    welcome_page_obj = None
    reg_page_obj = None
    signon_page_obj = None

    @classmethod
    def get_welcome_page_obj(cls):
        cls.log.info('executing method :: get_welcome_page_obj')
        if cls.welcome_page_obj is None:
            cls.log.info("obj is null -- so creating the welcome page obj")
            cls.welcome_page_obj = WelcomePageActions()
        return cls.welcome_page_obj

    @classmethod
    def get_reg_page_obj(cls):
        cls.log.info('executing method :: get_reg_page_obj')
        if cls.reg_page_obj is None:
            cls.log.info("obj is null -so creating reg page obj")
            cls.reg_page_obj = RegistrationPageActions()
        return cls.reg_page_obj

    @classmethod
    def get_signon_page_obj(cls):
        cls.log.info('executing method :: get_signon_page_obj')
        if cls.signon_page_obj is None:
            cls.log.info("obj is null -so creating reg page obj")
            cls.signon_page_obj = SignOnPageActions()
        return cls.signon_page_obj


