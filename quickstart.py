import os
import time
from tempfile import gettempdir
from selenium.common.exceptions import NoSuchElementException
from instapy import InstaPy
import instaMail


if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
print ('quickstart solo')

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
                potency_ratio=-1.21,
                delimit_by_numbers=True,
                max_followers=5000,
                    max_following=5555,
                    min_followers=45,
                    min_following=77)
        session.set_dont_like(['death', 'cancer'])
        session.like_by_feed(amount=50, unfollow=False, randomize=True, interact=True)
        session.end() 
        instaMail.completeTask('quickstart success')

    except Exception as exc:
        # if changes to IG layout, upload the file to help us locate the change
        if isinstance(exc, NoSuchElementException):
            file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
            with open(file_path, 'wb') as fp:
                fp.write(session.browser.page_source.encode('utf8'))
            print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
                '*' * 70, file_path))
        
        raise

    finally:
        session.end()
        
quickstart()        