from instapy import InstaPy

# read login info from file
f = open ('scripts/login.txt', 'r')
login = f.read().splitlines()

insta_username = login[0]
insta_password = login[1]

# if you want to run this script on a server, 
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# set up all the settings
session.set_upper_follower_count(limit=1000)
session.set_lower_follower_count(limit = 50)

# session.set_dont_include(['friend1', 'friend2', 'friend3'])
session.set_dont_like(['death', 'cancer'])

# do the actual liking
# session.like_by_tags(['natgeo', 'world'], amount=100)
session.like_by_feed(amount=200)

# end the bot session
session.end()
