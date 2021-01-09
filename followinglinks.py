from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://py4e-data.dr-chuck.net/known_by_Sukveer.html"
count = int(7)
position = int(18)
for i in range(count):
    html = urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    array = list()
    targets = []
    for tag in tags:
        x = tag.get('href', None)
        array.append(x)
        y = tag.text
        targets.append(y)

    print (array[position-1])
    print (targets[position-1])
    url = array[position-1]