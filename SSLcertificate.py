import ssl
from urllib.parse import urlparse

def sslc(url):
    try:
        url = 'https://'+url
        ssl_info = ssl.get_server_certificate((urlparse(url).hostname, 443))
        return ssl_info
    except:
        return None
