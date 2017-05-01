

# Import the email modules we'll need
from email.mime.text import MIMEText
# Import smtplib for the actual sending function
import smtplib

textfile = "this is my message"

msg = MIMEText(textfile)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'test mesage'
msg['From'] = "jeremycrowley7007@gmail.com"
msg['To'] = "jeremycrowley7007@gmail.com"

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.sendmail(msg['From'], msg['to'], msg.as_string())
s.quit()