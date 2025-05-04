from stats import get_num_words, get_num_chars, get_list_of_chars
import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	if  len(sys.argv) == 2:
		number_of_characters = get_num_chars(get_book_text(sys.argv[1]))
		list_of_chars = get_list_of_chars(number_of_characters)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}...")
		print("----------- Word Count ----------")
		print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
		print("--------- Character Count -------")
		for chars in get_list_of_chars(number_of_characters):
			if chars["char"].isalpha() == True:
				print(f"{chars["char"]}: {chars["num"]}")
		print("============= END ===============")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
main()
