def print_art(art):	
	line = ""
	for s_arr in art:
		for s in s_arr:
			line += s
	print("\n")
	print(line)






error_art = [["\033[31m{}".format("###### ###### ###### ###### ######"), "\n"],
	     ["\033[31m{}".format("##     ##  ## ##  ## ##  ## ##  ##"), "\n"],
	     ["\033[31m{}".format("###### #####  #####  ##  ## ##### "), "\n"],
	     ["\033[31m{}".format("##     ##  ## ##  ## ##  ## ##  ##"), "\n"],
	     ["\033[31m{}".format("###### ##  ## ##  ## ###### ##  ##"), "\n"]]
	     
	     
 
error_404 =[["\033[33m{}".format("##  ## ###### ##  ##"), "\n"],
	    ["\033[33m{}".format("##  ## ##  ## ##  ##"), "\n"],
	    ["\033[33m{}".format("###### ##  ## ######"), "\n"],
	    ["\033[33m{}".format("    ## ##  ##     ##"), "\n"],
	    ["\033[33m{}".format("    ## ######     ##"), "\n"]]
 
def print_code_art(code_dict):

	number = code_dict.get("number")
	reward = code_dict.get("reward")
	details = code_dict.get("details")
	
	code_art = [["\033[31m{}".format("###### ######     ## ######	"), "\033[37m{}".format(number), "\n"],
 	    ["\033[31m{}".format("##     ##  ##     ## ##	"), "\n"],		
 	    ["\033[31m{}".format("##     ##  ## ###### #####	"), "\033[34m{}".format("Награда:"), "\n"],
 	    ["\033[31m{}".format("##     ##  ## ##  ## ##		"), "\033[37m{}".format(reward), "\n"],
 	    ["\033[31m{}".format("###### ###### ###### ######   "), "\n"],
 	    ["\033[34m{}".format("Детали:"), "\n"],
 	    ["	", "\033[37m{}".format(details), "\n"]]
	
	print_art(code_art)
 			

def print_error_art(code_num):
	print_art(error_art)
	
	if(code_num == 404):
		print_art(error_404)
		
