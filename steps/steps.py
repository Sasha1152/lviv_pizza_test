from behave import when, then

from tools.locator_tools import click_on_link, element_is_clickable, element_exist
from tools.common_tools import type_in_textfield

@when('I have opened google starting page')
def step(context):
    context.classes['googlepage'].goto_start_page(context)
    assert context.classes['googlepage'].get_title(context) == "Google"


@then('I have written text to the textbox')
def step(context):
    type_in_textfield(context, context.classes['googlepage'].text_to_search)


@then("I click on the 'pizzalviv.com' link")
def step(context):
    element = context.browser.find_element_by_partial_link_text("pizzalviv.com")
    element.click()
    assert context.classes['pizzalvivpage'].get_title(context) == "Доставка піци Львів"


@then("I click on the 'Піца' button")
def step(context):
    click_on_link(context, 'link_text', 'Піца')
    assert context.classes['pizzalvivpage'].get_title(context) == "Піца | Доставка піци Львів"


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
