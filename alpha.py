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
        session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, multi_logs=True)
        session.switch_language=False
        session.login()
        session.set_dont_like(['death', 'cancer'])
        session.set_relationship_bounds(enabled=True,
                potency_ratio=None,
                delimit_by_numbers=True,
                max_followers=5000,
                    max_following=5555,
                    min_followers=45,
                    min_following=77)
        session.set_do_comment(True, percentage=30)
        session.set_dont_like(['death', 'cancer', 'rest in peace', 'restinpeace'])
        session.set_comments([u':clap:', u':thumbsup:', u':raised_hands:'])
        session.like_by_tags(['nudeart', 'wonderful_places', 'gothefuckoutside'], amount=50 )
        print('alpha success')  
        instaMail.completeTask('alpha success')
    except Exception as exc:
        print('alpha fail!')   
        print("error: {0}".format(exc))  
        if isinstance(exc, NoSuchElementException):
            print('NoSuchElementException')
            file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
            with open(file_path, 'wb') as fp:
                fp.write(session.browser.page_source.encode('utf8'))
            print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
                '*' * 70, file_path))
        
        instaMail.completeTask('alpha fail')
        raise   
        
        
        
    finally:
        # end the bot session
        session.end()
       
if __name__ == '__main__':
    alpha()

'''
#photo #vlog #mavicpro #myerasmus #dji # #engineer # #germany  #creative #erasmus 
 #dbtravel #turkmen #  #blagoevgrad  #aubg #campus #2018 #senior #collegelife
# # # #explorenewzealand #purenewzealand #gonewzealand
#kilonewton #renewableenergy #engineering #greenenergy
#functionalart  # #artmatsdm  #charecterdesign
# #roamtheplanet #teamcanon #folkgreen  
 #folkgoood  # # #roadtrippin  #dreaming # #moodynature #exploremore #  
 #ingrande_crew #calabria #loves_united_calabria #loves_united_italia #volgocalabria 
 #volgoitalia #ig_italia #igerscalabria #italia #calabriadaamare #like4like #vivocalabria #like4follow 
 #verso_sud #yallerscalabria #follow4follow #yallersitalia #italia_inunoscatto #likeforlike
 #italiainunoscatto_hdr #ig_calabria #ig_crotone #igreggiocalabria # #igcosenzan
 #underwater  #landscape_captures #followback #ig_europe #topfrancephoto 
 #ig_worldclub #followbackinstantly #followme # #igworldclub 
 # # #nature_perfection #
 #igphoto # #igersworldwide #ig_captures #igs_photos #ig_daily #worldbestgram #splendid_shotz
 #proud #lol #smile #snapback # #pushthroughit #igotthis 
 #almostthere #determination #fit  #tone 
 #tanlines # # #farm 
 #noh8 #blessed #keeppushing #keepgoing #keepgrinding #getit #blah #icute #summertime
 '''