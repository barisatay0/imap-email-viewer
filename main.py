from email_connector import connect_to_email
from email_fetcher import fetch_latest_emails
from email_parser import decode_subject
from email_printer import print_email_info

def main():
    username = 'example@hotmail.com'
    password = 'example'

    mail = connect_to_email(username, password)
    if mail:
        for msg in fetch_latest_emails(mail):
            print_email_info(msg)
        mail.logout()

if __name__ == "__main__":
    main()
