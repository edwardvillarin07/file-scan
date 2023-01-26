import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

download_folder = 'PATH WHERE YOU WANT TO SCAN'
extensions = ('.pdf', '.txt','.png','.jpg','.GIF','.gif','.rar','.zip') # Scanning File Extension you can add or change just follow the format

msg = MIMEMultipart()
msg['Subject'] = 'Downloads'
msg['From'] = 'YOUREMAIL'
msg['To'] = 'RECEIVER EMAIL'

for file in os.listdir(download_folder):
    if file.endswith(extensions):
        with open(os.path.join(download_folder, file), 'rb') as f:
            file_data = f.read()
        file_name = os.path.basename(file)
        attachment = MIMEApplication(file_data, _subtype='txt')
        attachment.add_header('content-disposition', 'attachment', filename=file_name)
        msg.attach(attachment)

# send the email
server = smtplib.SMTP('HOST', 587) # Change the port, For SSL is 465  | For Non-SSL 587
server.starttls()
server.login('YOUREMAIL', 'YOURPASSWORD')
server.send_message(msg)
print("SEND!")
server.quit()