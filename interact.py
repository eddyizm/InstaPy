from instapy import InstaPy
from selenium.common.exceptions import NoSuchElementException
from tempfile import gettempdir
import time
import instaMail
import random
import os

if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
     
def interactUser():
    ob = []
    t = random.randint(0,6)
    if t == 0:
        ob.append('eddyizm')
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
        ob.append('cbioffroadfab')
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
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, multi_logs=True)
        session.switch_language=False
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
        session.set_dont_like(['death', 'cancer', 'rest in peace', 'restinpeace'])
        session.interact_user_followers(u, amount=50, randomize=True)
        print('interact success')
        instaMail.completeTask('interact success')
    except Exception as exc:
        print('interact fail')
        if isinstance(exc, NoSuchElementException):
            print('NoSuchElementException')
            file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
            with open(file_path, 'wb') as fp:
                fp.write(session.browser.page_source.encode('utf8'))
            print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
                '*' * 70, file_path))
        
        raise

    finally:
        session.end()
           # end the bot session
        
         
interact() 
