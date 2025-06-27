from primp import Client
from urllib.parse import unquote
from typing import Dict

def get_emailnator_cookies() -> Dict[str, str]:
    """
    Retrieve and decode cookies from Emailnator using browser impersonation.
    """
    client = Client(impersonate="chrome_124", impersonate_os="windows", cookie_store=True)
    response = client.get("https://www.emailnator.com")
    cookies = response.cookies
    return {k: unquote(v) for k, v in cookies.items()}
