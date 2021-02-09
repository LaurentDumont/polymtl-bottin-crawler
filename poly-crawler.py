
import requests
import string
from bs4 import BeautifulSoup

emailList= []

#add url of the page you want to scrape to urlString
urlString='https://www.polymtl.ca/bottin/personnes/'

#function that extracts all emails from a page you provided and stores them in a list
def emailExtractor(urlString):
    alphabet_letters = string.ascii_lowercase
    for letter in alphabet_letters:
      headers = {'User-Agent': 'potato tomato poutine'}
      getH=requests.get(urlString+letter, headers=headers)
      h=getH.content
      soup=BeautifulSoup(h,'html.parser')
      mailtos = soup.select('a[href^=mailto]')
      for i in mailtos:
          href=i['href']
          try:
              str1, str2 = href.split(':')
          except ValueError:
              break
            
          emailList.append(str2)
        
        
            

emailExtractor(urlString)
unique_emails = set(emailList)
print(len(unique_emails))
