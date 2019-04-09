class GeneralPage:
    def __init__(self, browser):
        self.browser = browser

    def get_title(self, context):
        return context.browser.title

    @classmethod
    def create_instanses_for_all(cls, context):
        classes = {}
        for obj in cls.__subclasses__():
            inst_name = obj.__name__.lower()
            class_obj = obj(context.browser)
            classes[inst_name] = class_obj
        return classes
