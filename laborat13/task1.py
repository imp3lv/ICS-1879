class Book:
    def __init__(self, name, author, publisher, year, pages):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages

    def set_year(self, y):
        self.year = y

    def set_pages(self, p):
        self.pages = p


books = []

b1 = Book('Кобзар', 'Шевченко', 'Знання', 2010, 320)
b2 = Book('Захар Беркут', 'Франко', 'Ранок', 2015, 256)
books.append(b1)
books.append(b2)

b1.set_year(2020)
b1.set_pages(350)

b3 = Book('Лісова пісня', 'Леся Українка', 'Основа', 2012, 180)
books.append(b3)

books.remove(b2)

for b in books:
    print(b.name, b.author, b.publisher, b.year, b.pages)
