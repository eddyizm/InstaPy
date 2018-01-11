import smtplib
import sqlite3 
from datetime import datetime

def SendBody(body, d):
    f = open ('scripts/login.txt', 'r')
    login = f.read().splitlines()
    f.close()
    u = login[2]
    l = login[3]
    # set up the SMTP server
    try:
        s = smtplib.SMTP(host='smtp.live.com', port=587)
        s.starttls()
        s.login(u, l)

        # import necessary packages
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # create a message
        msg = MIMEMultipart()       
        print('sending mail')
        
        # setup the parameters of the message
        msg['From']='cervantes.e@outlook.com'
        msg['To']='eddyizm@me.com'
        msg['Subject']='Instapy Stats '+d

        # add in the message body
        msg.attach(MIMEText(body, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
    except smtplib.SMTPException as e:
        print (str(e))

def file_len(fname):
    try: 
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
    except IOError as e:
        print (str(e))

def daily_log():
    #get follower count 
    fCount = file_len('logs/followerNum.txt')
    f = open('logs/followerNum.txt','r').readlines()
    s = f[fCount-1]
    followers = 'followers: '+(s[-5:]+'\n')
    # Access DB and parse out data.
    conn = sqlite3.connect('C:\\Users\\eddyizm\\Source\\Repos\\InstaPy\\db\\instapy.db')
    # apparently you have to have a cursor with python/sqlite
    c = conn.cursor()
    # query text
    q = 'SELECT likes, comments, follows, unfollows, server_calls, created FROM statistics WHERE created > date("now","-4 day");'
    results = c.execute(q)
    columns = 'like | comment | follow | unfollow | server_call | created'
    day = c.fetchone()
    z = '\n%s | %s | %s | %s | %s | %s' % (day[0],day[1],day[2], day[3], day[4], day[5])
    nextday = c.fetchone()
    x = '\n%s | %s | %s | %s | %s | %s' % (nextday[0],nextday[1],nextday[2], nextday[3], nextday[4], nextday[5])
    # close db connection
    conn.close() 
    message =  followers+columns+x+z+'\n'

    # get log info : 
    endFile = file_len('logs/timelog.txt')
    n = open('logs/timelog.txt','r')
    log = n.readlines()
    count = endFile-15
    for x in range(count, (endFile)):
        message+=log[x]
    n.close()
    # print(message)
    SendBody(message, nextday[5])

def completeTask(jobname):
    # fCount = file_len('logs/general.log')
    tStamp = datetime.now()
    n = tStamp.strftime("%Y-%m-%d")
    # import modules. 
    from shutil import copyfile
    message = 'function: '+jobname +' completed'
    # get log info : 
    try:
        logfile = 'logs/general.log'
        endFile = file_len(logfile)
        n = open(logfile,'r')
        log = n.readlines()
        count = endFile-100
        for x in range(count, (endFile-1)):
            message+=log[x]
        n.close()
    except IOError as e:
        print (str(e))
    SendBody(message, jobname)    
    
def archive_log():
    from shutil import copyfile
    tStamp = datetime.now()
    nLog = tStamp.strftime("%Y-%m-%d")+'_general.log'
    try:
        copyfile('logs/general.log', 'C:\\Users\\eddyizm\\Documents\\emailLog\\'+nLog)
        open('logs/general.log','w').close()
    except IOError as e:
        print (str(e))