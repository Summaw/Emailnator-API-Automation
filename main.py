from modules.generateEmail import generate_email
from modules.getMessages import get_messages
from modules.getCookies import get_emailnator_cookies
from modules.write.write import write


### Function write(text, case) writes the text to the console with the given case

### Function generateEmail() returns a generated email address
### Function getMessages(email) returns a list of messages for the given email address


def main() -> None:
    """
    Main workflow for generating a temporary email, fetching messages, and logging the process.
    """
    write('Starting...', 'info')
    cookies = get_emailnator_cookies()
    write(f'Cookies: {cookies.get("XSRF-TOKEN", "")[:55]}...', 'success')

    email = generate_email(cookies)
    write(f'Generated email: {email}', 'success')

    messages = get_messages(email, cookies)
    write(f'Messages: {messages}', 'success')

    write('Finished', 'info')

if __name__ == '__main__':
    main()






