import requests
import simplejson as json
from requests.auth import HTTPBasicAuth
from error import dprint as print

def get_from_repo(repo, username, password):
    global y
    f = requests.get(repo, auth=HTTPBasicAuth(username, password))
    print(f)
    try:
        f.raise_for_status()
    except:  # if theres an exception, ignore it
        pass
    # noinspection PyBroadException
    try:
        y = json.loads(f.content.decode('utf-8'))
    except:  # if theres an exception, ignore it
        pass
    print(y)
    return y


def push_to_repo(repo, username, password, data):
    global y
    f = requests.post(str(repo), auth=HTTPBasicAuth(username, password), json=data)
    print(f)
    try:
        f.raise_for_status()
    except:  # if theres an exception, ignore it
        pass
    try:
        y = json.loads(f.content.decode('utf-8'))
    except:  # if theres an exception, ignore it
        pass
    print(y)
    return y
