from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.historyofvaccines.org/content/articles/do-vaccines-cause-autism"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.title.string)

if __name__ == "__main__":
    main()
