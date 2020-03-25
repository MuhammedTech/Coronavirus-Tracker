from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime



def main(country):
    url = 'https://www.worldometers.info/coronavirus/'
    website = urlopen(url).read().decode()
    soup = BeautifulSoup(website,'html.parser')
    title = soup.find('title').string
    cases = title.split()[3]
    death = title.split()[6]
    time = datetime.datetime.now().strftime('%d %B %Y %H:%M ')
    dis = '{}\nTotal Coronavirus cases: {}\nTotal Global Death: {}'.format(time,cases,death)
    print(dis)

#continue
    url = 'https://www.worldometers.info/coronavirus/#countries'
    website = urlopen(url).read().decode()
    soup = BeautifulSoup(website, 'html.parser')
    table = soup.find('table')
    body = table.find('tbody')
    column = body.find_all('tr')
    country = country.title()
    for row in column:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols[0] == country:
            if cols[2] == '': new = 0
            else: new = cols[2]
            if cols[1] == '': cases = 0
            else: cases = cols[1]
            if cols[3] == '': deaths = 0
            else: deaths = cols[3]
            if cols[6] == '': active = 0
            else: active = cols[6]
            if cols [5] == '': recovered = 0
            else: recovered = cols[5]
            out = '{}:\n\tTotal Cases: {}\n\tTotal Deaths: {}\n\tNew cases: {}\n\tActive Cases: {}\n\tRecovered: {}\n\t'.format(country,cases,deaths,new,active,recovered)
            print(out)

user = input('Enter country name: ')
print(main(user))

