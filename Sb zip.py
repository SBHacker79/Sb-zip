#!/use/bin/evn python
# https://github.com/SBHacker79/zip-password-cracker.git
# SB hacker

from zipfile import ZipFile
import sys
import os

argv=False
try:
	if (sys.argv[1]=="-version" or sys.argv[1]=="--version"):
		print("ZipKrack - version 1.0")
		argv=True
	else:
		pass
except:
	pass

def print_help():
	print("""
	
     zipfile          :   Specify the zip file.
     password list    :   Specify the password list.
     help             :   Show help.
     quit             :   Exit from the tool.
     --version        :   Display the version of ZipKrack.
     --help           :   Show help.
	""")


try:
	if (sys.argv[1]=="-help" or sys.argv[1]=="--help"):
		print_help()
		argv=True
	else:
		pass
except:
	pass

if (argv==True):
	sys.exit()
else:
	pass

os.system("clear")

print("""\033[1;96m 
                                        
 @@@@@@   @@@@@@@      @@@@@@@@  @@@  @@@@@@@   
@@@@@@@   @@@@@@@@     @@@@@@@@  @@@  @@@@@@@@  
!@@       @@!  @@@          @@!  @@!  @@!  @@@  
!@!       !@   @!@         !@!   !@!  !@!  @!@  
!!@@!!    @!@!@!@         @!!    !!@  @!@@!@!   
 !!@!!!   !!!@!!!!       !!!     !!!  !!@!!!    
     !:!  !!:  !!!      !!:      !!:  !!:       
    !:!   :!:  !:!     :!:       :!:  :!:       
:::: ::    :: ::::      :: ::::   ::   ::       
:: : :    :: : ::      : :: : :  :     :        
                                                
                                       Cyber SB hacker
\033[0;0m""")

while(True):
	try:
		exit=False
		print("\033[1;94m")
		action=input("\n {1} Zip file > ")
		if(action=="quit"):
			exit=True
			break
		elif(action=="help"):
			print_help()
		else:
			pass
		try:
			zip=ZipFile(action,"r")
			break
		except:
			if(action=="" or action=="help"):
				pass
			else:
				print("\n\033[0;91m[!] Unable to locate the zip file!\033[0;0m")
	except:
		pass


if (exit==True):
	sys.exit()
else:
	pass

list=input("\n {2} Password list > ")

print("\033[1;92m")

print(" {+} Password Attack")
try:
	word=open(list,"rb")
	count=open(list,"r")
except:
	print("\n\033[0;94m[!] Unable to locate the password list!\033[0;0m")
	sys.exit()

print("\n")
line=count.readline()
condition=0
while(line):
	password=word.readline()
	try:
		zip.extractall(path="Extract",pwd=password.strip())
		print("\033[1;91m")
		print("\n[Successful Password Hack!] :: {}".format(password.decode()))
		condition+=1
		break
	except:
		print(password.decode())
	line=count.readline()
	
if(condition==0):
	print("\n[Password not found!]")
else:
	pass

zip.close()
word.close()
count.close()