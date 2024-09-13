from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText

# Email content
subject = "Test Email"
body = "This is a test email sent from Python."
sender_email = "mohit.bansal623@gmail.com"
receiver_email = "mohit.bansal623@gmail.com"
password = "iokz uzjn ieev ccyi"

# Create a plain-text message
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Establish a connection to the SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # Secure the connection
    server.login(sender_email, password)  # Log in to your email account
    server.sendmail(sender_email, receiver_email,
                    msg.as_string())  # Send the email

print("Email sent successfully!")


subject = "Test Email"
body = "This is a test email."

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Error: Unable to authenticate.")
except smtplib.SMTPConnectError:
    print("Error: Unable to connect to the server.")
except Exception as e:
    print(f"An error occurred: {e}")


# HTML content
html = """
<html>
  <body>
    <h1>Hello!</h1>
    <p>This is an <b>HTML</b> email sent from Python!</p>
  </body>
</html>
"""

# Email details
subject = "Test HTML Email"

# Create an HTML message
msg = MIMEText(html, "html")
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("HTML email sent successfully!")


# Email details
subject = "Email with Attachment"
body = "Please find the attached document."

# Create a multipart message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the email body
msg.attach(MIMEText(body, "plain"))

# Attach the file
filename = "random_demo.py"
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={filename}")
    msg.attach(part)

# Send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email with attachment sent successfully!")
