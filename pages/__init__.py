from selenium import webdriver
from pages.home_page import HomePage


def get_starting_page(driver: webdriver.Remote, base_url: str) -> webdriver:
    driver.get(base_url)
    return HomePage(driver)
