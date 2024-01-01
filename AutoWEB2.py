'''
该代码用于个人python课程学习
python大作业的“自动化网址收集”部分
2024/1/1
'''
import time
from selenium import webdriver
from bs4 import BeautifulSoup
#from selenium.webdriver.common.by import By
'''对于'http://www.sodzs123.com/wangzhan/'网站的信息采集，但https的url过少
def get_urls1():
    base_url = 'http://www.sodzs123.com/wangzhan/'
    urls = set()
    with webdriver.Chrome() as driver: # 使用Chrome浏览器驱动
        driver.get(base_url)           # get请求

        time.sleep(1)      # 等待1s,使用XPath选择所有带有onclick属性的span元素
        page_urls = driver.find_elements(By.XPATH, '//span[@onclick]')
        for page_url in page_urls: # 遍历每个span元素，提取onclick属性中的URL
            onclick_value = page_url.get_attribute('onclick')
            url = onclick_value.split("'")[1]#分割+添加
            urls.add(url)

    return urls
'''
def get_urls2():
    base_url = 'http://www.soxs123.com/'
    urls = set()
    with webdriver.Chrome() as driver:
        driver.get(base_url)

        time.sleep(1)  #等待
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        # 使用find_all方法选择所有带有'target'属性为'_blank'的a元素
        page_urls = soup.find_all('a', {'target': '_blank'})
        for page_url in page_urls:
            # 遍历每个a元素，提取href属性中的URL
            url = page_url['href']
            urls.add(url)

    return urls


# 提取网址部分
def match_urls(ori_urls):
    lines = '\n'.join(result_urls)
    urls = [url.strip() for url in lines.split('\n') if url.startswith('https://')]
    return urls

# 写入文件
def website_export(urls):
    now = str(time.time())
    with open(now+'website.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(urls))
    print('finished!')



if __name__ == "__main__":
    result_urls = get_urls2()
    new_urls = match_urls(result_urls)
    website_export(new_urls)