from selenium.webdriver.common.keys import Keys


def type_in_textfield(context, text_to_type):
	element = context.browser.find_element_by_name(context.googlepage.search_field_name)
	element.click()
	element.send_keys(text_to_type)
	element.send_keys(Keys.RETURN)

