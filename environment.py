from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from page_objects.general_page import GeneralPage
from tools.locator_tools import click_on_link
from tools.common_tools import set_dynamic_instances
from page_objects.google_page import GooglePage
from page_objects.pizzalviv_page import PizzalvivPage


def before_all(context):
	context.browser = webdriver.Chrome()
	context.browser.set_page_load_timeout(10)
	context.browser.implicitly_wait(10)
	set_dynamic_instances(context)


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
