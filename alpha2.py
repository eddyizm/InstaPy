from instapy import InstaPy
import time
import instaMail
from selenium.common.exceptions import NoSuchElementException
from tempfile import gettempdir
import os


if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"

def alpha():
    try:
        print ('alpha script')
        f = open ( logintext , 'r')
        login = f.read().splitlines()
        f.close()
        insta_username = login[0]
        insta_password = login[1]
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
        session.login()
        session.set_dont_like(['death', 'cancer', 'rest in peace', 'restinpeace'])
        session.set_relationship_bounds(enabled=True,
                potency_ratio=None,
                delimit_by_numbers=True,
                max_followers=5000,
                    max_following=5555,
                    min_followers=45,
                    min_following=77)
        session.set_do_comment(True, percentage=30)
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.like_by_tags(['passionpassport', 'travelgirls', 'gonewzealand'], amount=50 )
        print('alpha2 success')  
        instaMail.completeTask('alpha2 success')
    except Exception as exc:
        print('alpha2 fail!')       
        print("error: {0}".format(exc))
        instaMail.completeTask('alpha2 fail')
        # if changes to IG layout, upload the file to help us locate the change
        #if isinstance(exc, NoSuchElementException):
            # file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
            # with open(file_path, 'wb') as fp:
            #     fp.write(session.browser.page_source.encode('utf8'))
            # print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            #     '*' * 70, file_path))
        # full stacktrace when raising Github issue
        
    finally:
        # end the bot session
        session.end()
       
alpha()

'''
 # #livefolk # # #traveldiary 
 #instadaily #featuremeseas #featuremeof #hinfluencercollective 
 #earth_portraits # #femmetravel #featuremeof #l0tsabraids 
 # #seamyphotos #bravogreatphoto # 
 #wtnadventures #l0tsabraids #ftwotww #expofilm #ftmedd #portraitsvisuals 
 # #portraits_universe #gramkilla #artofvisual
 #myerasmus #dji #engineer #erasmus 
 #dbtravel #turkmen #  #blagoevgrad #bulgaria  #aubg #campus #2018 #senior #collegelife
#artnude #purenewzealand #
#kilonewton #textiles #artmatsdm #charecterdesign
# #teamcanon # 
 #folkgoood # #roadtrip #dreaming # # # #folkcreative  
 #ingrande_crew #calabria #loves_united_calabria #loves_united_italia #volgocalabria 
 #volgoitalia #ig_italia # #italia #calabriadaamare  #vivocalabria #like4follow 
 #verso_sud #yallerscalabria #follow4follow #yallersitalia #italia_inunoscatto #likeforlike
 #italiainunoscatto_hdr #ig_calabria #ig_crotone #igreggiocalabria #instanlikes #igcosenzan
 #landscape_captures #followback # #topfrancephoto 
 #ig_worldclub # #followme #super_europe 
 # #follow4follow #nature_perfection #worldtravelpics
 #igphoto # #igersworldwide #ig_captures #igs_photos #ig_daily #worldbestgram #splendid_shotz
 #proud #lol #smile #snapback # #pushthroughit #igotthis 
 #almostthere # #fit #fitnessfreaks #fit#  #healthy #tone 
 #tanlines #cutoffs #countrylife #farm #
 #noh8 #blessed #keeppushing #keepgoing   #blah #icute #summertime
  #artnude  #sensual_art # #longhair # #bodyscape # #sexypose # # #impliednude #passion #eroticart #shotsosensual #bodypositivity #ass'
 '''