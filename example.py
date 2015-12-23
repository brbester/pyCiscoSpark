import pyCiscoSpark
import idstring

accesstoken="Bearer "+idstring.idstring

resp = pyCiscoSpark.get_persondetails(accesstoken,"me")
if resp.status_code != 201:
    print (format(resp.status_code))
print(resp.text)

resp = pyCiscoSpark.get_rooms(accesstoken)
if resp.status_code != 201:
    print (format(resp.status_code))
print(resp.text)

