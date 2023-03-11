import requests
from dotenv import load_dotenv
import os

load_dotenv()

def hunter(domain):
    try:
        api_key = os.getenv('API_KEY')
        url = f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}'

        response = requests.get(url)
        data = response.json()

        emails = []
        for email in data['data']['emails']:
            emails.append(email['value'])

        organisation = data['data']['organization']

        socialmedia = []
        if data['data']['twitter']:
            socialmedia.append(data['data']['twitter'])
        if data['data']['facebook']:
            socialmedia.append(data['data']['facebook'])
        if data['data']['linkedin']:
            socialmedia.append(data['data']['linkedin'])
        if data['data']['instagram']:
            socialmedia.append(data['data']['instagram'])
        if data['data']['youtube']:
            socialmedia.append(data['data']['youtube'])

        res = dict()
        res['organisation'] = organisation
        res['socialmedia'] = socialmedia
        res['emails'] = emails

        return res
    except:
        return 'Error'
