# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"




url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers= headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')


table_rows = soup.findAll("tr")

#total deaths/total cases
deathHigh = 0.0
highDeathState = ''
deathLow = 10000.0
lowDeathState = ''

testHigh = 0.0
highTestState = ''
testLow = 10000.0
lowTestState = ''


for row in table_rows[2:53]:
    td = row.findAll("td")
    state = td[1].text
    cases = int(td[2].text.replace(',',''))
    death = int(td[4].text.replace(',',''))
    tests = int(td[10].text.replace(',',''))
    pop = int(td[12].text.replace(',',''))
    deathRate = round(100*(death/cases),2)
    testRate = round(100*(tests/pop),2)

    if deathRate > deathHigh:
        deathHigh = deathRate
        highDeathState = state

    if deathRate < deathLow:
        deathLow = deathRate
        lowDeathState = state
    
    if testRate > testHigh:
        testHigh = testRate
        highTestState = state

    if testRate < testLow:
        testLow = testRate
        lowTestState = state

    '''print(f"State: {state}")
    print(f"Deaths: {death}")
    print(f"Cases: {cases}")
    print(f"Tests: {tests}")
    print(f"Population: {pop}")
    print(f"Death Rate: {deathRate}%")'''
print(f"State with worst death rate: {highDeathState}")
print(f"Death Rate: {deathHigh}%\n")
print(f"State with best death rate: {lowDeathState}")
print(f"Death Rate: {deathLow}%\n")
print(f"State with worst test rate: {lowTestState}")
print(f"Test Rate: {testLow}%\n")
print(f"State with best test rate: {highTestState}")
print(f"Test Rate: {testHigh}%\n")





#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

