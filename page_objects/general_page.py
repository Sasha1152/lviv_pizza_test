class GeneralPage:
    def __init__(self, browser):
        self.browser = browser

    def get_title(self, context):
        return context.browser.title
