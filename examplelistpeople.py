import pyCiscoSpark
import sys
import json

accesstoken="Bearer "+str(sys.argv[1])

email="brbester@cisco.com"

resp_dict = pyCiscoSpark.get_people(accesstoken,email)

personid = resp_dict['items'][0]['id']
print (personid)

resp_dict2=pyCiscoSpark.get_persondetails(accesstoken,personid)
print (resp_dict2['displayName'])

