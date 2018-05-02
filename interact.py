from instapy import InstaPy

import time
import instaMail
import random
import os

if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
     


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
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        u = interactUser()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_relationship_bounds(enabled=True,
            potency_ratio=-1.21,
            delimit_by_numbers=True,
            max_followers=5000,
                max_following=5555,
                min_followers=45,
                min_following=77)
        session.set_user_interact(amount=4, randomize=True, percentage=70, media='Photo')
        session.set_do_like(enabled=True, percentage=80)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.set_do_comment(enabled=True, percentage=20)
        session.set_dont_like(['death', 'cancer'])
        session.interact_user_followers([u], amount=50, randomize=True)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
        instaMail.completeTask('interact success')
    except Exception as r:
        print(r)
        instaMail.completeTask(r)
 
interact() 
