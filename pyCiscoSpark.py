import requests
import json

def _url(path):
    return 'https://api.ciscospark.com/v1' + path

def get_rooms(at):
    headers = {'Authorization':at}
    return requests.get(_url('/rooms'),headers=headers)

def get_people(at):
    headers = {'Authorization':at}
    return requests.get(_url('/people'),headers=headers)

def get_persondetails(at,personId):
    headers = {'Authorization':at}
    return requests.get(_url('/people/{:s}/'.format(personId)),headers=headers)




def add_task(summary, description=""):
    return requests.post(_url('/tasks/'), json={
        'summary': summary,
        'description': description,
        })


