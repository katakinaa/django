import requests
from bs4 import BeautifulSoup as BS

URL = "https://rezka.ag"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
}


# start
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


# get data
def get_data(html):
    bs = BS(html, "html.parser")
    items = bs.find_all("div", class_='b-content__inline_item')
    rezka_list = []
    for item in items:
        title = item.find("div", class_="b-content__inline_item-link").get_text(strip=True)
        image = URL + item.find("div", class_="b-content__inline_item-cover").find("img").get("src")
        rezka_list.append({"title": title, "image": image})
    return rezka_list


# parsing
def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        rezka_list_2 = []
        for page in range(1, 2):  # измените диапазон, чтобы начать с 1
            response = get_html('https://rezka.ag/films/', params={'page': page})  # передайте параметры правильно
            rezka_list_2.extend(get_data(response.text))
        return rezka_list_2
    else:
        raise Exception('Ошибка при парсинге')


print(parsing())
