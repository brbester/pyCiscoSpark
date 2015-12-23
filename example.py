import pyCiscoSpark
import sys

accesstoken="Bearer "+str(sys.argv[1])
print accesstoken

resp = pyCiscoSpark.get_persondetails(accesstoken,"me")
if resp.status_code != 201:
    print (format(resp.status_code))
print(resp.text)

resp = pyCiscoSpark.get_rooms(accesstoken)
if resp.status_code != 201:
    print (format(resp.status_code))
print(resp.text)

