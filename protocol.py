#from fuzzywuzzy import fuzz
import os
import profile_wd
import raiting

profile_wd.hello_user()

PS1 = profile_wd.PS1

code = ""
code_text = ""

def get_text(name_file):
    text = ""
    if os.path.exists(name_file):
        with open(name_file, 'r') as fp:
            text  = fp.read()

    return text

def set_text(name_file, text):
    text2 = None
    if os.path.exists(name_file):
        text2 = get_text(name_file)
        text = text2+","+text

    with open(name_file, 'w+') as fp:
        fp.writelines(text)


def remove_text(name_file):
    os.remove(name_file)


def help():
	print("\n")
	print("quit 			   - выход.")
	print("add code <code number_code> - текущий код задачи.")
	print("ls code 			   - показать список активных задач.")
	print("del <code_number> 	   - вводите номер кода и тот будет удален.")

def code_view(text):
	text = text[5:]
	code_text_list = get_text("code_text.txt").split(",")
	for code_text in code_text_list:
		code_num = code_text[0:3]
		code_num2 = text[0:3]

		if(code_num == code_num2):
			print(code_text)

def add_code(text):
	text = text.replace("add code", "") 
	set_text("code_text.txt", text[1:]) 
	print("code added complite!")


def ls(text):
	if(text == "code"):
		code_list = get_text("code_text.txt").split(",") 
		print(code_list)

def del_code(text):
	new_text = ""

	text = text[4:]
	code_text_list = get_text("code_text.txt").split(",")
	for code_text in code_text_list:
		code_num = code_text[:3]
		code_num2 = text[:3]
		if(code_num == code_num2):
			print("Done!")
		else:
			new_text = new_text+","+code_text
	new_text = new_text[1:]
	remove_text("code_text.txt")
	set_text("code_text.txt", new_text)
	

while(True):
	error = 1

	text = input(PS1)

	if text in "help":
		help()
		error = 0

	if text == "quit":
		break

	if text.find(code) >= 0:
		code_view(text)
		error = 0

	if text.find("add code") >= 0: 
		add_code(text) 
		error = 0 
        
	if len(text) >= 2:
		if text[:2] == "ls":
			ls(text[3:])
		error = 0
	
	if len(text) >= 3: 
		if text[:3] == "del":
			del_code(text)
			
	raiting.raiting_shell(text)

	if error == 1:
		print("comman not found!")
