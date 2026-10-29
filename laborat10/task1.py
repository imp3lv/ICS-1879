import re

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower().replace('’', "'")

words = re.findall(r"[a-z]+(?:['-][a-z]+)*", text)
unique_words = sorted(set(words))

print("Кількість оригінальних слів:", len(unique_words))

with open('output.txt', 'w', encoding='utf-8') as f:
    for word in unique_words:
        f.write(word + '\n')
