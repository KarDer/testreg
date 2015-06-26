import urllib2
import json

# ************************ add new user ************************ #
response = urllib2.urlopen('http://31.131.18.202:8002/api_registration?username=somenameIS&email=myfirst@mail.ua&pass=0000&phone=380668885522')
data = json.load(response)
print data

print "*"*50
print "*"*50
print "*"*50
# ************************ end ************************ #

# ************************ filter ************************ #
response = urllib2.urlopen('http://31.131.18.202:8002/api_filter?email=test@mail.com')
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


response = urllib2.urlopen('http://31.131.18.202:8002/api_filter?username=testname')
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


response = urllib2.urlopen('http://31.131.18.202:8002/api_filter?phone=380665551122')
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