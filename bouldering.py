from instapy import InstaPy

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
session.set_upper_follower_count(limit=500)
session.set_lower_follower_count(limit = 50)
session.set_do_comment(True, percentage=10)
session.set_do_follow(enabled=True, percentage=10, times=2)
session.set_comments(['Rad!', 'Super cool!', 'Excellent!', 'Amazing!'])

# session.set_dont_include(['friend1', 'friend2', 'friend3'])
session.set_dont_like(['death', 'cancer'])

# do the actual liking
session.like_by_tags(['trailrunning', 'climbing_pictures_of_instagram', 'natgeo', 'rei1440project','optoutside'], amount=25)

# end the bot session
session.end()
