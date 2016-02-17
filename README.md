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



## Examples
###example.py
Python example to show room members and print the text messages in a specified room
execute via "python example.py access_token_string"

###example2.py
Searches for a specified room and then posts a designated message

###createwebhook.py
creates webhook to watch for new messages in a room

### ciscospark.php
Sample PHP script to receive notifications from created webhook

### sparkmess.py
Sample python script to act on notifications by posting a message back to room in response (bot example)

### sparkgoogle.py
Sample "bot" script. prefix a query or question with Google in a room and it responds with top 2 Google search results and links.  Requires ciscospark.php or similar to call it in response to created webhook.

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
Get room details

### get_memberships(at):
Get membership list

### get_membership(at,membershipId):
Get membership details

### get_messages(at,roomId):
Get list of messages

### get_message(at,messageId):
Get details of a specific message - useful for reading the text

### get_webhooks(at):
list registered webhooks

### get_webhook(at,webhookId):
get webhook info

### post_createroom(at,title):
Create a room with title

### post_message(at,roomId,text):
Post a message to a room (text only right now - see post_file)

### post_file(at,roomId,url):
Posts a file to a room

### post_membership(at,roomId,personEmail,isModerator=True):
Add a person to a room

### post_webhook(at,name,targetUrl,resource,event,filter):
Create a webhook

### put_room(at,roomId,title):
Change a room's title

### put_membership(at,membershipId,isModerator):
change a member's moderator status

### put_webhook(at,webhookId,name,targetUrl):
Change the targetURL or name for a webhook

### del_room(at,roomId):
Delete a room

### del_membership(at,membershipId):
Leave a room

### del_message(at,messageId):
Delete a message

### del_webhook(at,webhookId):
Delete a webhook

