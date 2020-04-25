from splinter import Browser
from bs4 import BeautifulSoup as bs
import re
import time

def scrape():
    scrap_data={}
    browser = Browser('chrome', headless='False')

    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    # browser.is_element_present_by_css('ul.item_list li.slide', wait_time=1)
    html = browser.html
    news_soup = bs(html, 'html.parser')
    slide_elem= news_soup.select_one('ul.item_list li.slide')

    # print(slide_elem)
    # slide_elem.find('div', class_='content_title')
    news_title = slide_elem.find('div',class_='content_title').get_text()
    # news_title
    news_p = slide_elem.find('div',class_='article_teaser_body').get_text()
    # news_p
    # print(news_title)
    # print('-' * 25)
    # print(news_p)
    scrap_data['Article Title']=news_title
    scrap_data['Article P']=news_p
    return scrap_data


if __name__ == '__main__':
    print(scrape())

    