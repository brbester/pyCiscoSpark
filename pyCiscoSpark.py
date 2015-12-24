import requests
import json
import urllib2


def _url(path):
    return 'https://api.ciscospark.com/v1' + path
    


def get_people(at):
    headers = {'Authorization':at}
    return requests.get(_url('/people'),headers=headers)

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
    return requests.get(_url('/messages/{:s}/'.format(messageId)),headers=headers)

def get_webhooks(at):
    headers = {'Authorization':at}
    return requests.get(_url('/webhooks'),headers=headers)

def get_webhook(at,webhookId):
    headers = {'Authorization':at}
    return requests.get(_url('/webhooks/{:s}'.format(webhookId)),headers=headers)


def post_createroom(at,title):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {"title":title}
    return requests.post(url=_url('/rooms'),json=payload, headers=headers)

def post_message(at,roomId,text):
    headers = {'Authorization':at, "content-type":"application/json"}
    payload = {'roomId':roomId, "text":text}
    return requests.post(url=_url('/messages'),json=payload, headers=headers)



