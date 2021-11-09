"""#Hacker News Headlines Emailer

REQUEST LIB - HTTP request.

BEAUTIFUL SOUP - WEB SCRAPING.

SMTP LIB - email authentication and email transaction.

EMAIL.MIME - creating the email body.

DATETIME - accessing or manipulating date and time.

NOTE: Request and bs4 are external lib. and others are default lib.
"""

import requests
from bs4 import BeautifulSoup

import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

now = datetime.datetime.now()

#email content placeholder
content = '' 

#extracting hacker news stories

def extract_news(url):
  print("Extracting")
  cnt = ''
  cnt+=('<b>HN Top Stories</b>\n'+'<br>'+'-'*50+'<br>'+'\n<br>')
  response = requests.get(url)
  content = response.content
  soup = BeautifulSoup(content,'html.parser')
  for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
      cnt+= ((str(i+1)+' ::'+tag.text + "\n"+'<br>')if tag.text!='More' else '')
  return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content +=cnt
#print(content)
content += ("<br>-----------<br>")
content += ('<br><br>End of message')

"""How to send an email with Gmail as provider using Python?

1.Google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure", so what you have to do is go to this link while you're logged in to your google account, and allow the access


https://www.google.com/settings/security/lesssecureapps



2.Still not working? If you still get the SMTPAuthenticationError but now the code is 534, its because the location is unknown. Follow this link:

https://accounts.google.com/DisplayUnlockCaptcha



Note: I have 2-Step Verification enabled on my account. App Password works with this! (for gmail smtp setup, you must go to https://support.google.com/accounts/answer/185833?hl=en and follow the below steps)

This setting is not available for accounts with 2-Step Verification enabled. Such accounts require an application-specific password for less secure apps access.
"""

#sending the mail
print("composing email")

SERVER = "smtp.gmail.com" #smtp server for gmail
PORT = 587 
FROM = "XXXXXXXXXXXXXXXXX"
TO = "XXXXXXXXXXXXXXXXX"  #It can be list of emails
PASS = '************' #password of the mail-ID


#fp = open(file_name, 'rb')
#Create a text/plain message
# msg = MIMEText('')
msg = MIMEMultipart()

#msg.add_header('Content-disposition','attachment',filename= 'empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated email]'+ '' + str(now.day) + '-' + str(now.month)+ '-' + str(now.year)
msg['From'] = FROM
msg['To']  = TO
msg.attach(MIMEText(content, 'html'))  #making the message an html format
#fp.close()

print('Initiating Server...')
server = smtplib.SMTP(SERVER,PORT)
#server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.set_debuglevel(1) #(1)shows the errors if task not executed, (0)skips it.
server.ehlo()
server.starttls()
#server.ehlo
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print('Email sent...')
server.quit()
