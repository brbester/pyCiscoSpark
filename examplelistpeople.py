import pyCiscoSpark
import sys
import json

accesstoken="Bearer "+str(sys.argv[1])
print accesstoken

email="brbester@cisco.com"

resp = pyCiscoSpark.get_people(accesstoken,email)
if resp.status_code != 200:
    print (format(resp.status_code))
print(resp.text)

resp_dict=json.loads(resp.text)

personid = resp_dict['items'][0]['id']

resp2=pyCiscoSpark.get_persondetails(accesstoken,personid)

resp_dict2 = json.loads(resp2.text)

print resp_dict2

