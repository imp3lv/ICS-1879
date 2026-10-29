def remove_extra_spaces(line):
    return ' '.join(line.split())

with open('engtext.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

print("До:")
for line in lines:
    print(line)

print("Після:")
for line in lines:
    print(remove_extra_spaces(line))
