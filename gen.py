from lxml import html
import csv
import os
import urllib3
import requests
import re
requests.packages.urllib3.disable_warnings()

#visit
a = input('Enter Name :')
url = 'https://www.amazon.in/s?keywords='+a
htmltext = requests.get(url).content.decode('utf-8')
print('processing'+ url)
response = requests.get(url, verify=False)


#click function
doc = html.fromstring(response.content)
Xurl = doc.xpath('//*[@id="result_0"]//@href')
ASIN = Xurl[0].split("/")
print(ASIN[3]+"="+ASIN[5])
name = ASIN[3]
asincode = ASIN[5]
#CSV 
data = {
	'NAME' : name,
	 'ASIN-Code' :  asincode
}
extracted_d = []


data1 = "hello"
with open('ASINfeed.csv', 'w') as csvfile:
        fieldnames = ['NAME','ASIN-Code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()    
        for data in extracted_d:
            writer.writerow(data1)
            print("File is updated")

