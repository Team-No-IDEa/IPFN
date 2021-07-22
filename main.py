from bs4 import BeautifulSoup
import requests

def main():
    print(get_title("https://www.historyofvaccines.org/content/articles/do-vaccines-cause-autism"))

def get_title(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string
    return title

if __name__ == "__main__":
    main()
