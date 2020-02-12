from selenium.webdriver.common.by import By


class WelcomePageObjects:

    SIGN_ON_LINK = (By.XPATH, "//a[contains(text(),'SIGN-ON')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'REGISTER')]")
    SUPPORT_LINK = (By.XPATH, "//a[contains(text(),'SUPPORT')]")
    CONTACT_LINK = (By.XPATH, "//a[contains(text(),'CONTACT')]")
    USER_NAME_FIELD = (By.XPATH, "//input[@name='userName']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SIGN_IN_BTN = (By.XPATH, "//input[@name='login']")
