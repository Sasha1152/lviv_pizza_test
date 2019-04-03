class GooglePage:
    search_field_name = 'q'
    text_to_search = 'pizza lviv'
    start_page_url = 'http://www.google.com'

    def __init__(self, browser):
        self.browser = browser

    # def search_text(self):
    #     self.browser.find_element_by_css_selector(search_field)


class PizzaLvivPage:
    start_page_pizza_title = 'Доставка піци Львів'

    def __init__(self, browser):
        self.browser = browser