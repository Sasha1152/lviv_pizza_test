from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.common_tools import click_on_link, element_is_clickable


@when('I have opened google starting page')
def step(context):
    context.browser.get('http://www.google.com')
    assert context.browser.title == "Google"

@then('I have written text to the textbox')
def step(context):
    element = context.browser.find_element_by_name("q")
    element.click()
    element.send_keys("pizza lviv")
    element.send_keys(Keys.RETURN)


@then("I click on the 'pizzalviv.com' link")
def step(context):
    element = context.browser.find_element_by_partial_link_text("pizzalviv.com")
    element.click()
    assert context.browser.title == "Доставка піци Львів"


@then("I click on the 'Піца' button")
def step(context):
    click_on_link(context, 'Піца')

@then("I select all available kind of pizzazz")
def step(context):
    click_on_link(context, 'Всі')
    assert "замовлення" in context.browser.page_source


@then("I click on the 'Pepperoni' pizza")
def step(context):
    if element_is_clickable(context, 'Pepperoni'):
        click_on_link(context, 'Pepperoni')

@then("I click on the 'add to the basket' button")
def step(context):
    if element_is_clickable(context, 'Додати в кошик'):
        click_on_link(context, 'Додати в кошик')


@then("I click on the 'my orders' button")
def step(context):
    try:
        WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME('corner left')))
        )
        element = context.browser.find_element_by_class_name('corner left')
        element.click()
    except:
        pass


@then("I click on the 'remove order' button")
def step(context):
    try:
        WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR(
                'a.button has_popup inl vmid removeFromCart cartPage'
            )))
        )
        element = context.browser.find_element_by_css_selector(
            'a.button has_popup inl vmid removeFromCart cartPage'
        )
        element.click()
    except:
        pass
