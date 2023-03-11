from flask import Flask, request

from NsLookup import nslookup
from Whois import who_is
from SSLcertificate import sslc
from DNS import dns_enum
from Wappy import wapp
from Hunterio import hunter

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi'

@app.route('/api', methods=['GET', 'POST'], strict_slashes=False)
def result():
    data = dict()
    if request.json['url']:
        url = str(request.json['url'])

        data['NsLookup'] = nslookup(url)
        data['Whois'] = who_is(url)
        data['SSLCertificate'] = sslc(url)
        data['Dig'] = dns_enum(url)
        data['Wappalyzer'] = wapp(url)
        data['Hunterio'] = hunter(url)
    return data


if __name__ == '__main__':
    app.run()