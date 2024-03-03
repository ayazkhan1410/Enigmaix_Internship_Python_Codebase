# Import the smtplib library
import smtplib

# Create an SMTP object
obj = smtplib.SMTP("smtp.gmail.com", 587)

# Start TLS encryption
obj.starttls()

# Login to your Gmail account
obj.login("youremail@gmail.com", "Password")

# Define email subject and body
subject = "Sending message using Python"
body = "Hi there, I am here to inform you that I am fine and I will join the company as soon as possible"

# Format the message
message = f"Subject: {subject}\n\n{body}"

# List of recipient email addresses
list_of_addresses = ["samplemail69@gmail.com"]

# Send the email
obj.sendmail("youremail@gmail.com", list_of_addresses, message)

# Print a success message
print("Email sent successfully...")

# Quit the SMTP session
obj.quit()
