import time
import os
B  = '\033[1;34m'
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
option = input("Index-Generator : ")
if option==1:
	title      = raw_input("Enter Your Index Title           : ")
	page_color = raw_input("Enter Your Page Color            : ")
	page_body  = raw_input("Enter Your Body Text             : ")
	Text_color = raw_input("Enter Your Text Color            : ")
	Text_size  = raw_input("Enter Your Text Size (px)        : ")
	Image      = raw_input("Insert A Picture (Image Source)  : ")
	pic_size   = raw_input("Enter Your Picture Size (px)     : ")
	otext      = raw_input("Another Text ? (Optional)        : ")
	finalindex = raw_input("Output Name                      : ")
	x = '"'
	print("Wait While Making Your Index ....")
	time.sleep(2)
	lindex = (finalindex+".html")
	
	makeindex = open(lindex, "w")
	pageindex = '<html> <head><title>'+title+'</title></head><body bgcolor='+x+page_color+x+'><center><br><div><font color='+x+Text_color+x+" "+'size='+x+Text_size+x+" "+ 'style="font-family: courier;">'+page_body+'</div></center></style></font>'+'<center><br><br><br><img src='+x+Image+x+" "+' size='+x+pic_size+x+' >'+'<center><br><br><br><div><font color='+x+Text_color+x+" "+'size='+x+Text_size+x+" "+ 'style="font-family: courier;">'+otext+'</div></center></style></font>'


	makeindex.write(pageindex)
	makeindex.close()

	print("Your Index Was Successfully Saved ! ")
	print(B+"Thanks For Using Our Script :)")
if option == 2:
	os.system("exit")
