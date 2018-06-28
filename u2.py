from instapy import InstaPy
from tempfile import gettempdir
from selenium.common.exceptions import NoSuchElementException
import os
import instaMail


if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
print ('u2')

def unfollow():
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
        session.set_dont_include(['lularoshni', 'ironbetic', 'theyoungturks'])
        session.set_dont_like(['death', 'cancer'])
        session.unfollow_users(amount=2, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=30)
        print ('u2 success')
        instaMail.completeTask('u2 success')
    except Exception as exc:
        print ('u2 fail')
        instaMail.completeTask('u2 fail')
        # if changes to IG layout, upload the file to help us locate the change
        # if isinstance(exc, NoSuchElementException):
        #     file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        #     with open(file_path, 'wb') as fp:
        #         fp.write(session.browser.page_source.encode('utf8'))
        #     print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
        #         '*' * 70, file_path))
        # # full stacktrace when raising Github issue
        # raise

    finally:
        # end the bot session
        session.end()
        

unfollow()