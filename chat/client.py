var_encoding_type = "utf-8"


import socket, threading, json, time
from os import path
from requests import get
import re
import chat.welcome as welcome



path_profile_client = "profile_client.json"
host = '127.0.0.1'
port = 1124 #Choosing unreserved port
reserv_port = 1123
bufferSize = 1024*200
PS5 = welcome.PS5

receive_thread = None
write_thread = None
client = socket.socket()
quit = False

client_name = ""
nickname = ""


def get_address_server():
	global host, port
	forwarding_link = get("https://raw.githubusercontent.com/manuq4979/protocol_wd/main/host_port").text
	forwarding_link = forwarding_link.split(":")
	host = forwarding_link[0]
	port = int(forwarding_link[1])

def set_name_this_client(client_name):
	var_profile_dict = {'name': client_name}
	with open(path_profile_client, "w+") as f:
		if path.exists(path_profile_client) == False:
			var_profile_dict = get_profile_this_client()
			var_profile_dict["name"] = client_name
			json.dump(var_profile_dict, f)
			print(0)
		else:
			print(1)
			json.dump(var_profile_dict, f)

def get_profile_this_client():
	if path.exists(path_profile_client):
		with open(path_profile_client, "r") as f:
			var_profile_dict = json.load(f)
			return var_profile_dict
	else:
		return False

def input_nickname():
	global client_name, nickname
	client_name = get_profile_this_client()
	if client_name == False:
		nickname = input("\033[32m{}".format("Choose your ")+ "\033[34m{}".format("nickname")+"\033[0m{}".format(": "))
		set_name_this_client(nickname)
	else:
		nickname = client_name['name']
	
	
		


def connect_client():
	global client
	
	get_address_server()
	
	print("[INFO]: Подключение к серверу, подождите...")
	print("[INFO]: "+"host: "+str(host) + " port: "+str(port))
	print("[INFO]: если подключения нет больше 2-3 минут, значит сервер по указанному адресу не доступен!")
	
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket initialization
	try:
		try:
			client.connect((host, port)) #connecting client to server
		except ConnectionRefusedError:
			try:
				client.connect((host, reserv_port))
			except:
				print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("сервер не доступен."))
		except:
			print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("скорее всего неожиданно обрубился интернет, попробуйте позже, это сработает :)"))
	except TimeoutError:
		print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("время ожидания истекло, сервер не доступен."))

var_new_line = False
# Данные попадают в буфер и информация с сервера не мешает вводить пользователю сообщение и только после ввода, информация из чата будет видна.
buffer_messages = []
def receive():
	global quit
	
	i = 0
	while True: #making valid connection
		if quit == True:
			break
		try:
			message = client.recv(bufferSize).decode(var_encoding_type)
			if message == 'NICKNAME':
				client.send(nickname.encode(var_encoding_type))
			else:
				if i == 0:
					time.sleep(2)
					i = 1
				#print(message)
				buffer_messages.append(message)
				
		except: #case on wrong ip/port details
			print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("An error occured!"))
			try:
				client.send(("[BROADCAST]: "+client_name['name']+" left!").encode(var_encoding_type))
				client.close()
			except:
				print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("время ожидания сообщения истекло, сервер не доступен."))
			break
			
def is_command(message):
	message = message.split()
	if len(message) > 1:
		regex = "@"
		string = message[1]
		pattern = re.compile(regex)
		result = pattern.search(string) is not None
		if result == True:
			return  message[1]
		return result
	
def print_buffer_msg(message=False):
	print("[Список сообщений]:")
	if message != False:
		buffer_messages.append(message)
	for msg in buffer_messages:
		print(msg)
	
def write():
	global receive_thread, write_thread, quit
	i = 0
	while True: #message layout\
		if i == 0:
			time.sleep(2)
			print_buffer_msg()
			i = 1
		message = '{}: {}'.format(nickname, input(PS5))
		

		result = is_command(message)
		if result != False:
			if result == "@quit":
				#receive_thread.join()
				#write_thread.join()
				try:
					client.send(("[BROADCAST]: "+client_name['name']+" left!").encode(var_encoding_type))
				except BrokenPipeError:
					print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("cервер уже оборвал соединение."))
				client.close()
				time.sleep(2)
				quit = True
				break
		
		try:
			client.send(message.encode(var_encoding_type))
			print_buffer_msg(message=message)
		except BrokenPipeError:
			print("\033[31m{}".format("[ERROR]: ")+"\033[0m{}".format("cервер неожиданно оборвал соединение."))
			quit = True
			break
			

def start_client():
	global receive_thread, write_thread
	
	input_nickname()
	welcome.hello_user()
	
	connect_client()
	receive_thread = threading.Thread(target=receive) #receiving multiple messages
	receive_thread.start()
	#write_thread = threading.Thread(target=write) #sending messages
	#write_thread.start()
	write()


