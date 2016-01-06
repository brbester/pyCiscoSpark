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

#grabbing roomId
roomid=str(txt["roomId"])

print "\n\n"
print message
print "\n\n"
f.write ("text:"+message)

#LOOP PREVENTION - watch for Google prefix and respond without Google as prefix
if ((message.find("Google", 0, 6))==0):
    searchterm = message.lstrip("Google ")
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

f.close
