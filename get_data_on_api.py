import urllib2
import json

# ************************ add new user ************************ #
response = urllib2.urlopen('http://31.131.18.202:8002/api_registration?username=somenameIS&email=myfirst@mail.ua&pass=0000&phone=380668335522')
data = json.load(response)
print data
print "*"*50

response = urllib2.urlopen('http://31.131.18.202:8002/api_registration?username=somename&email=my@mail.ua&pass=0000&phone=380668335522&comment=some_more_text&skype=skype_name&ICQ=34567890')
data = json.load(response)
print data
print "*"*50

response = urllib2.urlopen('http://31.131.18.202:8002/api_registration?username=name&email=my2@mail.ua&pass=0000&phone=380661135522&email2=two@pe.com&ZIP=34890')
data = json.load(response)
print data
print "*"*50

print "*"*50
print "*"*50
print "*"*50
# ************************ end ************************ #

# ************************ filter ************************ #
response = urllib2.urlopen('http://31.131.18.202:8002/api_filter?email=myfirst@mail.ua')
data = json.load(response)
print data

if not 'result' in data:
    for i in data:
        print data[i]['username']
        print data[i]['email']
        print data[i]['date_added']
else:
    print data['result']
print "*"*50


response = urllib2.urlopen('http://31.131.18.202:8002/api_filter?username=my2')
data = json.load(response)
print data
if not 'result' in data:
    for i in data:
        print data[i]['username']
        print data[i]['email']
        print data[i]['date_added']
else:
    print data['result']
print "*"*50


response = urllib2.urlopen('http://31.131.18.202:8002/api_filter?phone=380668335522')
data = json.load(response)
print data

if not 'result' in data:
    for i in data:
        print data[i]['username']
        print data[i]['email']
        print data[i]['date_added']
else:
    print data['result']
print "*"*50
# ************************ end ************************ #