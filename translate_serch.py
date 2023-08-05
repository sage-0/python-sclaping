from googletrans import Translator
import re
from bs4 import BeautifulSoup
import requests

def translate_google(wtrans, xt):
  wtrans #翻訳したい言語
  tr = Translator()
  result = tr.translate(wtrans, src="ja", dest="en").text
  en_words = result
  googleSearch = 'https://www.google.co.jp/search'
  response = requests.get(googleSearch, params={'q': en_words,'num': xt})
  #結果取得
  soup = BeautifulSoup(response.text, "html.parser")
  elems = soup.find_all(href=re.compile("www."))
  for searchResult in elems:
    transe_title = searchResult.text
    transe_url = re.sub("\/url\?q=","",searchResult.get('href'))
    furl =  transe_url.partition('&')[0]
    print('[英語検索結果]タイトル:',transe_title)
    print('[英語検索結果]URL:',furl)
    return (transe_title, transe_url)