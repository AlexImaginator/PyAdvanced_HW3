import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from decorators import log_func


@log_func()
def parse_habr(keywords):
    base_url = 'https://habr.com'
    get_articles_url = 'https://habr.com/ru'
    headers = Headers(os='windows', browser='firefox', headers=True).generate()
    select_articles = []
    response = requests.get(get_articles_url, headers=headers)
    soup_articles_list = BeautifulSoup(response.text, 'html.parser')
    articles = soup_articles_list.find_all('article')
    for article in articles:
        p_preview_items = article.find(class_="article-formatted-body").find_all('p')
        preview = ' '.join([item.text for item in p_preview_items])
        if len(preview) < 1:
            preview = article.find(class_="article-formatted-body").text
        set_preview = set(preview.split(' '))
        href = article.find(class_="tm-article-snippet__title-link").get('href')
        response = requests.get(f'{base_url}{href}', headers=headers)
        soup_article_body = BeautifulSoup(response.text, 'html.parser')
        article_body = soup_article_body.find(class_="article-formatted-body").find('div').text
        set_article_body = set(article_body.split(' '))
        set_article_text = set_article_body.union(set_preview)
        set_cheking = set_article_text.intersection(set(keywords))
        if len(set_cheking) > 0:
            datetime_stamp = article.find(class_="tm-article-snippet__datetime-published").find('time')['title']
            article_title = article.find(class_="tm-article-snippet__title-link").find('span').text
            article_disp = {
                'datetime_stamp': datetime_stamp,
                'article_title': article_title,
                'href': f'{base_url}{href}'
            }
            select_articles.append(article_disp)
    return select_articles
        