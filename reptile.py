from bs4 import BeautifulSoup as bs
import requests

def get_article_list():
    res = requests.get('https://www.ptt.cc/bbs/Tech_Job/index.html')
    soup = bs(res.text,'lxml')

    raw_titles = soup.select('.title > a')
    results = []
    for i in raw_titles:
        result = {}
        result['topic'] = i.text
        result['url'] = 'https://www.ptt.cc' + i.get('href') 
        #可以在抓下來的網址前面加上ptt的url標頭
        results.append(result)

    return results

#2454 M 3034 N 2330 GG 3711 moon
def search_stock_price(stock_num): 
    url = 'https://tw.stock.yahoo.com/quote/' + stock_num
    result = list() # 最終結果
    
    response = requests.get(url)
    soup = bs(response.text, 'lxml')

    stock_name = soup.find('h1', {'class': 'C($c-link-text) Fw(b) Fz(24px) Mend(8px)'}).getText()
    stock_date = soup.find('span', {'class': 'C(#6e7780) Fz(14px) As(c)'}).getText().replace('資料時間：', '')

    market_date = stock_date[0:10]  #日期
    market_time = stock_date[11:16]  #時間

    stock_price = soup.find('span', {'class': 'Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c)'}).getText()
    data = (market_date, market_time, stock_name, stock_price)

    return data

def get_wiki(company):
    res = requests.get('https://zh.wikipedia.org/wiki/{}'.format(company))
    soup = bs(res.text, 'lxml')
    article = soup.select_one('.mw-parser-output p').text

    return article