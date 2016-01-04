#!/usr/bin/python
import pyCiscoSpark
import sys

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
if ((message.find("robot", 0, 5))==-1): 
    resp_dict = pyCiscoSpark.post_message(accesstoken,roomid,newmessage)
    print resp_dict

f.close
