'''
该代码用于个人python课程学习
python大作业的“自动化网站挑选”部分
2024/1/1
'''
from selenium import webdriver
import logging
import time

def get_urls():
    with open('website.txt', 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file]
    return urls

def time_test(urls):
    new_urls = set()
    driver = webdriver.Chrome()
    try:
        driver.implicitly_wait(10)
        for url in urls:
            start_time = time.time()
            driver.get(url)
            elapsed_time = time.time() - start_time
            if (elapsed_time >= 5 or driver.current_url != url or "Error" in driver.title):
                logger.info(f'Skipping {url} due to conditions.')
            else:
                new_urls.add(url)
                logger.info(f'Title of {url}: {driver.title}, Time: {elapsed_time:.2f}s')
    finally:
        driver.quit()
    return new_urls

def website_export(urls):
    with open('new_website.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(urls))
    print('finished!')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    urls = get_urls()
    new_urls = time_test(urls)
    website_export(new_urls)
