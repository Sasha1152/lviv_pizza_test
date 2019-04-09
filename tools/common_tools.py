from selenium.webdriver.common.keys import Keys
import os
from page_objects.google_page import GooglePage
from page_objects.pizzalviv_page import PizzalvivPage

def type_in_textfield(context, text_to_type):
	element = context.browser.find_element_by_name(context.classes['googlepage'].search_field_name)
	element.click()
	element.send_keys(text_to_type)
	element.send_keys(Keys.RETURN)


def get_file_names():
	filenames = os.listdir('../page_objects')
	return [f.split('.')[0] for f in filenames]


def get_class_names():
	filenames = get_file_names()
	filenames = [f.split('_') for f in filenames]
	classes_words = []
	for words in filenames:
		l = [word.title() for word in words]
		classes_words.append(l)
	classes_names = [''.join(word) for word in classes_words]
	return classes_names


def get_instance(class_name):
	try:
		return eval(class_name)(context.browser)
	except NameError:
		return False


list_filenames = get_file_names()
list_classnames = get_class_names()

def get_instance_all_classes():
	instances = {}
	for i in range(len(list_classnames)):
		instances[list_filenames[i]] = get_instance(list_classnames[i])

	return instances

# def get_context_inst_all_classes(context):
# 	instances = get_instance_all_classes()
# 	for key, value in instances.items():
# 		instances[key] = context.value
# 	return instances