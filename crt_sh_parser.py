from bs4 import BeautifulSoup
import urllib.request
import sys


def main():
    if len(sys.argv) != 2:
        exit('You should provide one and only one argument: the domain!')

    parseHtml(sys.argv[1])


def parseHtml(param):

    url = 'https://crt.sh/?q={}'.format(param)
    filterby = {'Type: Identity', '*'}

    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, 'html.parser')

    subdomains = []

    for url in soup.find_all('td', string=True):
        obj = str(url.string)
        if param in obj and obj not in subdomains and param is not obj:
            subdomains.append(obj)

    for f in filterby:
        for s in subdomains[:]:
            if f in s or s == param:
                subdomains.remove(s)

    for el in subdomains:
        print(el)


main()
