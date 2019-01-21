from instapy import InstaPy

import time
import instaMail
import random
import os
if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
print ('lit solo')
def lit():
    try:
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, multi_logs=True)
        session.switch_language=False
        session.login()
        session.set_relationship_bounds(enabled=True,
                    potency_ratio=None,
                    delimit_by_numbers=True,
                    max_followers=5000,
                        max_following=5555,
                        min_followers=45,
                        min_following=77)
        session.set_dont_like(['death', 'cancer', 'rest in peace', 'restinpeace'])
        session.set_do_comment(True, percentage=20)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.like_by_tags(['literature','SalomonSquad','igersworldwide'], amount=40)
        session.end()
        instaMail.completeTask('literature success')
    except Exception as exc:
        print('lit fail!')        
        print("error: {0}".format(exc))
        instaMail.completeTask('lit fail')

lit()
