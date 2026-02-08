import requests
from config import USER_AGENT, TIMEOUT, VERIFY_SSL

session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT})

def get(url):
    return session.get(url, timeout=TIMEOUT, verify=VERIFY_SSL)

def post(url, data):
    return session.post(url, data=data, timeout=TIMEOUT, verify=VERIFY_SSL)

