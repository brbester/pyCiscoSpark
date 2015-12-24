# pyCiscoSpark
Python Library to Interface to Cisco Spark REST API

using requests >2.4 - install instructions here:
http://docs.python-requests.org/en/latest/user/install/


at = personal Access Token (see https://developer.ciscospark.com/getting-started.html)


get_people(at,email,displayName,max):
List People in your Organization - max default is 10
you need to enter an email or displayName or Spark will send an error

get_persondetails(at,personId):
Get Person Details

get_me(at):
Get your Details

get_rooms(at):



get_room(at,roomId):
get_memberships(at):
get_membership(at,membershipId):
get_messages(at,roomId):
get_message(at,messageId):
get_webhooks(at):
get_webhook(at,webhookId):
post_createroom(at,title):
post_message(at,roomId,text):
post_membership(at,roomId,personEmail,isModerator=True):
post_webhook(at,name,targetUrl,resource,event,filter):
put_room(at,roomId,title):
put_membership(at,membershipId,isModerator):
put_webhook(at,webhookId,name,targetUrl):
del_room(at,roomId):
del_membership(at,membershipId):
del_message(at,messageId):
del_webhook(at,webhookId):

