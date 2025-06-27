import requests
from modules.write.write import write
from typing import Dict, Any

def get_messages(email: str, cookies: Dict[str, str]) -> Any:
    """
    Fetch messages for the given email address from Emailnator.
    """
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.emailnator.com',
        'priority': 'u=1, i',
        'referer': 'https://www.emailnator.com/inbox/',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Opera GX";v="119"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"119.0.5497.144"',
        'sec-ch-ua-full-version-list': '"Chromium";v="134.0.6998.205", "Not:A-Brand";v="24.0.0.0", "Opera GX";v="119.0.5497.144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': cookies['XSRF-TOKEN'],
    }
    json_data = {'email': email}
    response = requests.post(
        'https://www.emailnator.com/message-list',
        cookies=cookies,
        headers=headers,
        json=json_data
    )
    response.raise_for_status()
    return response.json()







