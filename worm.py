#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv
import func


url = "http://www.newsmth.net/nForum/board/PieLove?ajax&p={page}"

#已完成的页数序号，初时为0
page = 0

csv_file = open("tinsghua.csv","wb")
csv_writer = csv.writer(csv_file, delimiter=',')
while page < 100:
    page += 1
    print "fetch: ", url.format(page=page)
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text,'html5lib')
    title_list = html.select(".board-list.tiz tr")
    del title_list[0]
    for title in title_list:
        a = title.select(".title_9 a")
        artitle = a[0].attrs

        href = artitle['href']

        name =  a[0].text

        b = title.select(".title_10")
        ctime = b[0].text

        if(func.compare_time(ctime)):
            csv_writer.writerow([name.encode('utf-8'), href.encode('utf-8'), ctime.encode('utf-8')])
        else:
            continue



    print 1



csv_file.close()

