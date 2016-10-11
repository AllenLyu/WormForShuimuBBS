# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv
import func
import re

TOPIC_LINE = '#################################################################'
REPOST_LINE = '-----------------------------------------------------------------'
URL_PREFIX = 'http://www.newsmth.net'
URL_SUFFIX = '?p={page}'

detail_file = open('detail.txt', 'w')


def main():
    csv_file = open("tinsghua.csv", "r")
    reader = csv.reader(csv_file, delimiter=',')
    i = 0
    while i < 5:
        i += 1
        line = reader.next()
        detail_file.write(line[0]+'\n')
        detail_file.write(TOPIC_LINE + '\n')

        get_topic(URL_PREFIX + line[1] + URL_SUFFIX)
        print 1

        detail_file.write('\n\n\n\n\n')


def get_topic(url):
    page = 1
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text, 'html5lib')
    page_count = html.select('.t-pre ')[0].select('.page-main li')
    if len(page_count) > 1:
        page_count = len(page_count) - 1
    else:
        page_count = len(page_count)
    art_list = html.select('.a-content p')

    line = art_list[0].text.encode('utf-8') + '\n'

    line = re.sub('(.*, 站内)', '', line)
    line = re.sub('(--    ※ 来源.*)', '', line)
    detail_file.write(line)

    detail_file.write(TOPIC_LINE + '\n')

    del (art_list[0])
    for art in art_list:
        line = art.text.encode('utf-8') + '\n'

        line = re.sub('(.*, 站内)', '', line)
        line = re.sub('(--    ※ 来源.*)', '', line)
        detail_file.write(line)

        detail_file.write(REPOST_LINE + '\n')
    get_post(url, page_count)


def get_post(url, page):
    if page == 1:
        return
    else:
        i = 2
        while i < page:
            i += 1
            response = requests.get(url.format(page=i))
            html = BeautifulSoup(response.text, 'html5lib')
            art_list = html.select('.a-content p')
            for art in art_list:
                line = art.text.encode('utf-8') + '\n'

                line = re.sub('(.*, 站内)', '', line)
                line = re.sub('(--    ※ 来源.*)', '', line)
                detail_file.write(line)

                detail_file.write(REPOST_LINE + '\n')


main()
