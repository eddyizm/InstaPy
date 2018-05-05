from instapy import InstaPy
import time
import instaMail
from selenium.common.exceptions import NoSuchElementException
from tempfile import gettempdir
import os

print ('alpha script')
if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"

def alpha():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
        session.login()
        session.set_dont_like(['death', 'cancer'])
        session.set_relationship_bounds(enabled=True,
                potency_ratio=None,
                delimit_by_numbers=True,
                max_followers=5000,
                    max_following=5555,
                    min_followers=45,
                    min_following=77)
        session.set_do_comment(True, percentage=30)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.like_by_tags(['igersitalia', 'creativeminds', 'imagine'], amount=50 )
        session.end()
        print('alpha success')  
        #instaMail.completeTask('alpha success')
    except Exception as exc:
        print('alpha fail!')        
        #instaMail.completeTask('alpha fail')
        # if changes to IG layout, upload the file to help us locate the change
        #if isinstance(exc, NoSuchElementException):
            # file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
            # with open(file_path, 'wb') as fp:
            #     fp.write(session.browser.page_source.encode('utf8'))
            # print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            #     '*' * 70, file_path))
        # full stacktrace when raising Github issue
        
    finally:
        # end the bot session
        session.end()
        
        

alpha()
# #liveamplified
'''
#photo #vlog #hamburg 
#mavicpro # #myerasmus #dji #panasonic 
#engineer # #germany #sexy #creative #erasmus 
# #machupicchu  #waynapicchu #dbtravel 
#turkmen #turkmengirl  #blagoevgrad #bulgaria  #aubg #campus #2018 #senior #collegelife'
'''