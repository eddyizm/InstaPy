from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import os
import instaMail

if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
    set_workspace(path="C:\\Users\\eddyizm\\Source\\Repos\\InstaPy\\")
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
    set_workspace(path="/Users/eduardocervantes/Downloads/Repo/InstaPy/")

f = open ( logintext , 'r')
login = f.read().splitlines()
f.close()
insta_username = login[0]
insta_password = login[1]

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=6000,
                                    max_following=3000,
                                    min_followers=100,
                                    min_following=100)
    session.set_user_interact(amount=10, randomize=True, percentage=30,
                              media='Photo')
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=True, percentage=5)
    session.set_comments(
        ['Nice shot! @{}', 'I love your profile! @{}', '@{} Love it!',
        '@{} :heart::heart:', 'Very cool', 'Excellent'
        'Love your posts @{}', 'Sweet!'
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
         '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:'],
        media='Photo')

    # unfollow activity
    session.set_dont_include(['lularoshni', 'ironbetic', 'theyoungturks'])
    session.unfollow_users(amount=1, nonFollowers=True, style="RANDOM",
                           unfollow_after=42 * 60 * 60, sleep_delay=300)
    # session.unfollow_users(amount=5, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655) 
    # follow activity
    amount_number = 1
    session.follow_user_followers(['theyoungturks', 'nasa'],
                                  amount=amount_number, randomize=False,
                                  interact=True, sleep_delay=240)

    """ Joining Engagement Pods... """
    session.join_pods(topic='travel', engagement_mode='no_comments')
    instaMail.completeTask('simple script')