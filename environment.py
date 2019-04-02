from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def before_all(context):
	context.browser = webdriver.Chrome()
	context.browser.set_page_load_timeout(10)
	context.browser.implicitly_wait(10)
	# context.browser.maximize_window()

def before_step(context, step):
	"""This function checks if a popup is active"""
	try:
		context.browser.find_element_by_class_name('popup_start popup_window active')
		context.browser.find_element_by_class_name('close_popup').click()
	except:
		pass

def after_all(context):
	# context.browser.quit()
	pass