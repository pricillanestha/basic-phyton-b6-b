# Youtube Don't type email, create your email bot python
# dan https://stackoverflow.com/questions/3362600/how-to-send-email-attachments
# https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

fromaddr = "otter8396@gmail.com"
toaddr = open ("receiverlist.txt", "r")


msg = MIMEMultipart()
msg["Subject"] = "Daftar Pesanan "
msg["From"] = fromaddr
msg["To"] = toaddr

 
body = "Semangka, Ayam, Sapi, Sedotan"
msg.attach(MIMEText(body, "plain"))
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(fromaddr, "Travelokapass12345!!!")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

