import requests
from bs4 import BeautifulSoup

class BookText:
    def __init__(self):
        self.url = 'https://www.gutenberg.org/files/11/11-h/11-h.htm'
        self.html = self.get_html()

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def get_book_text(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        return soup.get_text()[:5000]

if __name__ == "__main__":
    book = BookText()
    text = book.get_book_text()
    with open('text.txt', 'w', encoding='utf-8') as f:
        f.write(text)
