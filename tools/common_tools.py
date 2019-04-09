from selenium.webdriver.common.keys import Keys
import os


def type_in_textfield(context, text_to_type):
	element = context.browser.find_element_by_name(context.classes['googlepage'].search_field_name)
	element.click()
	element.send_keys(text_to_type)
	element.send_keys(Keys.RETURN)


def get_files_names():
	filenames = os.listdir('../page_objects')
	return [f.split('.')[0] for f in filenames]
print(get_files_names())

def get_classes_names():
	filenames = get_files_names()
	filenames = [f.split('_') for f in filenames]
	classes_words = []
	for words in filenames:
		l = [word.title() for word in words]
		classes_words.append(l)
	classes_names = [''.join(word) for word in classes_words]
	return classes_names

print(get_classes_names())

# def get_instanses_of_classes():
var = get_files_names()[0]
exec(f'{var} = 100')
print(google_page)
eval(get_classes_names()[0])
classname_obj = GooglePage
print(classname_obj)
google_page = classname_obj(context)

print(google_page)
