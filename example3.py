#Example searches rooms for "pyCiscoSpark TestRoom1", finds the id, and then posts a test message "python test message1"

import pyCiscoSpark
import sys
import urllib

fileurl="https://pbs.twimg.com/profile_images/616542814319415296/McCTpH_E.jpg"

def search (values, searchFor):
    for k in values["items"]:
        print k["title"]
        if (k["title"] == searchFor) : return k["id"]
    return None

accesstoken="Bearer "+str(sys.argv[1])

rooms_dict=pyCiscoSpark.get_rooms(accesstoken)

roomid = search (rooms_dict, "Google Bot Example")

print roomid

resp_dict = pyCiscoSpark.post_file(accesstoken,roomid,fileurl)

print resp_dict


