from selenium.webdriver.common.by import By
from pages.base import BasePage


class HomePage(BasePage):

    class Locators:
        HOME_PAGE_TITLE = By.XPATH, "//h3"

    def get_page_title(self):
        return self.get_element(self.Locators.HOME_PAGE_TITLE).text
