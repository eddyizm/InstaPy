from instapy import InstaPy

import time
import instaMail
import random
logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
print ('u2')

def unfollow():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('unfollow\n')
        n.write(t+'\n')
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_dont_unfollow_active_users(enabled=True, posts=10)
        session.set_dont_include(['lularoshni', 'ironbetic', 'theyoungturks'])
        session.set_dont_like(['death', 'cancer'])
        session.unfollow_users(amount=2, onlyNotFollowMe=True,  sleep_delay=30)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
        instaMail.archive_log()
        instaMail.completeTask('unfollow success')
    except:
        print('unfollow fail!')
        instaMail.completeTask('unfollow fail')

unfollow()