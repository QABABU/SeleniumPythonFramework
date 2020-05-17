from config.logger import ConsoleLogger


class RegistrationPageActions:

    log = ConsoleLogger.get_logger("RegistrationPageActions")

    @classmethod
    def reg_page(cls):
        cls.log.info("on reg page")
