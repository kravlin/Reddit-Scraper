#!/usr/bin/python2

#import statements
import os
import hashlib
import json
import requests
import re
import urllib

#set basic information up
path="/srv/http/pictures/"
subreddit="clopclop"
files = {}
stillup = {}
stories = []

#get hashes of current files
dirList=os.listdir(path)
for name in dirList:
    files[name] = hashlib.sha1(open(path+name).read()).hexdigest()
    stillup[name] = 0
request = requests.get('http://www.reddit.com/r/'+subreddit+'/hot.json')
data = request.json()

#get info from reddit
for story in data['data']['children']:
    isimgur = re.search("imgur",story['data']['url'])
    if(isimgur):  
        stories.append(story['data']['url'])

#download everything
i = 0
for picture in stories:
    #response = urllib2.urlopen(picture)
    urllib.urlretrieve (picture, path+str(i)+".jpg")
    i = i+1
    
