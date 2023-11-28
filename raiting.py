import profile_wd
import traceback
import os

PS1 = profile_wd.PS1

def is_rank_text(enter):
  enter = int(enter)
  print(enter)

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
        print("Текущий ранг: "+arr_newbie[0]+" "+dict_numbers[4])
        return
  if(enter == 2000):
        print("Текущий ранг: "+arr_veteran[0]+" "+dict_numbers[4])
        return
  if(enter == 3000):
        print("Текущий ранг: "+arr_elite[0]+" "+dict_numbers[4])
        return
  if(enter == 4500):
        print("Текущий ранг: "+arr_professional[0]+" "+dict_numbers[4])
        return
  if(enter == 6500):
        print("Текущий ранг: "+arr_master[0]+" "+dict_numbers[4])
        return
  if(enter == 8000):
        print("Текущий ранг: "+arr_grant_master[0]+" "+dict_numbers[4])
        return
      
  for arr_rank in array_ranks:
    for lvl in range(5):
        if enter in range(arr_rank[lvl+1], arr_rank[lvl+2]):
        
          rank_lvl = lvl+1
          rank_lvl = dict_numbers[rank_lvl-1]
          
          
          print("Текущий ранг: "+arr_rank[0]+" "+rank_lvl)
          return

def create_point_file():
  file = open("otus.txt", "w+")
  file.write("1")
  return file

def read_rank():
  file = None
  try:
    file = open("otus.txt", "r")
  except FileNotFoundError:
    file = create_point_file()
  points = file.read()
  if(points == ""):
    points = 1
  points = int(points)
  file.close()
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
  default_rank()
  write_rank(points-points_for_del)



def read_history_points():
    text = ""
    if os.path.exists("history_points.txt"):
        with open("history_points.txt", 'r') as fp:
            text  = fp.read()

    return text

def add_history_point(text):
    text2 = None
    if os.path.exists("history_points.txt"):
        text2 = read_history_points()
        text = text2+"_"+text

    with open("history_points.txt", 'w+') as fp:
        fp.writelines(text)


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
  print("status                       - текущий ранг.\n" +
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
			point = int(enter.split(" ")[1])
			description = input("За какие заслуги? : ")
			text = str(point)+" - "+description
			add_history_point(text)
			
			write_rank(point + read_rank())
			command_start = True
			
		try:
			if len(enter) >= 3: 
				if enter[:6] == "del -p": 
					del_rank(int(enter.split(" ")[2]))
					command_start = True
		except ValueError as e:
			print("\033[31m{}".format("ERROR:\n")+"\033[37m{}".format(traceback.format_exc())+"\nЕсли коротко, то команда была написана неверно!")
			
		if enter == "status":
			print(is_rank_text(read_rank()))
			command_start = True
		
		if enter == "history points" or enter == "ls -hp":
			print_history_points()
			command_start = True
			
		if enter == "del -hp":
			del_history()
			command_start = True
			
			
		if enter.isdigit(): 
		  is_rank_text(enter)
		  write_rank(enter)
		  command_start = True
		  
		return command_start
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
