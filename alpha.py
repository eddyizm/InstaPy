from instapy import InstaPy
import time

# open log file and write time
n = open('logs/timelog.txt','a+')
# get time stamp
t = time.strftime("%H:%M:%S")
#write script name and timestamp
n.write('alphapy.py\n')
n.write(t+'\n')
# read login info from file
f = open ('scripts/login.txt', 'r')
login = f.read().splitlines()
insta_username = login[0]
insta_password = login[1]
# if you want to run this script on a server, 
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
session.login()
# set up all the settings
session.set_upper_follower_count(limit=2500)
session.set_lower_follower_count(limit = 50)
# Set don't include
session.set_dont_like(['death', 'cancer'])
# do the actual liking
session.like_by_tags(['sonyalpha', 'a7r'], amount=25 )

# closing timestamp 
c = time.strftime("%H:%M:%S")
n.write(c+'\n')
n.close()
# end the bot session
session.end()
