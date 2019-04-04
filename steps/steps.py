from behave import when, then
from selenium.webdriver.common.keys import Keys

from tools.common_tools import click_on_link, element_is_clickable, element_exist


@when('I have opened google starting page')
def step(context):
    context.browser.get(context.google_page.start_page_url)
    assert context.browser.title == "Google"

@then('I have written text to the textbox')
def step(context):
    element = context.browser.find_element_by_name(context.google_page.search_field_name)
    element.click()
    element.send_keys(context.google_page.text_to_search)
    element.send_keys(Keys.RETURN)


@then("I click on the 'pizzalviv.com' link")
def step(context):
    element = context.browser.find_element_by_partial_link_text("pizzalviv.com")
    element.click()
    assert context.browser.title == context.pizzalviv_page.start_page_pizza_title


@then("I click on the 'Піца' button")
def step(context):
    click_on_link(context, 'link_text', 'Піца')


@then("I click 'next' button until find the 'Pepperoni' pizza")
def step(context):
    while not element_exist(context, 'link_text', 'Pepperoni'):
        if element_is_clickable(context, 'link_text', 'Наступна'):
            click_on_link(context, 'link_text', 'Наступна')
        else:
            break


@then("I click on the 'Pepperoni' pizza")
def step(context):
    if element_is_clickable(context, 'link_text', 'Pepperoni'):
        click_on_link(context, 'link_text', 'Pepperoni')

@then("I click on the 'add to the basket' button")
def step(context):
    if element_is_clickable(context, 'link_text', 'Додати в кошик'):
        click_on_link(context, 'link_text', 'Додати в кошик')


@then("I click on the 'my orders' button")
def step(context):
    if element_is_clickable(context, 'class_name', 'corner left'):
        click_on_link(context, 'class_name', 'corner left')


@then("I click on the 'remove order' button")
def step(context):
    if element_is_clickable(context, 'css_selector', 'a.button has_popup inl vmid removeFromCart cartPage'):
        click_on_link(context, 'css_selector', 'a.button has_popup inl vmid removeFromCart cartPage')
