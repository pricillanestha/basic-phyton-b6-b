# Youtube Don't type email, create your email bot python
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "otter8396@gmail.com"
toaddr = open('receiver_list.txt', 'r')
print('receiver_list.txt')
close()

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Pesanan "
 
body = "ISI PESAN"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Travelokapass12345!!!")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

