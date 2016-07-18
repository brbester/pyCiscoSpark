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
#        print (room['title'])
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
#    print (payload)
    resp = requests.get(_url('/people'),params=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_persondetails(at,personId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/people/{:s}/'.format(personId)),headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_me(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/people/me'),headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_rooms(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/rooms'),headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_room(at,roomId):
    headers = {'Authorization':at}
    payload = {'showSipAddress':'true'}
    resp = requests.get(_url('/rooms/{:s}'.format(roomId)),params=payload,headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_memberships(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/memberships'),headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_membership(at,membershipId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/memberships/{:s}'.format(membershipId)),headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_messages(at,roomId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'roomId':roomId}
    resp = requests.get(_url('/messages'),params=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_message(at,messageId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/messages/{:s}'.format(messageId)),headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_webhooks(at):
    headers = {'Authorization':at}
    resp = requests.get(_url('/webhooks'),headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def get_webhook(at,webhookId):
    headers = {'Authorization':at}
    resp = requests.get(_url('/webhooks/{:s}'.format(webhookId)),headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

#POST Requests
def post_createroom(at,title):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'title':title}
    resp = requests.post(url=_url('/rooms'),json=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def post_message(at,roomId,text,toPersonId='',toPersonEmail=''):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'roomId':roomId, 'text':text}
    if (toPersonId != ''):
        payload['toPersonId']=toPersonId
    if (toPersonEmail != ''):
        payload['toPersonEmail']=toPersonEmail
    resp = requests.post(url=_url('/messages'),json=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def post_file(at,roomId,url,text='',toPersonId='',toPersonEmail=''):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'roomId':roomId, 'files':[url]}
    if (text != ''):
        payload['text']=text
    if (toPersonId != ''):
        payload['toPersonId']=toPersonId
    if (toPersonEmail != ''):
        payload['toPersonEmail']=toPersonEmail
    resp = requests.post(url=_url('/messages'),json=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict
    
def post_localfile(at,roomId,filename,text='',toPersonId='',toPersonEmail=''):
    headers = {'Authorization':at}
    payload = {'roomId':roomId}
    if (text != ''):
        payload['text']=text
    if (toPersonId != ''):
        payload['toPersonId']=toPersonId
    if (toPersonEmail != ''):
        payload['toPersonEmail']=toPersonEmail
    files = {'files': open(filename,'rb')}
    resp = requests.post(url=_url('/messages'),files=files, data=payload)
    dict['response']=(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def post_membership(at,roomId,personEmail,isModerator=True):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'roomId':roomId, 'personEmail':personEmail, 'isModerator':isModerator}
    resp = requests.post(url=_url('/memberships'),json=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def post_webhook(at,name,targetUrl,resource,event,filter):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'name':name, 'targetUrl':targetUrl, 'resource':resource, 'event':event, 'filter':filter}
    resp = requests.post(url=_url('/webhooks'),json=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

#PUTS
def put_room(at,roomId,title='title'):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'title': title}
    resp = requests.put(url=_url('/rooms/{:s}'.format(roomId)),json=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def put_membership(at,membershipId,isModerator):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'isModerator':isModerator}
    resp = requests.put(url=_url('/memberships/{:s}'.format(membershipId)),json=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

def put_webhook(at,webhookId,name,targetUrl):
    headers = {'Authorization':at, 'content-type':'application/json'}
    payload = {'name':name, 'targetUrl':targetUrl}
    resp = requests.put(url=_url('/webhooks/{:s}'.format(webhookId)),json=payload, headers=headers)
    dict = json.loads(resp.text)
    dict['statuscode']=str(resp.status_code)
    return dict

#DELETES

def del_room(at,roomId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    resp = requests.delete(url=_url('/rooms/{:s}'.format(roomId)), headers=headers)
    dict = {}
    dict['statuscode']=str(resp.status_code)
    return dict

def del_membership(at,membershipId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    resp = requests.delete(url=_url('/memberships/{:s}'.format(membershipId)), headers=headers)
    dict = {}
    dict['statuscode']=str(resp.status_code)
    return dict


def del_message(at,messageId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    resp = requests.delete(url=_url('/messages/{:s}'.format(messageId)), headers=headers)
    dict = {}
    dict['statuscode']=str(resp.status_code)
    return dict


def del_webhook(at,webhookId):
    headers = {'Authorization':at, 'content-type':'application/json'}
    resp = requests.delete(url=_url('/webhooks/{:s}'.format(webhookId)), headers=headers)
    dict = {}
    dict['statuscode']=str(resp.status_code)
    return dict




