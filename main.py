from web import *

class Run():
    def __init__(self):
        print(Web.get_title("https://www.historyofvaccines.org/content/articles/do-vaccines-cause-autism"))
        query = Web.get_title("https://www.historyofvaccines.org/content/articles/do-vaccines-cause-autism")

        print(Web.get_similar_sites(query))
        sites = Web.get_similar_sites(query)

        dates = Web.date_of_sites(sites)

        final_list = Web.combine_website_and_date(sites, dates)

        print(sorted(final_list, key=Web.take_second))

if __name__ == "__main__":
    a = Run()