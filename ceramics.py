from instapy import InstaPy
import os

if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
print ('ceramics solo')
# read login info from file
f = open ( logintext , 'r')
login = f.read().splitlines()
f.close()
insta_username = login[0]
insta_password = login[1]

# if you want to run this script on a server, 
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password,  headless_browser=True)
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
session.set_dont_like(['death', 'cancer'])
# do the actual liking
session.like_by_tags(['ceramics', 'coffee', 'etsy'], amount=50 )
# end the bot session
session.end()