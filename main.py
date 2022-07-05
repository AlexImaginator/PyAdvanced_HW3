from parse import parse_habr


if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    select_articles = parse_habr(KEYWORDS)
    for item in select_articles:
        print(f'{item["datetime_stamp"]} - {item["article_title"]} - {item["href"]}')
