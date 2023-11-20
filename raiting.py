import profile_wd
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

  arr_newbie = [newbie, 1, 201, 401, 601, 801, 1000]
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
  
  
def help():
  print("status       - текущий ранг\n" +
        "del <points> - удалить указанное кол-во очков\n" +
        "add <points> - добавить указанное кол-во очков\n"+
        "default rank - вернуться к началу\n")


def raiting_shell(enter):
		if enter == "help": help()
		if enter == "default": default_rank()
		if enter[0] == "a": write_rank(int(enter.split(" ")[1]) + read_rank())
		if enter[0] == "d" and len(enter.split(" ")[0]) == 3: del_rank(int(enter.split(" ")[1]))
		if enter == "status": print(is_rank_text(read_rank()))
		if enter.isdigit(): 
		  is_rank_text(enter)
		  write_rank(enter)
