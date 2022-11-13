
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import openpyxl as xl
#from openpyxl.styles import Font

#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'



page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

tables = soup.findAll('table')
movieTable = tables[0]

#print(movieTable)

#print(title)

tr = movieTable.findAll('tr')


for row in tr[0:6]:
    td = row.findAll("td")
    if td:
      print('Rank:', td[0].text)
      print('Release:', td[1].text)
      print('Total Gross:' , td[7].text)
      totGross = td[7].text.strip('$')
      totGross = totGross.replace(',','')
      totTheatre = td[6].text.strip('$')
      totTheatre = totTheatre.replace(',','')
      rev = '$' + str('{:,}'.format(round(float(totGross)/float(totTheatre))))
      print('Avg Rev/Theatre:' , rev)
      print('Distributor:' , td[9].text)



