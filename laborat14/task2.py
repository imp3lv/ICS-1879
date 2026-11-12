import requests
import random

h = {'User-Agent': 'Mozilla/5.0'}
links = ['https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg',
         'https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png',
         'https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg',
         'https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg',
         'https://upload.wikimedia.org/wikipedia/commons/d/d5/Rust_programming_language_black_logo.svg',
         'https://upload.wikimedia.org/wikipedia/commons/0/05/Go_Logo_Blue.svg',
         'https://upload.wikimedia.org/wikipedia/commons/2/27/PHP-logo.svg',
         'https://upload.wikimedia.org/wikipedia/commons/b/bd/Logo_C_sharp.svg',
         'https://upload.wikimedia.org/wikipedia/commons/7/73/Ruby_logo.svg',
         'https://upload.wikimedia.org/wikipedia/commons/9/9d/Swift_logo.svg']
random.shuffle(links)
for i in range(5):
    link = links[i]
    image = requests.get(link, headers=h)
    print(image.status_code)
    with open('picture' + str(i) + '.' + link.split('.')[-1], 'wb') as f:
        f.write(image.content)
