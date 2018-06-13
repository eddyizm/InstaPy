import os
import schedule
import time
import random
from tempfile import gettempdir
from selenium.common.exceptions import NoSuchElementException
from instapy import InstaPy
import instaMail
import alpha

if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"

print ('here we go!')
def sendlog():
    instaMail.daily_log()

def quickstart():
    try:
        f = open (logintext, 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        print ('pre session creation')
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, multi_logs=True)
        session.switch_language=False
        print ('pre login')     
        session.login()
        session.set_relationship_bounds(enabled=True,
                potency_ratio=None,
                delimit_by_numbers=True,
                max_followers=5000,
                    max_following=5555,
                    min_followers=45,
                    min_following=77)
        session.set_dont_like(['death', 'cancer'])
        session.like_by_feed(amount=100, unfollow=False, randomize=True, interact=False)
        instaMail.completeTask('quickstart success')

    except Exception as exc:
        print ('quickstart fail')
        print("error: {0}".format(exc))

    finally:
        session.end()

def thumbsup():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_relationship_bounds(enabled=True,
            potency_ratio=None,
            delimit_by_numbers=True,
            max_followers=5000,
                max_following=5555,
                min_followers=45,
                min_following=77)
        session.set_do_comment(True, percentage=20)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.set_dont_like(['death', 'cancer'])
        session.like_by_tags(['wanderlust', 'campvibes', 'nationalpark', 'vsconature', 'mountains', 'neverstopexploring' ], amount=50)
        instaMail.completeTask('thumbsup success')
    except Exception:
        print('thumbsup fail!')
        instaMail.completeTask('thumbsup fail')
        
    finally:
        session.end()
    
def ceramics():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        # set up all the settings
        session.set_relationship_bounds(enabled=True,
            potency_ratio=None,
            delimit_by_numbers=True,
            max_followers=5000,
                max_following=5555,
                min_followers=45,
                min_following=77)
        session.set_do_comment(True, percentage=20)
        session.set_do_follow(enabled=True, percentage=5, times=1)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:', 'Awesome!', 'Sweet!'])
        session.set_dont_include(['helloklai'])
        session.set_dont_like(['death', 'cancer'])
        session.like_by_tags(['ceramics', 'coffee', 'etsy'], amount=25)
        instaMail.completeTask('ceramics success')
    except Exception as exc:
        print('ceramics fail!')
        instaMail.completeTask('ceramics fail!')
        # if isinstance(exc, NoSuchElementException):
        #     file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        #     with open(file_path, 'wb') as fp:
        #         fp.write(session.browser.page_source.encode('utf8'))
        #     print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
        #         '*' * 70, file_path))
        
        # raise

    finally:
        session.end()
    
def bouldering():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_relationship_bounds(enabled=True,
            potency_ratio=None,
            delimit_by_numbers=True,
            max_followers=5000,
                max_following=5555,
                min_followers=45,
                min_following=77)
        session.set_do_comment(True, percentage=20)
        session.set_do_follow(enabled=True, percentage=5, times=1)
        session.set_comments(['Rad!', 'Super cool!', u'Excellent! :thumbsup:', 'Amazing!'])
        session.set_dont_like(['death', 'cancer'])
        session.like_by_tags(['bouldering', 'streetphotography','climbing', 'trailrunning','optoutside'], amount=25)
        instaMail.completeTask('bouldering success')
    except Exception as exc:
        print ('bouldering failed!')
        instaMail.completeTask('bouldering fail!')
        # if isinstance(exc, NoSuchElementException):
        #     file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        #     with open(file_path, 'wb') as fp:
        #         fp.write(session.browser.page_source.encode('utf8'))
        #     print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
        #         '*' * 70, file_path))
        
        # raise

    finally:
        session.end()
    
def unfollow():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_dont_unfollow_active_users(enabled=True, posts=5)
        session.set_dont_include(['lularoshni', 'ironbetic'])
        session.set_dont_like(['death', 'cancer'])
        session.unfollow_users(amount=4, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=10)
        print('unfollow success!')
        instaMail.completeTask('unfollow success')
    except Exception as exc:
        print('unfollow fail!')
        instaMail.completeTask('unfollow fail')
        # if isinstance(exc, NoSuchElementException):
        #     file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        #     with open(file_path, 'wb') as fp:
        #         fp.write(session.browser.page_source.encode('utf8'))
        #     print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
        #         '*' * 70, file_path))
        
        # raise

    finally:
        session.end()

def lit():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_dont_like(['death', 'cancer'])
        session.set_relationship_bounds(enabled=True,
            potency_ratio=None,
            delimit_by_numbers=True,
            max_followers=5000,
                max_following=5555,
                min_followers=45,
                min_following=77)
        session.set_do_comment(True, percentage=20)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.like_by_tags(['astronomy','architecture','literature'], amount=40)
        instaMail.completeTask('literature success')
    except Exception as exc:
        print('lit fail!')        
        instaMail.completeTask('lit fail')
        # if isinstance(exc, NoSuchElementException):
        #     file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        #     with open(file_path, 'wb') as fp:
        #         fp.write(session.browser.page_source.encode('utf8'))
        #     print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
        #         '*' * 70, file_path))
        
        # raise

    finally:
        session.end()

def interactUser():
    ob = []
    t = random.randint(0,6)
    if t == 0:
        ob.append('runningterritory')
        return ob
    elif t == 1:
        ob.append('newmexicotrue')
        return ob
    elif t == 2:
        ob.append('theyoungturks')
        return ob
    elif t == 3:
        ob.append('noel_russ')
        return ob
    elif t == 4:
        ob.append('mountaingirls')
        return ob
    elif t == 5:
        ob.append('sonyalpha')
        return ob
    else:
        ob.append('berniesanders')
        return ob

def interact():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        u = interactUser()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
        session.login()
        session.set_relationship_bounds(enabled=True,
            potency_ratio=None,
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
        session.interact_user_followers(u, amount=25, randomize=True)
        instaMail.completeTask('interact success')
    except Exception as exc:
        print('interact fail!')
        instaMail.completeTask('interact fail')
        
    finally:
        session.end()

# scheduled methods
schedule.every().day.at("5:15").do(quickstart)
schedule.every().day.at("9:30").do(thumbsup)
schedule.every().day.at("14:00").do(interact)
schedule.every().day.at("5:00").do(sendlog)
schedule.every().day.at("19:30").do(alpha.alpha)
schedule.every().wednesday.at("23:30").do(bouldering) 
schedule.every().tuesday.at("2:45").do(unfollow)
schedule.every().monday.at("23:45").do(lit)
schedule.every().tuesday.at("23:30").do(interact)  
schedule.every().thursday.at("23:30").do(ceramics)  
schedule.every().friday.at("23:30").do(thumbsup)  
schedule.every().saturday.at("23:30").do(quickstart)  
schedule.every().sunday.at("23:30").do(alpha.alpha)  

while True:
    schedule.run_pending()
    time.sleep(1)
