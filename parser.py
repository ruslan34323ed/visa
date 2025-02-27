import requests
from bs4 import BeautifulSoup
from config import URL

def fetch_latest_news():
    """
    Получает последние новости со страницы и возвращает дату, заголовок и текст.
    """
    response = requests.get(URL)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем первый блок новости
    news_block = soup.find('div', class_='d-flex py-4 align-items-start align-items-md-baseline mt-4')
    if not news_block:
        return None

    date_tag = news_block.find('u')  # Дата новости
    title_tag = news_block.find('h3')  # Заголовок новости

    news_date = date_tag.text.strip() if date_tag else "Неизвестная дата"
    news_title = title_tag.text.strip() if title_tag else "Без заголовка"
    news_content = news_block.text.strip()  # Получаем весь текст блока

    return news_date, news_title, news_content
