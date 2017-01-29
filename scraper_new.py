import urllib2
import ast
url = 'http://www.unitedstateszipcodes.org/91801/'
req = urllib2.Request('http://www.unitedstateszipcodes.org/91801/', headers={ 'User-Agent': 'Mozilla/5.0' })
html = urllib2.urlopen(req).read()

f1 = open('test.htm','w+')
print>>f1, html;

f1 = open('test.htm','r')
k=0
line1 = ''
print "ZIP Code: ",
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
    if line.find("Worked Full-time With Earnings")>-1:
        line1 = line[15:-2]
    if line.find("$10,000-$19,999")>-1:
        line2 = line[15:-2]
    if line.find("</td></tr><tr><th>Coordinates:</th><td>")>-1:
        print "Coordinates: " + line[line.find("</td></tr><tr><th>Coordinates:</th><td>")+39:-46]
        print "County: " + line[line.find("</td></tr><tr><th>County: </th><td>")+35:-270] + "\n"

print "\n"+"Employment Status"
for i in range(len(ast.literal_eval(line1)[0]['values'])):
    print ast.literal_eval(line1)[0]['values'][i]['x'] + ':',
    print ast.literal_eval(line1)[0]['values'][i]['y']

print "\n"+"Annual Indivisual Earnings"
for i in range(len(ast.literal_eval(line2)[0]['values'])):
    print ast.literal_eval(line2)[0]['values'][i]['x'] + ':',
    print ast.literal_eval(line2)[0]['values'][i]['y']










