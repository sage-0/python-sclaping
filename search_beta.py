import requests
from bs4 import BeautifulSoup
import re
def serch_google(words, xs):
    #検索
    googleSearch = 'https://www.google.co.jp/search'
    response = requests.get(googleSearch, params={'q': words,'num': xs})
    #結果取得
    soup = BeautifulSoup(response.text, "html.parser")
    elems = soup.find_all(href=re.compile("www."))
    for searchResult in elems:
        title = searchResult.text
        url = re.sub("\/url\?q=","",searchResult.get('href'))
        furl =  url.partition('&')[0]
        print('タイトル:',title)
        print('URL:',furl)
    return (title, furl)




