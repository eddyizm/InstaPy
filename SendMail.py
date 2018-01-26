# import the smtplib module. It should be included in Python by default
import smtplib
# for pausing/debugging console window. 
import os 
f = open ('scripts/login.txt', 'r')
login = f.read().splitlines()
f.close()
u = login[2]
l = login[3]


def SendBody(body, d):
  # set up the SMTP server
  s = smtplib.SMTP(host='smtp.live.com', port=587)
  s.starttls()
  s.login(u, l)

  # import necessary packages
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText

  # create a message
  msg = MIMEMultipart()       
  print('sending mail')
  # add in the actual person name to the message template
  message = body
  
  # setup the parameters of the message
  msg['From']='cervantes.e@outlook.com'
  msg['To']='eddyizm@me.com'
  msg['Subject']='Instapy Stats '+d

  # add in the message body
  msg.attach(MIMEText(message, 'plain'))

  # send the message via the server set up earlier.
  s.send_message(msg)