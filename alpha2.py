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
        session.like_by_tags(['tacomaoffroad', 'artnude', 'vietnam'], amount=50 )
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
#toyotatacoma #tacomaworld #yotamafia #yota #explore #pnw #pnwonderland #pnwcollective #outdoors #getoutside  
#themysterypr0ject #project_soul #portraitphotography 
#___bodylanguage___ #__bodyart__ # #topview #still_view #humanedge #colors #soulmate #soulart #darkbeauty
# # #hellatrails #tacomabeast #scs
#sundaymood #mylife #nature #exploring 
#lypsing #like #likeforlike #floodlike #views #viewer #view #musicallyview # #tiktok #likeapps #transition #followers #followme #hitlike #bitlike #transition #lypsing'
#ilmiocuoresoloperte #aroundtheworld   #noidue #noi #instagramstories #instagramood #instagram'
#swimming  #grancenote  #tulum  #tb #traveling # #travel #vacation # #cave #cenote #beautiful #water #motivacnystatusalways'
#IBTMscout # #WLYG #imgirls # #numa #wescoutusa #m4scouting #LA #manager #model #fashion #filmmaker #cast #director 
#italy#acting #shortfilm  #bloger #beauty #makeup #magazine #trends #clothes #paris'
#vilnius #guangzhoutower #guangzhoucity #thehide # # #shanghai #shenzhen #milan #dubai #jeddah # #foodporn #like4like # 
#vilniusoldtown # #odessa #hangzhou #foshan #dongguan #seoul # #panyu #guangzhoufood #brasilianmodel 
#lawofattraction #meditiation # #spiritualjourney #faith # #lightwarrior #consciousness #spirituality #spiritualgangster #freethinking #quoteoftheday #positivevibes #positivethinking #presentmoment 
# #love # # #higherconsciousness #success #  #loa #thesecret #spiritual 
#sannyday#summer#summer2017#see#beach#batumi#batumi2017#batumicity#batumibeach#georgia#georgiagirl##russiangirl#followme#follow#followers#weekend#face'
 b'#uncoveredmagazine # #sensual_dreams #boudoirphotography #sensuality_bnw #sensuality_world # #infinity_sense #sensualart_flair 
#igf_sensual2 #lamalaeducacion #digers_body #shotsosensual #seduction_sensuality #be_one_sensual # #my_secret_lover_ #great_captures_sensual # #beautyandboudoir #best_expression_sensuality 
#loves_sensual_mood #pizza #insta_legs_2015  #hot #hotgirls  #fitbody #fitlove'   
'#haryanvi #haryanvistatus #haryanvi #haryanviculture #haryana #models #modelling #modellife #model #medellin #modello #italy 
#haryanvi #mood #modern # #manjul #handsome #handsomehunk #tag  #cool #dashing #supermodel #actor #  #indianmodel #indianmodels #indianfollowers
#ddlg #gls #tattoos #alternative #toes #feet #fetish #outdoorshoot  #bathtime #fitfam #pinup #freckles #fashionmodel  #pinkhair  
##alt #longlegs #art #travelingmodel
#throwrug #knit #softfurnishings #clay #knitthrow #interior #styling #decorating #interiorsdecorating #interiorstyling #sofa #bed #bambury 
# #designhouseinteriors #throwrugs #knitted # #autumnpalette #trendcolours
#46r #localadk # #sheadventures #hiking # #mtnmoment  #FunIsTheBest #outdoorwomen # #choosemountainswomen 
#forceofnature #GOATworthy #backcountry #rei1440project #mountainmoment
#instadaily #featuremeseas #featuremeof #hinfluencercollective 
#femmetravel #featuremeof #l0tsabraids 
#seamyphotos #bravogreatphoto 
#wtnadventures #l0tsabraids #ftwotww #expofilm #ftmedd #portraitsvisuals 
#portraits_universe #gramkilla #artofvisual
#myerasmus #dji #engineer #erasmus 
#dbtravel #turkmen #blagoevgrad #aubg #campus #2018 #senior #collegelife
#artnude # 
#kilonewton #textiles #artmatsdm #charecterdesign
# #teamcanon #folkgood #dreaming 
 #ingrande_crew #calabria #loves_united_calabria #loves_united_italia #volgocalabria 
 #volgoitalia #ig_italia #calabriadaamare #vivocalabria #like4follow 
 #verso_sud #yallerscalabria #follow4follow #yallersitalia #italia_inunoscatto #likeforlike
 #ig_calabria #ig_crotone #igreggiocalabria #instanlikes #igcosenzan
 #landscape_captures #followback # #topfrancephoto 
 #ig_worldclub # #followme #super_europe 
 # #follow4follow # #worldtravelpics
 #igphoto # #ig_captures #igs_photos #ig_daily #worldbestgram #
 #snapback #pushthroughit #igotthis 
 #almostthere # #fit # #fit#   #tone 
 #tanlines #cutoffs #countrylife #farm
 #  #sensual_art # #longhair #passion  #bodypositivity #ass
 '''