import smtplib
import sqlite3 
from datetime import datetime
import os

if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"


def SendBody(body, d):
    f = open ( logintext , 'r')
    login = f.read().splitlines()
    f.close()
    u = login[2]
    l = login[3]
    # set up the SMTP server
    try:
        s = smtplib.SMTP(host='smtp.live.com', port=587)
        s.starttls()
        s.login(u, l)
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        msg = MIMEMultipart()       
        print('sending mail')
        msg['From']='cervantes.e@outlook.com'
        msg['To']='7149003339@msg.fi.google.com'
        msg['Subject']='Instapy Stats '+d
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
    except smtplib.SMTPException as e:
        print (str(e))


def file_len(fname):
    try: 
        count = len(open(fname).readlines())
        return count

    except IOError as e:
        print (str(e))


def daily_log():
    
    if os.name == 'nt':
        conn = sqlite3.connect("C:\\Users\\eddyizm\\Source\\Repos\\InstaPy\\db\\instapy.db")
    else:
        conn = sqlite3.connect('/Users/eduardocervantes/Downloads/Repo/InstaPy/db/instapy.db')
    # apparently you have to have a cursor with python/sqlite
    c = conn.cursor()
    # query text
    q = 'SELECT likes, comments, follows, unfollows, server_calls, created FROM statistics WHERE created > date("now","-4 day");'
    c.execute(q)
    columns = 'like | comment | follow | unfollow | server_call | created'
    day = c.fetchone()
    z = '\n%s | %s | %s | %s | %s | %s' % (day[0],day[1],day[2], day[3], day[4], day[5])
    nextday = c.fetchone()
    x = '\n%s | %s | %s | %s | %s | %s' % (nextday[0],nextday[1],nextday[2], nextday[3], nextday[4], nextday[5])
    # close db connection
    conn.close() 
    message =  columns+x+z+'\n'
    SendBody(message, nextday[5])


def completeTask(jobname):
    tStamp = datetime.now()
    n = tStamp.strftime("%Y-%m-%d")
    message = jobname + ' completed - '+ n + '\n'
    # get log info : 
    try:
        logfile = 'logs/eddyizm/general.log'
        endFile = file_len(logfile)
        n = open(logfile,'r')
        log = n.readlines()
        count = endFile-14
        if endFile > 15:
            for x in range(count, (endFile-1)):
                message+=log[x]
        else:
            pass        
        n.close()
    except IOError as e:
        print (str(e))
    
    SendBody(message, jobname)    


def archive_log():
    from shutil import copyfile
    tStamp = datetime.now()
    nLog = tStamp.strftime("%Y-%m-%d")+'_general.log'
    if os.name == 'nt':
        archive = "C:\\Users\\eddyizm\\Documents\\emailLog\\"
    else:
        archive = '/Users/eduardocervantes/Downloads/Repo/InstaPy/db/'
    
    try:
        copyfile('logs/general.log', archive+nLog)
        open('logs/general.log','w').close()
    except IOError as e:
        print (str(e))

   
if __name__ == '__main__':
    pass