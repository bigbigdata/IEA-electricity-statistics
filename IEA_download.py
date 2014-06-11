import urllib 
import urllib2 

year = range(2008,2014)
year2014 = [2013]
month = range(1,13)

url = "http://www.iea.org/stats/surveys/Electricity/MES"

y = range(2007,2014) 
m = range(1,13)
link = []
time = []

for i in y:
    for j in m:
        if j<10:
            link.append(url+str(i)+'0'+str(j)+'.xls')
            time.append(str(i)+'0'+str(j)+'.xls')
            #linkname=(url+str(i)+'0'+str(j)+'.xls')
            #filename=(str(i)+'0'+str(j)+'.xls')
        else:
            link.append(url+str(i)+str(j)+'.xls')
            time.append(str(i)+str(j)+'.xls')
            #linkname=(url+str(i)+str(j)+'.xls')
            #filename=(str(i)+str(j)+'.xls')

for i in range(len(link)):
    file(time.pop(),'wb').write(urllib2.urlopen(link.pop()).read()) 
#demo one month 
