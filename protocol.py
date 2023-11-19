from fuzzywuzzy import fuzz
import os

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


while(True):
    error = 1

    text = input("protocol@watch_dog~#: ")

    if text in "help":
        print("quit - выход")
        print("add code <code number_code> - текущий код задачи.")
        print("ls code - показать список активных задач.")
        error = 0

    if text in "quit":
        break

    if text.find(code) >= 0:
        text = text[5:]
        code_text_list = get_text("code_text.txt").split(",")
        for code_text in code_text_list:
            code_num = code_text[0:3]
            code_num2 = text[0:3]

            if(code_num == code_num2):
                print(code_text)
        error = 0

    if text.find("add code") >= 0: 
        text = text.replace("add code", "") 
        set_text("code_text.txt", text[1:]) 
        print("code added complite!") 
        error = 0 
    if text in "ls code": 
        code_list = get_text("code_text.txt").split(",") 
        print(code_list)
        error = 0

    if error == 1:
        print("comman not found!")