from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import pymysql

page_per=0
#处理点击继续阅读
#参数：网页地址
#返回driver
def getNoPage(url):
    button_more_xpath='//div[@class="banner-more-btn"]/span'
    button_next_xpath='//*[@class="next_text"]'
    option=webdriver.chrome.options.Options()
    #无界面
    option.add_argument("--headless")
    #chrome_options=option
    brower=webdriver.Chrome(chrome_options=option)
    brower.get(url)
    time.sleep(1)
    try:
        button=brower.find_element_by_xpath(button_more_xpath)
        brower.execute_script("arguments[0].click();",button)
        #WebDriverWait(brower,2).until(lambda x:x.find_element_by_xpath(button_next_xpath))
        time.sleep(1)
    finally:
        return brower

#处理限制显示（百度文库一次只能显示5页）
#参数：网页地址
#返回字符串结果
def getHtml(url):
    title_xpath='//span[@id="doc-tittle-0"]'
    artical=[]
    brower=getNoPage(url)
    title=brower.find_element_by_xpath(title_xpath)
    artical.append(title.text)
    #一次拿一页，滚动条每次重新定位
    xpath="//div[@class='reader-txt-layer']/div/p/text()"
    postion="pageNo-"
    xpath_page_count="//span[@class='page-count']"
    page_size=int(brower.find_element_by_xpath(xpath_page_count).text[1:])
    res=""
    for i in range(page_size):
        #print(i)
        temp_postion="//div[@id='"+postion+str(i+1)+"']"
        #print(temp_postion)
        temp_xpath=temp_postion+xpath
        #print(temp_xpath)   
        #WebDriverWait(brower,5).until(lambda x:x.find_element_by_xpath(temp_postion))
        scroll=brower.find_element_by_xpath(temp_postion)
        result=brower.execute_script("arguments[0].scrollIntoView();",scroll)
        time.sleep(1)
        res+=getInfoNeed(brower.page_source,temp_xpath)
        global page_per
        page_per=((i+1)*100//page_size)
        #print("in"+str(page_per))
        #print(res)
    brower.close()
    artical.append(res)
    return artical

def get_page_count():
    xpath_page_count="//span[@class='page-count']"
    page_size=int(brower.find_element_by_xpath(xpath_page_count).text[1:])
    return page_size

#参数：网页html，查找内容xpath
def getInfoNeed(html,xpath):
    hxml=etree.HTML(html)
    #此处都是为了及时加载
    res=""
    count=0;
    while(count<5):
        res=hxml.xpath(xpath)
        if len(res)>0:
            break
        count+=1
        time.sleep(1)
    return "".join(res)

def saveArtical(title,content):
    sqlStr="insert into works_artical(title,content) values"
    conn=pymysql.connect("localhost","root","123456","pythondb")
    cursor=conn.cursor()
    cursor.execute(sqlStr+"(%s,%s)",(title,content))
    conn.commit()
    cursor.close()
    conn.close()

def test1():
    #百度文库一次最多显示5页
    #url="https://wenku.baidu.com/view/2b6865db16fc700aba68fc29.html?from=search"
    #url="https://wenku.baidu.com/view/95a980a9a45177232e60a246.html?from=search"
    #url="https://wenku.baidu.com/view/8c52232d1fd9ad51f01dc281e53a580216fc50fe.html?from=search"
    '''url="https://wenku.baidu.com/view/3a7bfb670b1c59eef8c7b45f.html"
    res=getHtml(url)
    saveArtical(res[0],res[1])
    url="https://wenku.baidu.com/view/e99b0c28453610661ed9f4c5.html"
    res=getHtml(url)
    saveArtical(res[0],res[1])'''
    #print(res[0])
    #print(res[1])
    #获取文库标题
    #获取文库内容
    '''res=getHtml(url)
    print(res[0])
    print(res[1])'''

#test1()
