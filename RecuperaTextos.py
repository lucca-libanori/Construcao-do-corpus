import requests
from bs4 import BeautifulSoup
import numpy as np



url1 = ('https://levity.ai/blog/how-natural-language-processing-works')
url2 = ('https://en.wikipedia.org/wiki/Natural_language_processing')
url3 = ('https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/')
url4 = ('https://www.qualtrics.com/experience-management/customer/natural-language-processing/')
url5 = ('https://www.oracle.com/hk/artificial-intelligence/what-is-natural-language-processing/')

urls = [url1, url2, url3, url4, url5]

sentencas = []

for url in urls:
    sites = requests.get(url).text
    soup = BeautifulSoup(sites,'html.parser')

    for site in soup.find_all("p"):
        sentencas.append(site.get_text())
        
print(sentencas)