import pyCiscoSpark
import sys

accesstoken="Bearer "+str(sys.argv[1])
print accesstoken

resp = pyCiscoSpark.get_messages(accesstoken,"Y2lzY29zcGFyazovL3VzL1JPT00vYWIwNDJmYTAtNzI5NS0xMWU1LWJkYzAtNWJhNzIyZGZhNDZh")
if resp.status_code != 200:
    print (format(resp.status_code))
print(resp.text)
