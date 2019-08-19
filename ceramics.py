from instapy import InstaPy
from instapy import set_workspace
import os

if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
    set_workspace(path="C:\\Users\\eddyizm\\Source\\Repos\\InstaPy\\")
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
    set_workspace(path="/Users/eduardocervantes/Downloads/Repo/InstaPy/")
    
print ('ceramics solo')
# read login info from file
f = open ( logintext , 'r')
login = f.read().splitlines()
f.close()
insta_username = login[0]
insta_password = login[1]

session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, multi_logs=True)
session.switch_language=False
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
session.set_do_follow(enabled=True, percentage=10, times=2)
session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:', 'Awesome!', 'Sweet!'])
session.set_dont_include(['helloklai'])
session.set_dont_like(['death', 'cancer', 'rest in peace', 'restinpeace'])
# do the actual liking
session.like_by_tags(['sql', 'python', 'florida'], amount=50 )
# end the bot session
session.end()