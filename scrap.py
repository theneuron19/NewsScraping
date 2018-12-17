from bs4 import BeautifulSoup
import requests
import dateutil.parser
import json 

titles = []
published_date = []
arr = ['saskatchewan', 'manitoba']
r  = requests.get("<news_url>")
data = r.text
soup = BeautifulSoup(data)
j = 3
for link in soup.find_all('a'):
    links = link.get('href')
    #if('saskatchewan' in links):
    if any(c in links for c in arr):
        #print(links)
        r1  = requests.get(links)
        data1 = r1.text
        soup1 = BeautifulSoup(data1)
        i = 0
        if(j % 3 == 0):
            for link1 in soup1.find_all('meta'):
                links1 = link1.get('content')
                #print(links1)
                if(i==3):
                    headline=links1.split("|")[0]
                    titles.append(headline)
                    #print(headline)
                if(i==8):
                    headline_date=links1[:-6]
                    #print(headline_date)
                    published_date.append(headline_date)
                    
                i=i+1          
        j=j+1
        
data = {}
#data = dict(zip(titles,published_date))
data['title'] = titles
data['published_date'] = published_date
with open('news_new.json', 'w') as outfile:
    json.dump(data, outfile)
