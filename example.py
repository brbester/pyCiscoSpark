import pyCiscoSpark

accesstoken="Bearer MjliZGEyMDAtNjViOS00MTI0LWI5YTQtZmVlMGU1ZjdlN2IyMGQ4ODkyOTQtM2Qw"

resp = pyCiscoSpark.get_persondetails(accesstoken,"me")
if resp.status_code != 201:
    print (format(resp.status_code))
print(resp.text)

resp = pyCiscoSpark.get_rooms(accesstoken)
if resp.status_code != 201:
    print (format(resp.status_code))
print(resp.text)

