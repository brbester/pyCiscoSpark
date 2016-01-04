# pyCiscoSpark
==============
Python Library to Interface to Cisco Spark REST API
---------------------------------------------------
using requests >2.4 - install instructions here:
http://docs.python-requests.org/en/latest/user/install/

at = personal Access Token (see https://developer.ciscospark.com/getting-started.html)




Basically call the functions below and get a Python dictionary of the JSON back. You can then print the raw dictionary and choose the specific return fields you want to parse.

This is an example of getting a Display Name from the Spark API from the personID:

`resp_dict2=pyCiscoSpark.get_persondetails(accesstoken,personid)`

`print resp_dict2['displayName']`


## Follows: https://developer.ciscospark.com/quick-reference.html
### get_people(at,email,displayName,max):
List People in your Organization - max default is 10
you need to enter an email or displayName or Spark will send an error

### get_persondetails(at,personId):
Get Person Details

### get_me(at):
Get your Details

### get_rooms(at):
Get a list of rooms in which you are a member

### get_room(at,roomId):
get room details

### get_memberships(at):


### get_membership(at,membershipId):

### get_messages(at,roomId):

### get_message(at,messageId):

### get_webhooks(at):

### get_webhook(at,webhookId):

### post_createroom(at,title):

### post_message(at,roomId,text):

### post_membership(at,roomId,personEmail,isModerator=True):

### post_webhook(at,name,targetUrl,resource,event,filter):

### put_room(at,roomId,title):

### put_membership(at,membershipId,isModerator):

### put_webhook(at,webhookId,name,targetUrl):

### del_room(at,roomId):

### del_membership(at,membershipId):

### del_message(at,messageId):

### del_webhook(at,webhookId):

