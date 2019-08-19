from instapy import InstaPy
from instapy import smart_run
from tempfile import gettempdir
from selenium.common.exceptions import NoSuchElementException
import os
import instaMail


if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
    set_workspace(path="C:\\Users\\eddyizm\\Source\\Repos\\InstaPy\\")
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
    set_workspace(path="/Users/eduardocervantes/Downloads/Repo/InstaPy/")

print ('u2')

def unfollow():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
        session.switch_language=False
        session.login()
        session.set_relationship_bounds(enabled=True,
        potency_ratio=None,
        delimit_by_numbers=True,
        max_followers=5000,
            max_following=5555,
            min_followers=45,
            min_following=77)
        session.set_dont_include(['lularoshni', 'ironbetic', 'theyoungturks'])
        session.unfollow_users(amount=5, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
        print ('u2 success')
        instaMail.completeTask('u2 success')
    except Exception as exc:
        print ('u2 fail')
        instaMail.completeTask('u2 fail')
        print("error: {0}".format(exc))
           

if __name__ == '__main__':        
    unfollow()