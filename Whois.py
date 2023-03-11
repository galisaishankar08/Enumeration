from urllib.parse import urlparse
import whois

def who_is(url):
    try:
        url = "https://"+url
        whois_info = whois.whois(urlparse(url).hostname)
        return whois_info
    except:
        None
