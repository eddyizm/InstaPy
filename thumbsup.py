from instapy import InstaPy

logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
# read login info from file
f = open ( logintext , 'r')
login = f.read().splitlines()

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
session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
session.set_dont_like(['death', 'cancer'])

# do the actual liking
session.like_by_tags(['wanderlust', 'rei1440project', 'nationalpark', 'vsconature', 'mountains', 'mytinyatlas' ], amount=50)
# session.like_by_tags(['gothefuckoutside', 'optoutside'], amount=50)

# end the bot session
session.end()

