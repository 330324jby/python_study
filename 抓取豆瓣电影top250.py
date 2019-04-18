import requests
from lxml import etree
import pymysql
import json
#豆瓣 https://movie.douban.com/top250?start=0&filter=

def getHtmls():
    request=""
    for i in range(10):
        request+=requests.get(\
            "https://movie.douban.com/top250?start=%d&filter="%(25*i)\
            ).text
    return request

def getNames(htmls):
    obHtml=etree.HTML(htmls)     
    return obHtml.xpath("//div[@class='hd']/a/span[1]/text()")

def saveNames(names):
    conn=pymysql.connect("localhost","root","123456","pythondb")
    cursor=conn.cursor()
    cursor.executemany("insert into works_movie_name(name) values(%s)",names)
    conn.commit()
    cursor.close()
    conn.close()

def main():
    #print(getNames(getHtmls()))
    saveNames(getNames(getHtmls()))
    #print(list(getNames()[:10]))
    '''movieNames=[]
    for i in getNames()[:10]:
        movieNames.append(i[1])
    print(movieNames)'''
    #print(json.dumps(getStores(),ensure_ascii=False))

main()
