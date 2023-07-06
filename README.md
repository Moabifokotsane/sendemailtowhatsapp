## For Ethical Purposes 
- Suitable For Businesses & Individuals
- Not For Unethical Activities
  
# sendemailtowhatsapp
Sending new emails to a whatsapp number. This will go through email account and fetch new incoming emails then send straight to a whatsapp number using a payload connection via the email account. it will take the email subject and body content and send them to a whatsapp number for alerts &amp; monitoring

### Technical
Script uses python "imaplib" to create a payload on the email account that fetches new emails in the account inbox then scans the email subject and body to send the email subject and content to your whatsapp number.

# How to install 
## For Terminal Usage
### Requirements
- Existing Whatsapp Library (Your Current Whatsapp Automation Program)
- Python 3 

```linux
git clone https://github.com/Moabifokotsane/sendemailtowhatsapp
cd sendemailtowhatsapp
sudo python3 checkemails.py 
```

# For Whatsapp intergration 
### Use Existing Whatsapp library With:

```Python
sudo nano checkemails.py
```

then insert your Whatsapp System Code into the script.
