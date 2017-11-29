import string

def Get_words(text):
	# Remove punctuations and special caracters
	text = text.translate(string.maketrans("",""), string.punctuation)
	# Separate Words
	words = text.split()
	# Remove duplicated words with set()
	wordset = set(words)
	return words, wordset
	
