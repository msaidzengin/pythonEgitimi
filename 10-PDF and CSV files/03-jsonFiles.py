import json

colors = {
    'red': 'kırmızı',
    'green': 'yeşil',
    'blue': 'mavi',
    'yellow': 'sarı',
    'orange': 'turuncu',
    'purple': 'mor'
}


with open('colors.json', 'w', encoding='utf-8') as f:
    json.dump(colors, f, ensure_ascii=False, indent=4)


with open('colors.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


print(data)
