from page_objects.general_page import GeneralPage

class GooglePage(GeneralPage):
    search_field_name = 'q'
    text_to_search = 'pizza lviv'
    start_page_url = 'http://www.google.com'

    def goto_start_page(self, context):
        return context.browser.get('http://www.google.com')
