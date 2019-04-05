from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from page_objects.instance_creater import create_instances_of_pages
from page_objects.pizzalviv_page import PizzaLvivPage
from tools.locator_tools import click_on_link


def before_all(context):
	context.browser = webdriver.Chrome()
	context.browser.set_page_load_timeout(10)
	context.browser.implicitly_wait(10)
	create_instances_of_pages(context, context.browser)
	# context.google_page = GooglePage(context.browser)
	# context.pizzalviv_page = PizzaLvivPage(context.browser)
	# context.browser.maximize_window()

def before_step(context, step):
	"""This function checks if a popup is active"""
	try:
		context.browser.find_element_by_class_name('popup_start popup_window active')
		click_on_link(context, 'class_name', 'close_popup')
	except NoSuchElementException:
		print("the popup wasn't detected")


def after_all(context):
	# context.browser.save_screenshot("screenshot.png")
	context.browser.quit()
