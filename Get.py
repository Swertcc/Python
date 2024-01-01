from selenium import webdriver
import logging

def get_urls():
    with open('website.txt', 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file]
    return urls

driver = webdriver.Chrome()

def webtest(urls):
    try:
        driver.implicitly_wait(10)
        for url in urls:
            driver.get(url)
            logger.info(f'Title of {url}: {driver.title}')
    finally:
        driver.quit()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    urls = get_urls()
    new_urls = webtest(urls)
