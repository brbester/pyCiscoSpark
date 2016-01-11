import pyCiscoSpark
import sys

accesstoken="Bearer "+str(sys.argv[1])
roomname="Google Bot Example"


print (accesstoken)

name = pyCiscoSpark.get_persondetails(accesstoken,"me")['displayName']

room_dict = pyCiscoSpark.get_rooms(accesstoken)

print ("Rooms to Which "+name+" is a member:")
print ("----------------------------------------------------")

for room in room_dict['items']:
    print (room['title'])
    if (room['title']==roomname):roomid = room['id']
print ("")

mess_dict = pyCiscoSpark.get_messages(accesstoken,roomid)

print ("Latest messages in "+roomname)
print ("----------------------------------------------------")
for room in mess_dict['items']:
    if 'text' in room:
        print (room['text'])
   
