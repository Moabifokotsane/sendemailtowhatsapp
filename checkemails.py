#!/usr/bin/env python3

import imaplib
import email
import smtplib
from email.header import decode_header

# IMAP server details
imap_server = "imap.example.com"
username = "your_email@example.com"
password = "your_password"

# WhatsApp details
whatsapp_number = "whatsapp_number"
whatsapp_message = "Email content copied from subject: "

# Connect to the IMAP server
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)
imap.select("INBOX")

# Search for emails with specific subject
status, messages = imap.search(None, 'SUBJECT "Your Subject"')
message_ids = messages[0].split()

for message_id in message_ids:
    # Fetch the email by ID
    _, msg_data = imap.fetch(message_id, "(RFC822)")
    raw_email = msg_data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Extract subject and body
    subject = decode_header(email_message["Subject"])[0][0]
    body = ""

    if email_message.is_multipart():
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode("UTF-8")
                break
    else:
        body = email_message.get_payload(decode=True).decode("UTF-8")

    # Print subject and body
    print("Subject:", subject)
    print("Body:", body)

    # Copy email content and send to WhatsApp
    whatsapp_text = f"{whatsapp_message}{subject}\n\n{body}"

    # Code for sending the 'whatsapp_text' to WhatsApp using the preferred library

# Close the IMAP connection
imap.close()
imap.logout()
