import random
import webbrowser
from pathlib import Path
from urllib.parse import urlparse

PROJECT_DIR = Path(__file__).parent


def open_random_articles(num_of_articles=2):
    selected_articles = []
    unique_domains = set()

    with open(f"{PROJECT_DIR}/articles.txt", 'r') as articles:
        valid_articles_with_domain_and_index = []

        all_articles = articles.readlines()
        for index in range(len(all_articles)):
            article = all_articles[index]

            # filter by read articles
            if article[0] == '*':
                continue

            article_domain = urlparse(article).netloc
            unique_domains.add(article_domain)

            valid_articles_with_domain_and_index.append((article, article_domain, index))

        while len(selected_articles) < num_of_articles:
            (article_url, article_domain, article_index) = random.choice(valid_articles_with_domain_and_index)

            article_url_string = str(article_url)

            # removes newline
            selected_articles.append(article_url_string.rstrip())

            # Mark article as read
            all_articles[article_index] = "*" + article_url_string

            # remove other articles with same domain if we have more than one domain available
            if len(unique_domains) > 1:
                valid_articles_with_domain_and_index = [(a, domain, i) for (a, domain, i) in
                                                        valid_articles_with_domain_and_index if
                                                        domain != article_domain]
                unique_domains.remove(article_domain)

    # updates read articles in txt
    with open(f"{PROJECT_DIR}/articles.txt", 'w') as articles:
        articles.writelines(all_articles)

    for selected_article in selected_articles:
        webbrowser.open_new(selected_article)


if __name__ == '__main__':
    open_random_articles()
