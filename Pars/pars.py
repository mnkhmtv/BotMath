from bs4 import BeautifulSoup
import requests


def get_html(url):
    r = requests.get(url)

    return r.text


def get_all_texts(html):
    soup = BeautifulSoup(html, 'lxml')

    divs = soup.find_all('div',class_ = 'wrapper')

    texts = []
    

    for div in divs:
        a = div.find('p', class_ = 'left_margin' ).get('p')
        texts.append(a)

        return texts


def main():
    url = 'https://math-ege.sdamgia.ru'
    
    all_texts = get_all_texts(get_html(url))

    for i in all_texts:
        print(i)

print(get_all_texts)


if __name__ == '__main__':
    main()