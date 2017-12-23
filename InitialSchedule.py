from instapy import InstaPy

import schedule
import time

def quickstart():
    try:
        f = open ('scripts/login.txt', 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
        session.login()
        session.set_upper_follower_count(limit=2500)
        session.set_lower_follower_count(limit = 50)
        session.set_dont_like(['death', 'cancer'])
        session.like_by_feed(amount=25)
        session.end()
    except Exception :
        print('quickstart fail!')

def thumbsup():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('thumbsup\n')
        n.write(t+'\n')
        f = open ('scripts/login.txt', 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_upper_follower_count(limit=1000)
        session.set_lower_follower_count(limit = 25)
        session.set_do_comment(True, percentage=20)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.set_dont_like(['death', 'cancer'])
        session.like_by_tags(['wanderlust', 'rei1440project', 'nationalpark', 'vsconature', 'mountains', 'mytinyatlas' ], amount=50)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
    except:
        print('thumbsup fail!')

def ceramics():
    try:
        #logfile
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('ceramics\n')
        n.write(t)
        #login
        f = open ('scripts/login.txt', 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        # set up all the settings
        session.set_upper_follower_count(limit=1000)
        session.set_lower_follower_count(limit = 25)
        session.set_do_comment(True, percentage=20)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:', 'Awesome!', 'Sweet!'])
        session.set_dont_include(['helloklai'])
        session.set_dont_like(['death', 'cancer'])
        # do the actual liking
        session.set_smart_hashtags(['ceramics', 'coffee', 'etsy'], limit=1, sort='top', log_tags=True)
        session.like_by_tags(amount=10, use_smart_hashtags=True)
        # logfiile  
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
    except:
        print('ceramics fail!')
    
def bouldering():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('bouldering\n')
        n.write(t+'\n')
        f = open ('scripts/login.txt', 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_upper_follower_count(limit=500)
        session.set_lower_follower_count(limit = 50)
        session.set_do_comment(True, percentage=10)
        session.set_do_follow(enabled=True, percentage=10, times=2)
        session.set_comments(['Rad!', 'Super cool!', 'Excellent!', 'Amazing!'])
        session.set_dont_like(['death', 'cancer'])
        session.like_by_tags(['bouldering', 'climbing_pictures_of_instagram', 'natgeo','rei1440project','optoutside'], amount=25)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
    except:
        print ('bouldering failed!')


schedule.every().day.at("6:35").do(quickstart)
schedule.every().day.at("10:35").do(thumbsup)
schedule.every().day.at("14:53").do(ceramics)
schedule.every().day.at("19:30").do(quickstart)
schedule.every().day.at("22:30").do(bouldering)  

while True:
    schedule.run_pending()
    time.sleep(1)