var_encoding_type = "utf-8"
#Что сюда нужно добавить?
#- Чтобы сообщение приходило конкретному адресату для этого нужен отдельный чат.
#- Чаты должны быть: чат с GPT, чат с конкретным клиентм и общий чат.
#- Добавить возможность получения динамического адреса через паст бин, как в MyRAT.

# Хочу сделать фильтр для каждого потока конкретного клиента подключенного к серверу. Это может пригодиться для использования комманд чата, например Help или <задать вопрос gpt4> и ответ будет приходить на имя конкретного пользователя, а не для всех - чтобы чат не засорять.





import socket, threading, string, os #Libraries import
import api_gpt
import keyboard


# Порты ниже 1024 использовать можно только из под рута!
host = '127.0.0.1' #LocalHost
port = 1123 #Choosing unreserved port
reserv_port = 1124
var_prompt = (	"\n"+
		"\033[33m{}".format("HELP LIST:")+"\033[0m{}".format("")+"\n"+
		"-------------------------------------------------------"+"\n"+
		"@help                       - Команда сервера которая видна только отправителю.\n"+
		"@имя_пользователя сообщение - отправить сообщение конкретному пользователю.\n"+
		"                              Остальные участники не увидят этого сообщения.\n"+
		"@user_list                  - запросить список пользоателей.\n"+
		"                              Команда как и чат не рабоатет, пока что :(\n"+
		"-------------------------------------------------------"+
		"\n")




print("[Настройка сервера!]")
print("Запустите команду: ngrok tcp "+str(port))
os.system("gnome-terminal -- ngrok tcp "+str(port))
os.system("gnome-terminal -- /home/manuq4979/Documents/GPT/bin/chat")
print("Выделите похожу строку: 0.tcp.eu.ngrok.io:18579 и скопируйте в поле ввода..\n")
forwarding_link = input("forwarding: ")
print("Перейдите по ссылке: https://github.com/manuq4979/protocol_wd/blob/main/host_port и вставьте в файл этот текст: "+forwarding_link)
answ = input("Сделано? : ")
print("Теперь можно запускать приложение.")
print("[Настройка завершена!]\n")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket initialization
try:
	server.bind((host, port)) #binding host and port to socket
except OSError:
	server.bind((host, port))
server.listen()

clients = {}
nicknames = []

# Реализация метода для отправки сообщений для всех.
def broadcast(message): #broadcast function declaration
	for client in clients.values():
		client.send(message)

# Вернет только буквы и символы, без знаков припинания и @.
def extract_name_or_command(message):
	table = str.maketrans("", "", string.punctuation)
	name_or_cammand = message.translate(table)
	return name_or_cammand

def commands_for_server(command, sender_name, question="None"):
	global var_prompt
	if command == "gpt":
		question = question[1:]
		q = ""
		for m in question:
			q += m
		answer = api_gpt.get_answer_gpt(q)
		print("answer: "+answer.split("\n")[1])
		
		answer = ("\033[33m{}".format("HELP LIST:")+"\033[0m{}".format("")+"\n"+
		          "-------------------------------------------------------"+"\n"+
		          "\n[gpt4]: "+answer.split("\n")[1]+"\n"+
		          "-------------------------------------------------------"+"\n")
		
		personal(answer, sender_name)
		return True
	if command == "help":
		help_text = var_prompt
		personal(help_text, sender_name)
		return True
	if command == "user_list":
		user_list = clients().keys()
		user_list_text = ""
		for user_name in user_list:
			user_list_text.append("[INFO]: " + user_name + "\n")
		personal(user_list_text, sender_name)
		return True
	return False
	
def personal(message, name):
	try:
		client = clients[name]
		client.send(message.encode(var_encoding_type))
	except:
		print("KeyError"+" personal()")
		return "KeyError"
					

def get_current_nickname(client):
	global clients
	nickname = ""
	try:
		invert_clients = {v: k for k, v in clients.items()}
		nickname = invert_clients[client]
	except:
		print("KeyError"+" get_current_nickname()")
		return "KeyError"
	return nickname


# это реализация функций конкретного потока клиента.
def handle(client):
	while True:
		try: #recieving valid messages from client
			message = client.recv(1024)
			lines_array = message.decode(var_encoding_type).split()

			# IndexError будет если строка в массиве нет сообщение, например lines_array[1][0], это бывает когда пробел отправляешь, это коротко:
			# "nickname: text message" == ["nickname", "text message"]
			# "nickname: " == ["nickname"]
			if len(lines_array) > 1:	
				print(message.decode(var_encoding_type))
				
				if lines_array[1][0] == "@":
					message = ""
					ii = 1
					for i in range(len(lines_array)-1):
						message += lines_array[i+ii]
					
					print(lines_array)
					name_or_command = extract_name_or_command(lines_array[1])
					# Проверка на команду сервера, вдруг сообщение для сервера например help, gpt и т.п.
					# Если команда, то вернется True.
					nickname = get_current_nickname(client)
					flag = commands_for_server(name_or_command, nickname, question=lines_array[1:])
					# проверка сообщения, кому оно адресовано из пользователей - chat gpt или другой пользователь.
					# Если нет адресата то это всем будет отправлено кроме chat gpt. @nickname, @command - это имя, команда.
					if flag == False:
						name = name_or_command
						personal(message, name)
				else:	
					broadcast(message)
		except: #removing clients
			nickname = get_current_nickname(client)
			if nickname != "KeyError":
				clients.pop(nickname)
			broadcast('[INFO]: {} left!'.format(nickname).encode(var_encoding_type))
			print(nickname)
			nicknames.remove(nickname)
			client.close()
			break
		

# Этот метод лишь проверяет подключились ли новые клиенты или они отключились.
def receive(): #accepting multiple clients
	print("linux server: "+"\033[32m{}".format("started!"))
	print("\033[0m{}".format(""), end="")
	
	while True:
		broadcast(var_prompt.encode(var_encoding_type))
		client, address = server.accept()
		print("[BROADCAST]: Connected with {}".format(str(address)))
		client.send('NICKNAME'.encode(var_encoding_type))
		nickname = client.recv(1024).decode(var_encoding_type)
		nicknames.append(nickname)
		clients[nickname] = client
		print("[BROADCAST]: Nickname is {}".format(nickname))
		broadcast("[BROADCAST]: {} joined!".format(nickname).encode(var_encoding_type))
		#client.send('Server conneted'.encode(var_encoding_type))
		thread = threading.Thread(target=handle, args=(client,))
		thread.start()
		
		

receive()




