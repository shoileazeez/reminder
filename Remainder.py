import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define email parameters
sender_email = "your_email@example.com"
receiver_email = "recipient@example.com"
subject = "Test Email from Python"
body = "This is a test email sent from Python."

# Create the MIMEText object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the email body to the message
msg.attach(MIMEText(body, 'plain'))

# Set up the SMTP server
smtp_server = "smtp.example.com"  # e.g., smtp.gmail.com for Gmail
port = 587  # For SSL, use 465
login = "your_email@example.com"
password = "your_password"

try:
    # Connect to the server and start TLS
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    
    # Log in to the server
    server.login(login, password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    
finally:
    server.quit()
