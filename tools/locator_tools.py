from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

locators = {
        "id": By.ID,
        "xpath": By.XPATH,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT,
        "name": By.NAME,
        "tag_name": By.TAG_NAME,
        "class_name": By.CLASS_NAME,
        "css_selector": By.CSS_SELECTOR
    }


def element_is_clickable(context, locator, text):
    try:
        WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((locators[locator](text)))
        )
        return True
    except TypeError:
        print("the element wasn't clickable")
        return False


def click_on_link(context, locator, text):
    try:
        context.browser.find_element(locators[locator], text).click()
        return True
    except NoSuchElementException:
        return False


def element_exist(context, locator, text):
    try:
        context.browser.find_element(locators[locator], text).is_displayed()
        return True
    except NoSuchElementException:
        return False

def find_element(context, locator, text):
    try:
        return context.browser.find_element(locators[locator], text)
    except NoSuchElementException:
        return False
