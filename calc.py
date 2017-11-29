import numpy as np
from text import Get_words 
from print_entropy import Print_entropy 

text = raw_input("Texto qualquer para conferencia de Entropia: ")
words, wordset = Get_words(text)

freq={word: words.count(word) for word in wordset}

word_count_information = []
entropy = 0
for word in wordset:
    probability = freq[word] / float(1.0 * len(words)) 
    self_information = np.log2(1.0/probability) 
    entropy += (probability * self_information)
    word_count_information.append([word, freq[word], self_information])

sorted_word_count_information = list(sorted(word_count_information, key=lambda k:k[2], reverse=True))

Print_entropy(sorted_word_count_information, entropy)
