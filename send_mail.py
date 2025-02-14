import smtplib
from email.message import EmailMessage
import imghdr

email_sender = "YOUR_GMAIL@gmail.com"
password = "YOUR_PASSWORD"
receiver = "YOUR_GMAIL@gmail.com"

def send_email(image_path):

    print("send_email function started")

    email_message = EmailMessage()
    email_message["Subject"] = "New Object Detected !"
    email_message.set_content("Identified a new object.")

    with open(image_path, 'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email_sender, password)
    gmail.sendmail(email_sender, receiver, email_message.as_string())
    gmail.quit()
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/image126.png")
