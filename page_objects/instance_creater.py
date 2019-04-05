from page_objects import google_page, pizzalviv_page

def create_instances_of_pages(context, browser):
	context.googlepage = google_page.GooglePage(browser)
	context.pizzalvivpage = pizzalviv_page.PizzaLvivPage(browser)
