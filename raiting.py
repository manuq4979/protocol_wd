import profile_wd
import traceback
import os
import RANK_ART.rank_arts

PS1 = profile_wd.PS1

def is_rank_text(enter):
	enter = int(enter)

	newbie = "Новичок"
	veteran = "Ветеран"
	elite = "Элита"
	professional = "Профессионал"
	master = "Мастер"
	grant_master = "Грант-мастер"
	ligend = "Легенда"

	arr_newbie = [newbie, 0, 201, 401, 601, 801, 1000]
	arr_veteran = [veteran, 1001, 1201, 1401, 1601, 1801, 2000]
	arr_elite = [elite, 2001, 2201, 2401, 2601, 2801, 3000]
	arr_professional = [professional, 3001, 3301, 3601, 3901, 4201, 4500]
	arr_master = [master, 4501, 4901, 5301, 5701, 6101, 6500]
	arr_grant_master = [grant_master, 6501, 6801, 7101, 7401, 7701, 8000]
	arr_ligend = [ligend, 8001, 0, 0, 0, 0, 8002]

	array_ranks = [arr_newbie, arr_veteran, arr_elite, arr_professional, arr_master, arr_grant_master, arr_ligend]

	dict_numbers = ["I", "II", "III", "IV", "V"]

	is_rank = newbie
	rank_lvl = 1
	points = 0


	points = read_rank()
	points = enter + points

      
	if(enter == 1000):
		# print("Текущий ранг: "+arr_newbie[0]+" "+dict_numbers[4])
		var_next_position_rank = 1201
		return [arr_newbie[0], dict_numbers[4], var_next_position_rank]
	if(enter == 2000):
		var_next_position_rank = 2201
		return [arr_veteran[0], dict_numbers[4], var_next_position_rank]
	if(enter == 3000):
		var_next_position_rank = 3301
		return [arr_elite[0], dict_numbers[4], var_next_position_rank]
	if(enter == 4500):
	  	var_next_position_rank = 4901; return [arr_professional[0], dict_numbers[4], var_next_position_rank]
	if(enter == 6500):
		var_next_position_rank = 6801
		return [arr_master[0], dict_numbers[4], var_next_position_rank]
	if(enter == 8000):
		var_next_position_rank = 10000
		return [arr_grant_master[0], dict_numbers[4], var_next_position_rank]
        
  
	for arr_rank in array_ranks:
		for lvl in range(5):
			if enter in range(arr_rank[lvl+1], arr_rank[lvl+2]):
			
				rank_lvl = lvl+1
				rank_lvl = dict_numbers[rank_lvl-1]
				var_start_position_interval_rank = arr_rank[lvl+1]
				var_next_position_rank = arr_rank[lvl+2]
				return [arr_rank[0], rank_lvl, var_next_position_rank, var_start_position_interval_rank]
          

def create_point_file():
	file = open("otus.txt", "w+", encoding='utf-8')
	file.write("1")
	return file

def read_rank():
	file = None
	try:
		file = open("otus.txt", "r", encoding='utf-8')
	except FileNotFoundError:
		file = create_point_file()
	points = file.read()
	file.close()
  
	if(points == ""):
		# points = 1 equal points = ""
		return 1
    
	return int(points)

def write_rank(points):
	file = None
	try:
		file = open("otus.txt", "w")
	except FileNotFoundError:
		file = create_point_file()
	points = str(points)
	file.write(points)
	file.close()

def default_rank():
	write_rank(1)
  
def del_rank(points_for_del):
	points = read_rank()
	if points_for_del <= points:
		default_rank()
		write_rank(points-points_for_del)
		print("\033[32m{}".format("delite complite!"))
	if points_for_del > points:
		print("\033[31m{}".format("ERROR: ")+"\033[0m{}".format("Вы хотите удалить больше чем у Вас есть!"))



def read_history_points():
	text = ""
	if os.path.exists("history_points.txt"):
		with open("history_points.txt", 'r', encoding='utf-8') as fp:
			text  = fp.read()

	return text

def add_history_point(text):
	text2 = None
	
	try:
		with open("history_points.txt", 'w+', encoding='utf-8') as fp:
			fp.write(text)
	except UnicodeEncodeError:
		print("\033[31m{}".format("ERROR: ") + "\033[0m{}".format("Увы данные не были записаны! Снова ошибка utf-8!"))
		return 1
	
	if os.path.exists("history_points.txt"):
		text2 = read_history_points()
		text = text2+"_"+text


def del_history():
	with open("history_points.txt", "w"):
		pass
	print("\033[32m{}".format("delite complite!"))
	

def print_history_points():
	list_empty = True
	history_list = read_history_points().split("_")
	for e in history_list:
		if len(e) > 0:
			print(e)
			list_empty = False
	if list_empty == True:
		print("\033[33m{}".format("WARNING: ")+"\033[37m{}".format("Ещё не было созданно истории очков! (См. history_points.txt)"))	


  
def help():
	print(  "status                       - текущий ранг.\n" +
	        "del -p <points>              - удалить указанное кол-во очков.\n" +
		"del -hp                      - удаляет всю историю пополнения очков.\n" +
		"add <points>                 - добавить указанное кол-во очков.\n" +
		"default rank                 - вернуться к началу.\n" +
		"history points (или ls -hp)  - вернет историю пополнения очков.\n")


def raiting_shell(enter, command_start):
	command_start = command_start
		
	if enter == "help": 
		help()
		command_start = True
			
	if enter == "default": 
		default_rank()
		command_start = True
			
	if enter[0] == "a" and command_start == False:
		point = enter.split(" ")[1]
			
		if point.isdigit():
			point = int(point)
			description = input("За какие заслуги? : ")
			text = str(point)+" - "+description
			add_history_point(text)
				
			point = point + read_rank()
			write_rank(point)
			print("\033[32m{}".format("Done!"))
			command_start = True
			
		try:
			if len(enter) >= 3: 
				if enter[:6] == "del -p": 
					del_rank(int(enter.split(" ")[2]))
					command_start = True
		except ValueError as e:
			print("\033[31m{}".format("ERROR:\n")+"\033[37m{}".format(traceback.format_exc())+"\nЕсли коротко, то команда была написана неверно!")
			
	if enter == "status":
		rank_int = read_rank()
		rank_array = is_rank_text(rank_int)
		my_rank_point = rank_int
		rank_array.append(my_rank_point)
			
		RANK_ART.rank_arts.print_rank_art(rank_array)
			
		command_start = True
		
	if enter == "history points" or enter == "ls -hp":
		print_history_points()
		command_start = True
	
	
	if enter[:3] == "del":
		
		if enter[3:7].replace(' ', '') == "-hp":
			del_history()
		
		if enter[3:6].replace(' ', '') == "-p":
			point_for_del = int(enter[7:])
			history = input("Какова причина: ")
			add_history_point(history)
			del_rank(point_for_del)
		command_start = True
	
	
			
	# if enter.isdigit(): 
	#	is_rank_text(enter)
	# 	write_rank(enter)
	# 	command_start = True
		  
	return command_start
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
