from instapy import InstaPy
from instapy import set_workspace
from tempfile import gettempdir
from selenium.common.exceptions import NoSuchElementException
import os
import instaMail
import time
import regex


if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
    set_workspace(path="C:\\Users\\eddyizm\\Source\\Repos\\InstaPy\\")
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
    set_workspace(path="/Users/eduardocervantes/Downloads/Repo/InstaPy/")

print ('unfollow solo')

def unfollow():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, multi_logs=True)
        session.switch_language=False
        session.login()
        session.set_dont_unfollow_active_users(enabled=True, posts=5)
        session.set_dont_include(['lularoshni', 'ironbetic'])
        session.unfollow_users(amount=10, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=90*60*60, sleep_delay=501)
        print('unfollow success!')
        instaMail.completeTask('unfollow success')
    except Exception as exc:
        print('unfollow fail!')
        print("error: {0}".format(exc))
        instaMail.completeTask('unfollow fail')
        
    finally:
        # end the bot session
        session.end()

unfollow()