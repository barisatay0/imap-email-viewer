from email_parser import decode_subject

def print_email_info(msg):
    subject = decode_subject(msg['Subject'])
    from_ = msg['From']
    date_ = msg['Date']
    
    print(f'From: {from_}, Subject: {subject}, Date: {date_}')
