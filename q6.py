review = ''	
unigram_list = []
bigram_list = []

with open("cleaned_data.txt", "r") as fin:
	review = ''		
	for line in fin:
		review += line[1:].rstrip()	

ug = set(review.split())
for key in ug:
	if review.count(key) > 1:
		unigram_list.append(key)

input_list = review.split()
for i in range(len(input_list)-1):
    bigram_list.append((input_list[i], input_list[i+1]))

bg = set(bigram_list)
bigram_list = []
for key in bg:
	substr = str(key[0])+" "+str(key[1])
	if review.count(substr) > 1:
		bigram_list.append(substr)

unigram_list.sort()
bigram_list.sort()
with open("vocab-unigram.txt", "w") as fd:
	for i in unigram_list:
		fd.write(str(i))
		fd.write("\n")

with open("vocab-bigram.txt", "w") as fd:
	for i in bigram_list:
		fd.write(i)
		fd.write("\n")
