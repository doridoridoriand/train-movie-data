contents = open('result.log').readlines()

urls = []
for content in contents:
    if content.replace('\n', '').split(' ')[-1] == '5':
        frame = content.split(' ')[2][9:]
        seconds = str(int(int(frame) / 25))
        source_url = 'https://www.youtube.com/watch?v=fYB1Ovpd0nc&t='
        urls.append(source_url + seconds + 's')

for url in sorted(set(urls)):
    print(url)
