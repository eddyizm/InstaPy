from instapy import InstaPy

import schedule
import time
import instaMail
import random
import os

if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"

print ('here we go!')
def sendlog():
    instaMail.daily_log()

def quickstart():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('quickstart\n')
        n.write(t+'\n')
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
        session.login()
        session.set_upper_follower_count(limit=5000)
        session.set_lower_follower_count(limit = 50)
        session.set_dont_like(['death', 'cancer'])
        session.like_by_feed(amount=35, unfollow=False, randomize=True, interact=True)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
        instaMail.completeTask('quickstart success')
    except Exception :
        print('quickstart fail!')
        instaMail.completeTask('quickstart fail!')

def thumbsup():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('thumbsup\n')
        n.write(t+'\n')
        f = open ( logintext , 'r')
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
        instaMail.completeTask('thumbsup success')
    except:
        print('thumbsup fail!')
        instaMail.completeTask('thumbsup fail')

def ceramics():
    try:
        #logfile
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('ceramics\n')
        n.write(t+'\n')
        #login
        f = open ( logintext , 'r')
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
        session.like_by_tags(['ceramics', 'coffee', 'etsy'], amount=25)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
        instaMail.completeTask('ceramics success')
    except:
        print('ceramics fail!')
        instaMail.completeTask('thumbsup fail!')
    
def bouldering():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('bouldering\n')
        n.write(t+'\n')
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_upper_follower_count(limit=500)
        session.set_lower_follower_count(limit = 50)
        session.set_do_comment(True, percentage=20)
        session.set_do_follow(enabled=True, percentage=5, times=1)
        session.set_comments(['Rad!', 'Super cool!', u'Excellent! :thumbsup:', 'Amazing!'])
        session.set_dont_like(['death', 'cancer'])
        session.like_by_tags(['bouldering', 'streetphotography','climbing_pictures_of_instagram', 'trailrunning','optoutside'], amount=25)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
        instaMail.completeTask('bouldering success')
    except:
        print ('bouldering failed!')
        instaMail.completeTask('bouldering fail!')

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
        session.set_dont_include(['lularoshni', 'ironbetic'])
        session.set_dont_like(['death', 'cancer'])
        session.unfollow_users(amount=2, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=10)
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
        instaMail.archive_log()
        instaMail.completeTask('unfollow success')
    except:
        print('unfollow fail!')
        instaMail.completeTask('unfollow fail')

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

# scheduled methods
schedule.every().day.at("5:15").do(quickstart)
schedule.every().day.at("9:30").do(thumbsup)
schedule.every().day.at("14:00").do(interact)
schedule.every().day.at("5:00").do(sendlog)
schedule.every().day.at("19:30").do(quickstart)
schedule.every().wednesday.at("23:30").do(bouldering) 
schedule.every().tuesday.at("2:45").do(unfollow)
schedule.every().monday.at("23:45").do(lit)
schedule.every().tuesday.at("23:30").do(quickstart)  
schedule.every().thursday.at("23:30").do(ceramics)  
schedule.every().friday.at("23:30").do(thumbsup)  
schedule.every().saturday.at("23:30").do(interact)  
schedule.every().sunday.at("23:30").do(quickstart)  

while True:
    schedule.run_pending()
    time.sleep(1)
