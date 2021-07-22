from bs4 import BeautifulSoup
import requests
from googlesearch import search
from htmldate import find_date
import validators

class IPFN():
    def get_title(self, url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        return title

    def get_similar_sites(self, query: str) -> list:
        result = []
        for i in search(str(query), tld="com", num=5, stop=5, pause=2):
            result.append(i)
        return result

    def date_of_sites(self, sites: list) -> list:
        result = []
        for site in sites:
            result.append(find_date(site))
        return result

    def combine_website_and_date(self, sites: list, dates: list) -> list:
        return list(zip(sites, dates))

    def take_second(self, elem):
        return elem[1]

    def validate_url(self, url: str) -> bool:
        return validators.url(url)

    def main(self):
        print(self.get_title("https://www.historyofvaccines.org/content/articles/do-vaccines-cause-autism"))
        query = self.get_title("https://www.historyofvaccines.org/content/articles/do-vaccines-cause-autism")

        print(self.get_similar_sites(query))
        sites = self.get_similar_sites(query)

        print(self.date_of_sites(sites))
        dates = self.date_of_sites(sites)

        print(self.combine_website_and_date(sites, dates))
        final_list = self.combine_website_and_date(sites, dates)

        print(sorted(final_list, key=self.take_second))
        

if __name__ == "__main__":
    a = IPFN()
    a.main()
