import time


PS5 = "\033[34m{}".format('┌──') + "\033[32m{}".format('connected')+"\033[34m{}".format('@')+"\033[31m{}".format('message')+"\033[34m{}".format('>>\n')+"\033[34m{}".format('└╼ ')+"\033[0m{}".format('')

def hello_user():
	print("mobile client: "+"\033[32m{}".format("started!"))
	print("\033[0m{}".format(""), end="")
	
	with open("./chat/art_gpt.py", "r") as fd:
		amblema = fd.read()
	amblema = amblema.split("\n")
	
	i = 0
	for e in amblema:
		if e != " ":
			print("\033[37m{}".format("\033[42m{}".format(e)))
			print("\033[0m{}".format(""), end="")
		else:
			print("\033[30m{}".format("\033[42m{}".format(e)), end)
			print("\033[0m{}".format(""), end="")
			
		if i == 1:
			time.sleep(0.05)
			i=0
		
		i = i+1
		
	
	print("\033[0m{}".format(" "))
	
