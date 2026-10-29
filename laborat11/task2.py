import json

books = {}
n = int(input("Скільки книг? "))

for i in range(n):
    title = input("Назва книги: ")
    author = input("Автор: ")
    books[title] = author

with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False)

print(books)
