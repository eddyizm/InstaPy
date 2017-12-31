from instapy import InstaPy

import schedule
import time

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
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
        session.login()
        session.set_upper_follower_count(limit=2500)
        session.set_lower_follower_count(limit = 50)
        session.set_dont_like(['death', 'cancer'])
        session.like_by_feed(amount=50)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
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
        session.like_by_tags(['wanderlust', 'campvibes', 'nationalpark', 'vsconature', 'mountains', 'neverstopexploring' ], amount=50)
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
        n.write(t+'\n')
        #login
        f = open ('scripts/login.txt', 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        # set up all the settings
        session.set_upper_follower_count(limit=5000)
        session.set_lower_follower_count(limit = 25)
        session.set_do_comment(True, percentage=20)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:', 'Awesome!', 'Sweet!'])
        session.set_dont_include(['helloklai'])
        session.set_dont_like(['death', 'cancer'])
        session.like_by_tags(['ceramics', 'coffee', 'etsy'], amount=30)
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

def unfollow():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('unfollow\n')
        n.write(t+'\n')
        f = open ('scripts/login.txt', 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_dont_unfollow_active_users(enabled=True, posts=10)
        session.set_dont_like(['death', 'cancer'])
        session.set_dont_include(['lularoshni'])
        session.set_upper_follower_count(limit=3000)
        session.set_lower_follower_count(limit = 25)
        session.set_do_comment(True, percentage=20)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.unfollow_users(amount=2, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=10)
        session.like_by_tags(['ironbetic','quote','literature'], amount=20)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
    except:
        print('unfollow fail!')

def interact():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('interact\n')
        n.write(t+'\n')
        f = open ('scripts/login.txt', 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_upper_follower_count(limit=3000)
        session.set_lower_follower_count(limit = 25)
        session.interact_user_followers(['noel_russ'], amount=10, randomize=True)
        session.set_do_comment(True, percentage=30)
        session.set_user_interact(amount=5, randomize=True, percentage=70, media='Photo')
        session.set_do_like(enabled=True, percentage=80)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.set_do_comment(enabled=True, percentage=20)
        session.set_dont_like(['death', 'cancer'])
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
    except:
        print('interact fail!')

# scheduled methods
schedule.every().day.at("6:00").do(quickstart)
schedule.every().day.at("10:35").do(thumbsup)
schedule.every().day.at("14:30").do(ceramics)
schedule.every().day.at("19:30").do(quickstart)
schedule.every().wednesday.at("23:30").do(bouldering) 
schedule.every().monday.at("23:45").do(unfollow)
schedule.every().tuesday.at("23:30").do(quickstart)  
schedule.every().thursday.at("23:30").do(interact)  
schedule.every().friday.at("23:30").do(thumbsup)  
schedule.every().saturday.at("23:30").do(interact)  
schedule.every().sunday.at("23:30").do(quickstart)  

while True:
    schedule.run_pending()
    time.sleep(1)