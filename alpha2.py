from instapy import InstaPy
from instapy import set_workspace
import time
import instaMail
from selenium.common.exceptions import NoSuchElementException
from tempfile import gettempdir
import os


if os.name == 'nt':
    logintext = "C:\\Users\\eddyizm\\Desktop\\Work\\login.txt"
    set_workspace(path="C:\\Users\\eddyizm\\Source\\Repos\\InstaPy\\")
else:
    logintext = "/Users/eduardocervantes/Desktop/Macbook/login.txt"
    set_workspace(path="/Users/eduardocervantes/Downloads/Repo/InstaPy/")

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
        session.like_by_tags(['autumnpalette', 'sensuality_bnw', 'shanghai'], amount=50 )
        print('alpha2 success')  
        instaMail.completeTask('alpha2 success')
    except Exception as exc:
        print('alpha2 fail!')       
        print("error: {0}".format(exc))
        instaMail.completeTask('alpha2 fail')
        
        
    finally:
        # end the bot session
        session.end()
       
alpha()

'''
#tacomaworld # #yotamafia #yota #explore #pnw #outdoors #getoutside  
#themysterypr0ject #project_soul 
#___bodylanguage___ #__bodyart__ #topview #still_view #humanedge #colors #soulmate #soulart #darkbeauty
# #tacomabeast #scs
# #mylife #nature #exploring 
#lypsing #like #likeforlike #floodlike #views #viewer #view #musicallyview # #tiktok #likeapps #transition #followers #followme #hitlike #bitlike #transition #lypsing'
#ilmiocuoresoloperte #noidue #noi #instagramstories #instagramood #instagram'
#swimming  #grancenote  #tulum  #tb #traveling #travel # #cave #cenote #beautiful #water #motivacnystatusalways'
#IBTMscout #WLYG #imgirls #numa #wescoutusa #m4scouting #LA #manager #model #fashion #filmmaker #cast #director 
#italy#acting #shortfilm  #bloger #beauty #makeup #magazine #trends #clothes #paris'
#vilnius #guangzhoutower #guangzhoucity #thehide # #shenzhen #milan #dubai #jeddah #foodporn #like4like 
#vilniusoldtown #odessa #hangzhou #foshan #dongguan #panyu #guangzhoufood #brasilianmodel 
#lawofattraction #spiritualjourney #faith # # #consciousness #spirituality #spiritualgangster #freethinking #quoteoftheday #positivevibes #positivethinking #presentmoment 
#love #success #loa #thesecret #spiritual 
#sannyday#summer#summer2017#see#beach#batumi#batumi2017#batumicity#batumibeach#georgiagirl###followme#follow#followers#weekend#face'
 b'#uncoveredmagazine #sensual_dreams #boudoirphotography # # #infinity_sense #sensualart_flair 
#igf_sensual2 #lamalaeducacion #digers_body #shotsosensual #seduction_sensuality #be_one_sensual #my_secret_lover_ #great_captures_sensual #beautyandboudoir #best_expression_sensuality 
#loves_sensual_mood #pizza #insta_legs_2015 #hot #fitbody #fitlove'   
'#haryanvi #haryanvistatus #haryanvi #haryanviculture # #models #modelling # #model # # #italy 
#haryanvi #mood # #manjul #handsome #handsomehunk #tag  #cool #dashing #supermodel #actor #indianmodel #indianmodels #indianfollowers
#ddlg #gls #tattoos #alternative #toes #feet # #outdoorshoot  #bathtime #fitfam #pinup #freckles #fashionmodel  #pinkhair  
##alt #longlegs #art #travelingmodel
#throwrug #knit #softfurnishings #clay #knitthrow #interior #styling #decorating #interiorsdecorating #interiorstyling #sofa #bed #bambury 
# #designhouseinteriors #throwrugs # # #trendcolours
#46r #localadk # #sheadventures #hiking # #mtnmoment  #FunIsTheBest # # #choosemountainswomen 
#forceofnature #GOATworthy # #rei1440project #
#instadaily #featuremeseas #featuremeof #hinfluencercollective 
#femmetravel #featuremeof #l0tsabraids 
#seamyphotos #bravogreatphoto 
#wtnadventures #l0tsabraids #ftwotww #expofilm #ftmedd # 
#portraits_universe #gramkilla
#myerasmus #dji #engineer #erasmus 
#dbtravel #turkmen #blagoevgrad #aubg #campus #2018 #senior #collegelife

#kilonewton #textiles #artmatsdm #charecterdesign
#teamcanon #folkgood #dreaming 
#ingrande_crew #calabria #loves_united_calabria #loves_united_italia #volgocalabria 
#volgoitalia #ig_italia #calabriadaamare #vivocalabria #like4follow 
#verso_sud #yallerscalabria #follow4follow #yallersitalia #italia_inunoscatto #likeforlike
#ig_calabria #ig_crotone #igreggiocalabria #instanlikes #igcosenzan
#landscape_captures #followback # #topfrancephoto 
#ig_worldclub #followme #super_europe 
#follow4follow #worldtravelpics
#igphoto #ig_captures #igs_photos #ig_daily #worldbestgram
#snapback #pushthroughit #igotthis 
#almostthere #fit# #tone 
#tanlines #cutoffs #farm
#longhair #passion  #bodypositivity #ass
'''