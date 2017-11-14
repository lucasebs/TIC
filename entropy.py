import io
import string
import urllib2
import numpy as np


text = "Texto./[ de de de qualquer  ^para conferencia de Entropia"
text = text.translate(string.maketrans("",""), string.punctuation)
words = text.split()
wordset = set(words)

freq={word: words.count(word) for word in wordset}

print "Word \t\t Count \t Self Information"
word_count_information = []
entropy = 0
for word in wordset:
    probability = freq[word] / float(1.0 * len(words)) 
    self_information = np.log2(1.0/probability) 
    entropy += (probability * self_information)
    word_count_information.append([word, freq[word], self_information])

sorted_word_count_information = list(sorted(word_count_information, key=lambda k:k[2], reverse=True))

for ii in sorted_word_count_information:
    # Very inelegant way of formatting
    separation = '\t\t' if len(ii[0]) < 7 else '\t'
    if len(ii[0]) >= 15: separation = '' 
    print("%s %s %s \t %s"%(ii[0], separation, str(ii[1]), str(ii[2])))
print "\n\nEntropy of complete text: {}".format(entropy)
