def input_correction(s):
	ru = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.:?!;%()-+[]{}|@ "
	s2 = ""
	for e in s:
		for ru_e in ru:
			if e == ru_e:
				s2 += ru_e
	
	return s2
