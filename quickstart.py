from instapy import InstaPy

import schedule
import time
import instaMail
import random

print ('quickstart solo')

def quickstart():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('quickstart\n')
        n.write(t+'\n')
        f = open ('scripts/login.txt', 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, multi_logs=True)
        session.login()
        session.set_upper_follower_count(limit=5000)
        session.set_lower_follower_count(limit = 50)
        session.set_dont_like(['death', 'cancer'])
        session.like_by_feed(amount=50, unfollow=False, randomize=True, interact=True)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        instaMail.completeTask('quickstart success')
    except Exception :
        print('quickstart fail!')
        instaMail.completeTask('quickstart fail!')
    finally:
    # end the bot session
    session.end()    
        
quickstart()        

