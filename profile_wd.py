import time

PS2 = "protocol@watch_dog~#: "
s1 = "\033[34m{}".format("┌──")
s2 = "\033[32m{}".format("protocol")
s3 = "\033[34m{}".format("@")
s4 = "\033[31m{}".format("watch_dog")
s5 = "\033[34m{}".format("~")
s6 = "\033[32m{}".format(":")
s7 = "\n"
s8 = "\033[34m{}".format("└╼")
s9 = "\033[31m{}".format("#")
s10 = "\033[37m{}".format(" ")
PS1=s1+s2+s3+s4+s5+s6+s7+s8+s9+s10

def hello_user():
	amblema=""
	print("\033[32m{}".format("protocol_v1 build 2")+"\033[34m{}".format(":")+" "+"\033[37m{}".format("Mobile version")+"\n")
	#print("\033[47m{}".format(" "))
	with open("wd_asci.py", "r") as fd:
		amblema = fd.read()
	
	
	i = 0
	for e in amblema:
		if e == "@":
			print("\033[37m{}".format("\033[40m{}".format(e)), end="")
			print("\033[0m{}".format(""), end="")
		else:
			print("\033[30m{}".format("\033[47m{}".format(e)), end="")
			print("\033[0m{}".format(""), end="")
			
		if i == 54:
			time.sleep(0.05)
			i=0
		
		i = i+1
		
	
	print("\033[0m{}".format(" "))
