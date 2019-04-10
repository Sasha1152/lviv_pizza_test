from selenium.webdriver.common.keys import Keys
import os
from importlib import import_module


filenames = os.listdir('../page_objects')
for f in filenames:
    name = f.split('.')[0]
    class_name = ''.join(x.capitalize() or '_' for x in name.split('_'))
    if class_name == 'GeneralPage' or class_name == '__Pycache__':
        continue
    path = f'page_objects.{name}'
    mod = import_module(path)
    globals()[class_name] = eval('mod.' + class_name)


def type_in_textfield(context, text_to_type):
    element = context.browser.find_element_by_name(context.google_page.search_field_name)
    element.click()
    element.send_keys(text_to_type)
    element.send_keys(Keys.RETURN)


def set_dynamic_instances(context):
    filenames = os.listdir('../page_objects')
    for f in filenames:
        name = f.split('.')[0]
        class_name = ''.join(x.capitalize() or '_' for x in name.split('_'))
        if class_name == 'GeneralPage' or class_name == '__Pycache__':
            continue
        class_obj = globals()[class_name](context.browser)
        setattr(context, name, class_obj)
    return context
