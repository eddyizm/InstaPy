from instapy import InstaPy
from tempfile import gettempdir
from selenium.common.exceptions import NoSuchElementException
import os
import instaMail
import time
if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
print ('unfollow solo')

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