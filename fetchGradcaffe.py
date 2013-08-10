import urllib2
from bs4 import BeautifulSoup
import numpy as np
from sklearn.externals import joblib
 
def sendRequest(l, p):
  req = urllib2.Request("http://thegradcafe.com/survey/index.php?q=computer&t=a&o=&pp=250&p="+str(p))
response = urllib2.urlopen(req)
namesPage = response.read()
soup = BeautifulSoup(namesPage)
tds = soup.find_all('td')
for t in tds:
    entry = str(t)
    if entry.find('class="instcol"') != -1 and t.getText() != 'Institution':
        w = t.parent.children
d = []
for x in w:
d.append(x.getText())
l.append(d)
 
if __name__ == '__main__':
titles = {'School':0, 'Program (Season)':1,'Decision & Date':2, 'Status':3,'Date Added':4, 'Notes':5}
l = []
for p in range(1,73):
print 'sending request number: ',p
sendRequest(l,p)
print 'Saving ...'
joblib.dump([l,titles],'listAll.pkl',compress=5)
