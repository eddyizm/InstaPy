from instapy import InstaPy
import time
import instaMail
print ('alpha script')
logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"

def alpha():
    try:
        n = open('logs/timelog.txt','a+')
        t = time.strftime("%H:%M:%S")
        n.write('alphapy.py\n')
        n.write(t+'\n')
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
        session.login()
        session.set_dont_like(['death', 'cancer'])
        session.set_upper_follower_count(limit=5000)
        session.set_lower_follower_count(limit = 25)
        session.set_do_comment(True, percentage=30)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.like_by_tags(['fullerton', 'ghosttown', 'space'], amount=50 )
        c = time.strftime("%H:%M:%S")
        n.write(c+'\n')
        n.close()      
        session.end()
        instaMail.completeTask('alpha success')
    except:
        print('alpha fail!')        
        instaMail.completeTask('alpha fail')

alpha()
# #liveamplified
'''
#creativeminds #photo #vlog #hamburg 
# #mavicpro #lumix #myerasmus #dji #panasonic #life #imagine 
# #engineer #sweden #germany #sexy #creative #erasmus 
# # #machupicchu  #waynapicchu #dbtravel #science
'''