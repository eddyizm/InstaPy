from instapy import smart_run
from instapy import InstaPy
from instapy import set_workspace
import os
import interact
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
session = InstaPy(username=insta_username, password=insta_password)
# session.set_dont_like(['death', 'cancer', 'rest in peace', 'restinpeace'])
# let's go! :>
with smart_run(session):
    # don't like if a post already has more than 150 likes
    session.set_delimit_liking(enabled=True, max_likes=150, min_likes=0)

    # don't comment if a post already has more than 4 comments
    session.set_delimit_commenting(enabled=True, max_comments=4, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-0.50,
                                    delimit_by_numbers=True,
                                    max_followers=2000,
                                    max_following=3500,
                                    min_followers=25,
                                    min_following=25)
    session.set_do_comment(True, percentage=20)
    session.set_do_follow(enabled=True, percentage=20, times=2)
    session.set_comments(['Amazing!', 'Awesome!!', 'Cool!', 'Good one!',
                          'Really good one', 'Love this!', 'Like it!',
                          'Beautiful!', 'Great!', 'Nice one'])
    session.set_sleep_reduce(200)

    """ Get the list of non-followers
        I duplicated unfollow_users() to see a list of non-followers which I 
        run once in a while when I time
        to review the list
    """
    # session.just_get_nonfollowers()
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments_d", "follows",
                                              "unfollows", "server_calls_h"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_daily=(100, 700),
                                 peak_comments_daily=(25, 200),
                                 peak_follows_daily=(48, 125),
                                 peak_unfollows_daily=(35, 400),
                                 peak_server_calls_daily=3000)
    """ Actions start here """
    # Unfollow users
    session.unfollow_users(amount=10, instapy_followed_enabled=True,
                           style="RANDOM",
                           unfollow_after=168 * 60 * 60,
                           sleep_delay=600)

    session.like_by_tags(['outdoorwomen', 'sundaymood', 'hellatrails', 'climbing','ohio'], amount=25)
    session.set_dont_include(['lularoshni', 'ironbetic', 'theyoungturks'])
    vUser = interact.interactUser()
    session.follow_user_followers([vUser],
                                  amount=3, randomize=False,
                                  interact=True, sleep_delay=240)

    instaMail.completeTask('instapy session complete.')
    # Remove specific users immediately
    """ I use InstaPy only for my personal account, I sometimes use custom 
    list to remove users who fill up my feed
        with annoying photos
    # custom_list = ["sexy.girls.pagee", "browneyedbitch97"]
    #
    # session.unfollow_users(amount=20, customList=(True, custom_list,
    # "all"), style="RANDOM",
    #                        unfollow_after=1 * 60 * 60, sleep_delay=200)
    """    