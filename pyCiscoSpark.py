import requests
import json

#Helpers
def _url(path):
    return 'https://api.ciscospark.com/v1' + path
    

#GET Requests
def get_people(at,email="",displayname="",max=10):
    headers = {'Authorization':at}
    payload = {"max":max}
    if (email != ""):
        payload["email"]=email
    if (displayname != ""):
        payload["displayName"]=displayname
    print payload
    return requests.get(_url('/people'),params=payload, headers=headers)

def get_persondetails(at,personId):
    headers = {'Authorization':at}
    return requests.get(_url('/people/{:s}/'.format(personId)),headers=headers)

def get_me(at):
    headers = {'Authorization':at}
    return requests.get(_url('/people/me'),headers=headers)

def get_rooms(at):
    headers = {'Authorization':at}
    return requests.get(_url('/rooms'),headers=headers)

def get_room(at,roomId):
    headers = {'Authorization':at}
    return requests.get(_url('/memberships'),headers=headers)

def get_memberships(at):
    headers = {'Authorization':at}
    return requests.get(_url('/memberships'),headers=headers)

def get_membership(at,membershipId):
    headers = {'Authorization':at}
    return requests.get(_url('/memberships/{:s}/'.format(membershipId)),headers=headers)

def get_messages(at,roomId):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {'roomId':roomId}
    return requests.get(_url('/messages'),params=payload, headers=headers)

def get_message(at,messageId):
    headers = {'Authorization':at}
    return requests.get(_url('/messages/{:s}'.format(messageId)),headers=headers)

def get_webhooks(at):
    headers = {'Authorization':at}
    return requests.get(_url('/webhooks'),headers=headers)

def get_webhook(at,webhookId):
    headers = {'Authorization':at}
    return requests.get(_url('/webhooks/{:s}'.format(webhookId)),headers=headers)

#POST Requests
def post_createroom(at,title):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {"title":title}
    return requests.post(url=_url('/rooms'),json=payload, headers=headers)

def post_message(at,roomId,text):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {'roomId':roomId, "text":text}
    return requests.post(url=_url('/messages'),json=payload, headers=headers)

def post_membership(at,roomId,personEmail,isModerator=True):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {'roomId':roomId, "personEmail":personEmail, "isModerator":isModerator}
    return requests.post(url=_url('/memberships'),json=payload, headers=headers)

def post_webhook(at,name,targetUrl,resource,event,filter):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {'name':name, "targetUrl":targetUrl, "resource":resource, "event":event, "filter":filter}
    return requests.post(url=_url('/webhooks'),json=payload, headers=headers)

#PUTS
def put_room(at,roomId,title):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {"title":title}
    return requests.put(url=_url('/rooms/{:s}'.format(roomId)),json=payload, headers=headers)

def put_membership(at,membershipId,isModerator):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {"isModerator":isModerator}
    return requests.put(url=_url('/memberships/{:s}'.format(membershipId)),json=payload, headers=headers)

def put_webhook(at,webhookId,name,targetUrl):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {"name":name, "targetUrl":targetUrl}
    return requests.put(url=_url('/webhooks/{:s}'.format(webhookId)),json=payload, headers=headers)

#DELETES

def del_room(at,roomId):
    headers = {'Authorization':at, "content-type":"application/json"}
    return requests.delete(url=_url('/rooms/{:s}'.format(roomId)), headers=headers)

def del_membership(at,membershipId):
    headers = {'Authorization':at, "content-type":"application/json"}
    return requests.delete(url=_url('/memberships/{:s}'.format(membershipId)), headers=headers)

def del_message(at,messageId):
    headers = {'Authorization':at, "content-type":"application/json"}
    return requests.delete(url=_url('/messages/{:s}'.format(messageId)), headers=headers)

def del_webhook(at,webhookId):
    headers = {'Authorization':at, "content-type":"application/json"}
    return requests.delete(url=_url('/webhooks/{:s}'.format(webhookId)), headers=headers)



