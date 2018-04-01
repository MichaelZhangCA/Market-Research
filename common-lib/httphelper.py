import requests
from urllib3.exceptions import InsecureRequestWarning 

ssl_verify = False

def get_httprequest(url):

    if(ssl_verify==True):
        return requests.get(url)
    else:
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        return requests.get(url, verify=False)
