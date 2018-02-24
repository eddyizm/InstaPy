from instapy import InstaPy

import time
import instaMail
import random
logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
print ('lit solo')

def lit():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('lit\n')
        n.write(t+'\n')
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_dont_like(['death', 'cancer'])
        session.set_upper_follower_count(limit=5000)
        session.set_lower_follower_count(limit = 25)
        session.set_do_comment(True, percentage=20)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.like_by_tags(['astronomy','architecture','literature'], amount=40)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
        instaMail.completeTask('literature success')
    except:
        print('lit fail!')        
        instaMail.completeTask('lit fail')

lit()
