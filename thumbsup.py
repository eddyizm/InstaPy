from instapy import InstaPy
import time
import instaMail
from selenium.common.exceptions import NoSuchElementException
from tempfile import gettempdir
import os


if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"

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
        session.like_by_tags(['wanderlust', 'campvibes', 'california', 'vsconature', 'mountains', 'neverstopexploring' ], amount=50)
        instaMail.completeTask('thumbsup success')
    except Exception:
        print('thumbsup fail!')
        instaMail.completeTask('thumbsup fail')
        
    finally:
        session.end()    

if __name__ == '__main__':
    thumbsup()