#from fuzzywuzzy import fuzz
import os
import profile_wd
import raiting
import arts_ascii
import json
import ast

profile_wd.hello_user()

PS1 = profile_wd.PS1

code = ""
code_text = ""

def get_text(name_file):
	text = ""
	if os.path.exists(name_file):
		with open(name_file, 'r', encoding='utf-8') as fp:
			text  = fp.read()

	return text

def set_text(name_file, text):
	text2 = None
	if os.path.exists(name_file):
		text2 = get_text(name_file)
		text = text2+"_"+text

	with open(name_file, 'w+', encoding='utf-8') as fp:
		fp.writelines(text)


def remove_text(name_file):
	os.remove(name_file)


def help():
	print("\n")
	print("quit                           - выход.")
	print("add code <code number_code>    - текущий код задачи.")
	print("ls code                        - показать список активных задач.")
	print("del -c <code_number>           - вводите номер кода и тот будет удален.")
	print("\n")

def code_view(number):
	code_text_list = get_text("code_text.txt").split(",")
	for code_dict in code_text_list:
		code_dict = json.loads(code_dict)
		code_num = code_dict["number"]
		code_num2 = int(number)

		if(code_num == code_num2):
			print(code_text)

def add_code(text):
	error = 0
	text = text.replace("add code", "")
	number = text[1:]
	
	if len(number) > 3:
		print("\033[31m{}".format("ERROR: ")+"\033[37m{}".format("Допустимая длина кода - от 1 до 3 включительно!"))
		error = 1
	if not number.isdigit():
		print("\033[31m{}".format("ERROR: ")+"\033[37m{}".format("Допускаются только цифры!"))
		error = 1
	if error == 0:
		reward = input("Укажите награду: ")
		if not reward.isdigit():
			print("\033[31m{}".format("ERROR: ")+"\033[37m{}".format("Допускаются только цифры!"))
			return
		details = input("Укажите подробности: ")
		d = {"number" : number, "reward" : reward, "details" : details}
		line = json.dumps(d)
		set_text("code_text.txt", line)
		print("\033[32m{}".format("code added complite!"))


def ls(text):
	if(text == "code"):
		list_empty = True
		codes_list = get_text("code_text.txt").split("_")
		for code_dict in codes_list:
			if len(code_dict) != 0:
				code_dict = json.loads(code_dict)
				arts_ascii.print_code_art(code_dict)
				list_empty = False
		
		if list_empty == True:
			print("\033[33m{}".format("WARNING: ")+"\033[37m{}".format("Ещё не было созданно кодов! (См. code_text.txt)"))	

def del_code(number):
	

	new_dict = ""

	code_text_list = get_text("code_text.txt").split("_")
	find_code = False
	for code_dict in code_text_list:
		if len(code_dict) != 0:
			code_dict = json.loads(code_dict)
			code_num = code_dict["number"]
			if(code_num == number[7:]):
				find_code = True
				
				status = input("Задание выполненно? : ")
				if status == "Да" or status == "да" or status == "Yes" or status == "yes":
					status = True
				if status == "Нет" or status == "нет" or status == "No" or status == "no":
					status = False
				if status == "Отмена" or status == "отмена" or status == "Cancel" or status == "cancel":
					status = -1
				
				print("\033[32m{}".format("Done!"))
				if status == -1:
					raiting.add_history_point(code_dict["reward"]+" - "+"Добавлен ошибочно или для теста!")
				if status == True:
					raiting.add_history_point(code_dict["reward"]+" - "+"Задание "+code_dict["number"]+" выполненно! : "+code_dict["details"])
					
					var_my_raiting = raiting.read_rank()

					var_my_raiting = var_my_raiting + int(code_dict["reward"])
					raiting.write_rank(var_my_raiting, status=True)
				if status == False:
					raiting.add_history_point(code_dict["reward"]+" - "+"Задание "+code_dict["number"]+" провалено! : "+code_dict["details"])
			else:
				new_dict = new_dict+"_"+json.dumps(code_dict)
	remove_text("code_text.txt")
	set_text("code_text.txt", new_dict)
	if find_code == False:
		print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("У Вас нечего удалять!"))
	

while(True):
	command_start = False

	text = input(PS1)
	
	# костыль, чтобы приложение от пустого ввода не ложилось!
	if text == "":
		text = "       "
		command_start = True

	if text in "help":
		help()
		command_start = True
	

	if text == "quit":
		break
	
	
	if text.find(text) >= 0 and text[0:3] == "code":
		code_view(text)
		command_start = True
	
	if text.find("add code") >= 0:
		add_code(text) 
		command_start = True
	
	if len(text) >= 2:
		if text[:2] == "ls":
			ls(text[3:])
			command_start = True
	
	if len(text) >= 3: 
		if text[:6] == "del -c":
			del_code(text)
			command_start = True
			
	command_start = raiting.raiting_shell(text, command_start)
	
	
	if command_start == False:
		#arts_ascii.print_error_art(404)
		print("\033[31m{}".format("ERROR: ")+"\033[37m{}".format("Команда отсутствует!"))


