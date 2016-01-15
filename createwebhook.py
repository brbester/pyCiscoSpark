import pyCiscoSpark
import sys


def search (values, searchFor):
    for k in values["items"]:
        print (k["title"])
        if (k["title"] == searchFor) : return k["id"]
    return None

at="Bearer "+str(sys.argv[1])
name="New messages in Room XYZ"
targetUrl="http://YOURIPorURL/ciscospark.php"
resource="messages"
event="created"
csfilter="roomId=YOURROOMID"


print (pyCiscoSpark.post_webhook(at,name,targetUrl,resource,event,csfilter))
