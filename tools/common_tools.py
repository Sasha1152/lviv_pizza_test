from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_on_link(context, link_text):
    element = context.browser.find_element_by_link_text(link_text)
    element.click()

def element_is_clickable(context, text):
    try:
        WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT(text)))
        )
        return True
    except:
        pass
