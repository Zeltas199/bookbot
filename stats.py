def get_num_words(file_contents):
        num_words = len(file_contents.split())
        return num_words

def sort_on(dict):
	return dict["num"]

def get_num_chars(file_contents):
	character_number = {}
	lowered_contents = file_contents.lower()
	for chars in lowered_contents:
		if(chars not in character_number):
			character_number[chars]=1
		else:
			character_number[chars] += 1
	return character_number

def get_list_of_chars(character_number):
	key_and_value = {}
	new_list = []
	for character in character_number:
		key_and_value = {"char": character, "num": character_number[character]}
		new_list.append(key_and_value)
	new_list.sort(reverse=True, key=sort_on)	
	return new_list
