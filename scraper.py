import urllib2
url = 'http://www.unitedstateszipcodes.org/92335/'
req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
html = urllib2.urlopen(req).read()

f1 = open('test.htm','w+')
print>>f1, html;

f1 = open('test.htm','r')
k=0
print url[-6:-1]
for line in f1:
    k=k+1;
    if k>378:
    	if k<430:
    		if line.find("<th>")!=-1:
    			if line.find("</th>")!=-1:
    				print line.strip()[4:-5],
    				print ' ',
    		if line.find("<td class=")!=-1:
    			if line.find("</td>")!=-1:
    				print line.strip()[23:-5];

