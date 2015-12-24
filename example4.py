import pyCiscoSpark
import sys

accesstoken="Bearer "+str(sys.argv[1])
print accesstoken

resp = pyCiscoSpark.post_createroom(accesstoken,"pyCiscoSpark TestRoom1")
if resp.status_code != 200:
    print (format(resp.status_code))
print(resp.text)
