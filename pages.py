class GeneralPage:
    def __init__(self, browser):
        self.browser = browser


class GooglePage(GeneralPage):
    search_field_name = 'q'
    text_to_search = 'pizza lviv'
    start_page_url = 'http://www.google.com'


class PizzaLvivPage(GeneralPage):
    start_page_pizza_title = 'Доставка піци Львів'
