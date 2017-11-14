import string

def get_words(text):
	text = text.translate(string.maketrans("",""), string.punctuation)
	words = text.split()
	wordset = set(words)
	return (words, wordset)
	
