import imaplib
import email
from email.header import decode_header
from nltk.tokenize import word_tokenize

# Your Grommunio IMAP details
IMAP_SERVER = "mail.yourdomain.com"
EMAIL_ACCOUNT = "your_username@yourdomain.com"
PASSWORD = "your_password"

def clean_subject(subject):
    parts = decode_header(subject)
    subject_str = ""
    for part, enc in parts:
        if isinstance(part, bytes):
            subject_str += part.decode(enc or "utf-8", errors="ignore")
        else:
            subject_str += part
    return subject_str

# Connect to IMAP
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL_ACCOUNT, PASSWORD)

# Select Inbox (or "Sent")
mail.select("INBOX")

# Search for recent emails (last 5 days for example)
status, data = mail.search(None, 'SINCE 12-Sep-2025')
mail_ids = data[0].split()

for num in mail_ids[-10:]:  # last 10 messages
    status, data = mail.fetch(num, "(RFC822)")
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)
    
    subject = clean_subject(msg["Subject"] or "")
    print("Subject:", subject)
    
    # Get body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                break
    else:
        body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")
    
    # Tokenize body
    tokens = word_tokenize(body)
    print("Tokens:", tokens[:20], "...\n")  # preview first 20 tokens
