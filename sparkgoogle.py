#!/usr/bin/python
import pyCiscoSpark
import sys
import requests
import json
import urllib


def get_google(searchterm):
    URL = 'https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='+urllib.quote_plus(searchterm)+'&userip=USERS-IP-ADDRESS'
    print "URL:"+URL+"\n"
    resp = requests.get(URL)
    return json.loads(resp.text)

def get_googlepics(searchterm):
    URL = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBlowr5J3SBAaCm6CZZywrf9thnAFW-0jM&cx=002683842610695450429:pjurqlgggde&q='+urllib.quote_plus(searchterm)+'&searchType=image&safe=high'
    print "URL:"+URL+"\n"
    resp = requests.get(URL)
    return json.loads(resp.text)

#storing the Authentication token in a file in the OS vs. leaving in script
fat=open ("/usr/lib/cgi-bin/at.txt","r+")
accesstoken=fat.readline()
accesstoken="Bearer "+accesstoken
fat.close

#opening a file to log each time the script acts
f=open ("/usr/lib/cgi-bin/spark.txt","a")

#grabbing messageId from the command line argument from ciscospark.php
msgid=str(sys.argv[1])

#logging to file
f.write ("at:"+accesstoken)
f.write ("\n")
f.write ("msgid:"+msgid)
f.write ("\n")

#reading text from message that caused alert
txt=pyCiscoSpark.get_message(accesstoken,msgid)
print txt

message=str(txt["text"])
newmessage="robot response to "+message

#grabbing roomId
roomid=str(txt["roomId"])

print "\n\n"
print message
print "\n\n"
f.write ("text:"+message)

#LOOP PREVENTION - this section won't execute if "robot" is at beginning of new posted message - if it isn't it will post a new message with "robot" as prefix
if ((message.find("Google", 0, 6))==0):
    searchterm = message[7:]
    print searchterm
    resp_dict = get_google(searchterm)
    print resp_dict
    newmessage = "Response from Google: " + resp_dict["responseData"]["results"][0]["title"]+" "+resp_dict["responseData"]["results"][0]["url"]
    newmessage = newmessage.replace("<b>","")
    newmessage = newmessage.replace("</b>","")
    print newmessage
    resp2_dict = pyCiscoSpark.post_message(accesstoken,roomid,newmessage)
    newmessage = "Response from Google: " + resp_dict["responseData"]["results"][1]["title"]+" "+resp_dict["responseData"]["results"][1]["url"]
    print newmessage
    newmessage = newmessage.replace("<b>","")
    newmessage = newmessage.replace("</b>","")
    resp2_dict = pyCiscoSpark.post_message(accesstoken,roomid,newmessage)
    print resp2_dict

if ((message.find("GPIC", 0, 4))==0):
    searchterm = message[5:]
    print searchterm
    resp_dict = get_googlepics(searchterm)
    print resp_dict
    newimage = resp_dict["items"][0]["link"]
    resp4_dict = pyCiscoSpark.post_file(accesstoken,roomid,newimage)

f.close
