from instapy import InstaPy

import schedule
import time
import instaMail
import random
logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
print ('quickstart solo')

def quickstart():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('quickstart\n')
        n.write(t+'\n')
        f = open (logintext, 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        print ('pre session creation')
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
        session.switch_language=False
        print ('pre login')     
        session.login()

        session.set_upper_follower_count(limit=5000)
        session.set_lower_follower_count(limit = 50)
        session.set_dont_like(['death', 'cancer'])
        session.like_by_feed(amount=50, unfollow=False, randomize=True, interact=True)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        #instaMail.completeTask('quickstart success')
        session.end() 
    except Exception:
        print('quickstart fail!')
        #instaMail.completeTask('quickstart fail!')
    finally:
        # end the bot session
        pass   
        
quickstart()        

