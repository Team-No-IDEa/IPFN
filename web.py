from bs4 import BeautifulSoup
import requests
from googlesearch import search
from htmldate import find_date
import validators

class Web():
    @staticmethod
    def get_title(url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        return title

    @staticmethod
    def get_similar_sites(query: str) -> list:
        result = []
        for i in search(str(query), tld="com", num=5, stop=5, pause=2):
            result.append(i)
        return result

    @staticmethod
    def date_of_sites(sites: list) -> list:
        result = []
        for site in sites:
            result.append(find_date(site))
        return result

    @staticmethod
    def combine_website_and_date(sites: list, dates: list) -> list:
        return list(zip(sites, dates))

    @staticmethod
    def take_second(elem):
        return elem[1]

    @staticmethod
    def validate_url(url: str) -> bool:
        return validators.url(url)
