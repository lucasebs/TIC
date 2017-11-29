
def Print_entropy(sorted_word_count_information, entropy):
	print "Word \t\t Count \t Self Information"
	for ii in sorted_word_count_information:
		# Very inelegant way of formatting
		separation = '\t\t' if len(ii[0]) < 7 else '\t'
		if len(ii[0]) >= 15: separation = '' 
		print("%s %s %s \t %s"%(ii[0], separation, str(ii[1]), str(ii[2])))
		
	print "\n\nEntropy of complete text: {}".format(entropy)
