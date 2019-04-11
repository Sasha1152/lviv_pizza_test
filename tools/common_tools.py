from selenium.webdriver.common.keys import Keys
import os
from importlib import import_module

def get_class_names():
    classes = {}
    filenames = os.listdir('../page_objects')
    for f in filenames:
        name = f.split('.')[0]
        class_name = ''.join(x.capitalize() or '_' for x in name.split('_'))
        if class_name == 'GeneralPage' or class_name == '__Pycache__':
            continue
        classes[name] = class_name
    return classes

classes = get_class_names()
for name, class_name in classes.items():
    path = f'page_objects.{name}'
    mod = import_module(path)
    globals()[class_name] = eval('mod.' + class_name)


def set_dynamic_instances(context):
    for name, class_name in classes.items():
        class_obj = globals()[class_name](context.browser)
        setattr(context, name, class_obj)
    return context


def type_in_textfield(context, text_to_type):
    element = context.browser.find_element_by_name(context.google_page.search_field_name)
    element.click()
    element.send_keys(text_to_type)
    element.send_keys(Keys.RETURN)
