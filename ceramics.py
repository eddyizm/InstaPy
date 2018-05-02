from instapy import InstaPy
import time

# open log file and write time
n = open('logs/timelog.txt','a+')
# get time stamp
t = time.strftime("%H:%M:%S")
#write script name and timestamp
n.write('ceramics.py\n')
n.write(t)
logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
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
session.set_upper_follower_count(limit=1000)
session.set_lower_follower_count(limit = 25)
session.set_do_comment(True, percentage=20)
session.set_do_follow(enabled=True, percentage=10, times=2)
session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:', 'Awesome!', 'Sweet!'])
session.set_dont_include(['helloklai'])
session.set_dont_like(['death', 'cancer'])

# do the actual liking
session.set_smart_hashtags(['ceramics', 'coffee', 'etsy'], limit=1, sort='top', log_tags=True)
session.like_by_tags(amount=10, use_smart_hashtags=True)

# closing timestamp 
c = time.strftime("%H:%M:%S")
n.write(c)
n.close()
# end the bot session
session.end()