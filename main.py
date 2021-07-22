from bs4 import BeautifulSoup
import requests
from googlesearch import search
from htmldate import find_date

def main():
    print(get_title("https://www.historyofvaccines.org/content/articles/do-vaccines-cause-autism"))
    query = get_title("https://www.historyofvaccines.org/content/articles/do-vaccines-cause-autism")

    print(get_similar_sites(query))
    sites = get_similar_sites(query)

    print(date_of_sites(sites))
    dates = date_of_sites(sites)

    print(combine_website_and_date(sites, dates))
    final_list = combine_website_and_date(sites, dates)

    print(sorted(final_list, key=take_second))

def get_title(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string
    return title

def get_similar_sites(query: str) -> list:
    result = []
    for i in search(str(query), tld="com", num=5, stop=5, pause=2):
        result.append(i)
    return result

def date_of_sites(sites: list) -> list:
    result = []
    for site in sites:
        result.append(find_date(site))
    return result

def combine_website_and_date(sites: list, dates: list) -> list:
    return list(zip(sites, dates))

def take_second(elem):
    return elem[1]


if __name__ == "__main__":
    main()
