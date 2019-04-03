from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def click_on_link(context, locator, text):
    element = context.browser.find_element(locators[locator], text)
    element.click()
