import requests
import json

# COMMENTED SECTION BELOW FOR DEBUGGING

#import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
#try:
#    import http.client as http_client
#except ImportError:
    # Python 2
#    import httplib as http_client
#http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
#logging.basicConfig() 
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger('requests.packages.urllib3')
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True


#Helpers
def _url(path):
    return 'https://api.ciscospark.com/v1' + path

def findroomidbyname (at,roomname):
    room_dict = get_rooms(at)    
    for room in room_dict['items']:
        print room['title']
        if (room['title']==roomname):roomid = room['id']    
    return roomid

#GET Requests
def get_people(at,email='',displayname='',max=10):
    headers = {'Authorization':at}
    payload = {'max':max}
    if (email != ''):
        payload['email']=email
    if (displayname != ''):
        payload['displayName']=displayname
    print payload
    resp = requests.get(_url('/people'),params=payload, headers=headers)
    return json.loads(resp.text)

def get_persondetails(at,personId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/people/{:s}/'.format(personId)),headers=headers)
    return json.loads(resp.text)

def get_me(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/people/me'),headers=headers)
    return json.loads(resp.text)

def get_rooms(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/rooms'),headers=headers)
    return json.loads(resp.text)

def get_room(at,roomId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/memberships'),headers=headers)
    return json.loads(resp.text)

def get_memberships(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/memberships'),headers=headers)
    return json.loads(resp.text)

def get_membership(at,membershipId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/memberships/{:s}/'.format(membershipId)),headers=headers)
    return json.loads(resp.text)

def get_messages(at,roomId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'roomId':roomId}
    resp = requests.get(_url('/messages'),params=payload, headers=headers)
    return json.loads(resp.text)

def get_message(at,messageId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/messages/{:s}'.format(messageId)),headers=headers)
    return json.loads(resp.text)

def get_webhooks(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/webhooks'),headers=headers)
    return json.loads(resp.text)

def get_webhook(at,webhookId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/webhooks/{:s}'.format(webhookId)),headers=headers)
    return json.loads(resp.text)

#POST Requests
def post_createroom(at,title):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'title':title}
    resp = requests.post(url=_url('/rooms'),json=payload, headers=headers)
    return json.loads(resp.text)

def post_message(at,roomId,text):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'roomId':roomId, 'text':text}
    resp = requests.post(url=_url('/messages'),json=payload, headers=headers)
    return json.loads(resp.text)

def post_file(at,roomId,url):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'roomId':roomId, 'files':[url]}
    resp = requests.post(url=_url('/messages'),json=payload, headers=headers)
    return json.loads(resp.text)

def post_membership(at,roomId,personEmail,isModerator=True):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'roomId':roomId, 'personEmail':personEmail, 'isModerator':isModerator}
    resp = requests.post(url=_url('/memberships'),json=payload, headers=headers)
    return json.loads(resp.text)

def post_webhook(at,name,targetUrl,resource,event,filter):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'name':name, 'targetUrl':targetUrl, 'resource':resource, 'event':event, 'filter':filter}
    resp = requests.post(url=_url('/webhooks'),json=payload, headers=headers)
    return json.loads(resp.text)

#PUTS
def put_room(at,roomId,title='title'):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'title': title}
    resp = requests.put(url=_url('/rooms/{:s}'.format(roomId)),json=payload, headers=headers)
    return json.loads(resp.text)

def put_membership(at,membershipId,isModerator):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'isModerator':isModerator}
    resp = requests.put(url=_url('/memberships/{:s}'.format(membershipId)),json=payload, headers=headers)
    return json.loads(resp.text)

def put_webhook(at,webhookId,name,targetUrl):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'name':name, 'targetUrl':targetUrl}
    resp = requests.put(url=_url('/webhooks/{:s}'.format(webhookId)),json=payload, headers=headers)
    return json.loads(resp.text)

#DELETES

def del_room(at,roomId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    resp = requests.delete(url=_url('/rooms/{:s}'.format(roomId)), headers=headers)
    return resp.status_code

def del_membership(at,membershipId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    resp = requests.delete(url=_url('/memberships/{:s}'.format(membershipId)), headers=headers)
    return resp.status_code


def del_message(at,messageId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    resp = requests.delete(url=_url('/messages/{:s}'.format(messageId)), headers=headers)
    return resp.status_code


def del_webhook(at,webhookId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    resp = requests.delete(url=_url('/webhooks/{:s}'.format(webhookId)), headers=headers)
    return resp.status_code




