import imaplib

def connect_to_email(username, password):
    try:
        mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
        mail.login(username, password)
        return mail
    except Exception as e:
        print(f"Error connecting to email: {e}")
        return None
