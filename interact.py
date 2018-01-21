from instapy import InstaPy

import time
import instaMail
import random

def interactUser():
    t = random.randint(0,6)
    if t == 0:
        ob = 'runningterritory'
        return ob
    elif t == 1:
        ob = 'newmexicotrue'
        return ob
    elif t == 2:
        ob = 'she_explores'
        return ob
    elif t == 3:
        ob = 'noel_russ'
        return ob
    elif t == 4:
        ob = 'mountaingirls'
        return ob
    elif t == 5:
        ob = 'sonyalpha'
        return ob
    else:
        ob = 'berniesanders'
        return ob


def interact():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('interact\n')
        n.write(t+'\n')
        f = open ('scripts/login.txt', 'r')
        login = f.read().splitlines()
        f.close()
        u = interactUser()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_upper_follower_count(limit=3000)
        session.set_lower_follower_count(limit = 25)
        session.set_user_interact(amount=4, randomize=True, percentage=70, media='Photo')
        session.set_do_like(enabled=True, percentage=80)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.set_do_comment(enabled=True, percentage=20)
        session.set_dont_like(['death', 'cancer'])
        session.interact_user_followers([u], amount=25, randomize=True)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
        instaMail.completeTask('interact success')
    except:
        print('interact fail!')
        instaMail.completeTask('interact fail')
 
interact() 