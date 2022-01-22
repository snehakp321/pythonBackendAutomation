import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.imdb.com/find?q=thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content,'html.parser')
#print(soup.prettify())
moviesTable = soup.find('table',{'class':'findList'})

#print(moviesTable.prettify())
rows = moviesTable.findAll('tr')
for i in rows:
    rowdata = i.findAll('td')
    print(rowdata[1].a.text)
    suburl = rowdata[1].a['href']
    subdata = requests.get("https://www.imdb.com/" + suburl)
    childsoup = BeautifulSoup(subdata.content,'html.parser')
    if childsoup.find('div',{'class':'see-more inline canwrap'}):
        genre = childsoup.find('div', {'class': 'see-more inline canwrap'})
        if genre.a.text =="Thriller":
            print(genre.a.text)
    else:
        pass

#course name
#appium = soup.find('a',string='Appium') --this is for visible text
#print(appium['href'])