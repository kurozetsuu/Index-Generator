import time
import os
B  = '\033[1;34m'
W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray

os.system("clear")
banner = '''
	     __________________________________________________
	    |                                                  |
	    |                  Index-Generator                 |
	    |                 By : Ayoub Ourass                |
	    |     https://www.facebook.com/ayoub.flack.90      |
	    |__________________________________________________|  
	   '''
print(banner)
print("[1] Start")
print("[2] Exit ")
option = input(B+"Index-Generator : ")
if option==1:
	title      = raw_input(G+"Enter Your Index Title           : ")
	page_color = raw_input(G+"Enter Your Page Color            : ")
	page_body  = raw_input(G+"Enter Your Body Text             : ")
	Text_color = raw_input(G+"Enter Your Text Color            : ")
	Text_size  = raw_input(G+"Enter Your Text Size (px)        : ")
	Image      = raw_input(G+"Insert A Picture (Image Source)  : ")
	pic_size   = raw_input(G+"Enter Your Picture Size (px)     : ")
	otext      = raw_input(G+"Another Text ? (Optional)        : ")
	Music      = raw_input(G+"Music                            : ")
	finalindex = raw_input(G+"Output Name                      : ")
	x = '"'
	print("Wait While Making Your Index ....")
	time.sleep(2)
	lindex = (finalindex+".html")
	Music = Music.replace("youtube","youtuberepeater")
	
	makeindex = open(lindex, "w")
	pageindex = pageindex = '<html> <head><title>'+title+'</title></head><body bgcolor='+x+page_color+x+'><center><br><div><font color='+x+Text_color+x+" "+'size='+x+Text_size+x+" "+ 'style="font-family: courier;">'+page_body+'</div></center></style></font>'+'<center><br><img src='+x+Image+x+" "+' size='+x+pic_size+x+' >'+'<center><br><div><font color='+x+Text_color+x+" "+'size='+x+Text_size+x+" "+ 'style="font-family: courier;">'+otext+'</div></center></style></font><iframe width="0" height="0" src="'+Music+x+' frameborder="0" allowfullscreen></iframe>'

	makeindex.write(pageindex)
	makeindex.close()

	print("Your Index Was Successfully Saved ! ")
	print(B+"Thanks For Using Our Script :)")
if option == 2:
	os.system("exit")
