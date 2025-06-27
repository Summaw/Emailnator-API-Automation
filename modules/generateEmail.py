import requests
from modules.write.write import write
from typing import Dict

def generate_email(cookies: Dict[str, str]) -> str:
    """
    Generate a temporary email address using Emailnator API.
    """
    session_cookies = {
        'XSRF-TOKEN': cookies['XSRF-TOKEN'],
        'gmailnator_session': cookies['gmailnator_session'],
    }
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'origin': 'https://www.emailnator.com',
        'referer': 'https://www.emailnator.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0',
        'x-xsrf-token': cookies['XSRF-TOKEN'],
    }
    json_data = {'email': ['dotGmail']}
    response = requests.post(
        'https://www.emailnator.com/generate-email',
        cookies=session_cookies,
        headers=headers,
        json=json_data
    )
    response.raise_for_status()
    email = response.json()['email'][0]
    return email