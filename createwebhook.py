import pyCiscoSpark
import sys


def search (values, searchFor):
    for k in values["items"]:
        print k["title"]
        if (k["title"] == searchFor) : return k["id"]
    return None

at="Bearer "+str(sys.argv[1])
name="New messages in Test3 Room"
targetUrl="http://brbester-kzgwtzcdqc.dynamic-m.com:56798/ciscospark.php"
resource="messages"
event="created"
csfilter="roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYWIwNDJmYTAtNzI5NS0xMWU1LWJkYzAtNWJhNzIyZGZhNDZh"


print pyCiscoSpark.post_webhook(at,name,targetUrl,resource,event,csfilter)
