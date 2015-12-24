import pyCiscoSpark
import sys

accesstoken="Bearer "+str(sys.argv[1])
print accesstoken

resp = pyCiscoSpark.post_message(accesstoken,"Y2lzY29zcGFyazovL3VzL1JPT00vYWIwNDJmYTAtNzI5NS0xMWU1LWJkYzAtNWJhNzIyZGZhNDZh","python test message1")
if resp.status_code != 200:
    print (format(resp.status_code))
print(resp.text)



