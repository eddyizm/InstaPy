from instapy import InstaPy

# read login info from file
f = open ('scripts/login.txt', 'r')
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
# session.follow_user_followers(['noel_russ'], amount=5, randomize=True)
session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:', 'Awesome!', 'Sweet!'])
session.set_dont_include(['helloklai'])
session.set_dont_like(['death', 'cancer'])

# do the actual liking
session.set_smart_hashtags(['ceramics', 'coffee', 'etsy'], limit=3, sort='top', log_tags=True)
session.like_by_tags(amount=10, use_smart_hashtags=True)

# end the bot session
session.end()

