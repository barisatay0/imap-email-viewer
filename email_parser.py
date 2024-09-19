from email.header import decode_header

def decode_subject(subject):
    decoded_subject, encoding = decode_header(subject)[0]
    if isinstance(decoded_subject, bytes):
        return decoded_subject.decode(encoding if encoding else 'utf-8')
    return decoded_subject
