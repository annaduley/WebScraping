
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys
from twilio.rest import Client


client = Client(keys.accountSID, keys.authToken)
TwilioNumber = '+14696639542'
myCellPhone = '+17138650271'


url = 'https://cryptoslate.com/coins/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers= headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tr = soup.findAll('tr')


#tests if Bitcoin is below 40,000
for row in tr:
    td = row.findAll("td")
    if td:
      if ((td[1].text).split()[0]) == 'Bitcoin' and((td[1].text).split()[1]) == 'BTC':
        num = float(((td[2].text.strip(' ')).strip('$')).replace(',',''))
        if((float(((td[2].text.strip(' ')).strip('$')).replace(',','')))<40000):
          textmsg = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = "Bitcoin has fallen below $40,000")


#tests if Ethereum is below 3,000
for row in tr:
    td = row.findAll("td")
    if td:
      if ((td[1].text).split()[0]) == 'Ethereum' and((td[1].text).split()[1]) == 'ETH':
        num = float(((td[2].text.strip(' ')).strip('$')).replace(',',''))
        if((float(((td[2].text.strip(' ')).strip('$')).replace(',','')))<3000):
          textmsg = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = "Ethereum has fallen below $3,000")


#displays output of top 5 currencies
for row in tr[0:6]:
    td = row.findAll("td")
    if td:
      print('Name:', (td[1].text).split()[0])
      print('Symbol:', (td[1].text).split()[1])
      print('Current Price:' , td[2].text.strip('  '))
      print('% Change in the Last 24 Hours:' , td[3].text.strip('  '))

      currentPrice =  float(((td[2].text.strip('  ')).strip('$')).replace(',',''))
      percentChange = .01*(float(((((td[3].text.strip('  ')).strip('$')).strip('+')).strip('%')).replace(',','')))
      change = '$' + str('{:,}'.format(float(currentPrice/(percentChange+1))))
      print('Price 24 Hours Prior:', change)

      print()
      input()

      

