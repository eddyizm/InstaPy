from instapy import InstaPy
import instaMail
from selenium.common.exceptions import NoSuchElementException
from tempfile import gettempdir
import os

if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
try: 
    f = open ( logintext , 'r')
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
    session.set_do_comment(True, percentage=10)
    session.set_do_follow(enabled=True, percentage=10, times=2)
    session.set_comments(['Rad!', 'Super cool!', 'Excellent!', 'Amazing!'])
    session.set_dont_like(['death', 'cancer', 'rest in peace', 'restinpeace'])
    # do the actual liking
    session.like_by_tags(['painter', 'gratitude', 'offroad', 'thirdeye','earth_portraits'], amount=25)
    print('bouldering success')  
    instaMail.completeTask('bouldering success')
    
except Exception as exc:
    print('bouldering fail!')       
    print("error: {0}".format(exc))
    instaMail.completeTask('bouldering fail')
finally:
    # end the bot session
    session.end()
