import email

def fetch_latest_emails(mail, num_emails=10):
    try:
        mail.select('inbox')
        status, messages = mail.search(None, 'ALL')
        mail_ids = messages[0].split()
        
        for i in mail_ids[-num_emails:]:
            status, msg_data = mail.fetch(i, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])
            yield msg
    except Exception as e:
        print(f"Error fetching emails: {e}")
