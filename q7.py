import pickle
import math

def training(reviews, univocabulary, bivocabulary):
	N = len(reviews)
	N1 = 0
	N2 = 0
	
	pos = ''
	neg = ''

	for review in reviews:
		if review[0] == '+':
			N1 += 1
			pos += ' ' + review[1:] 
		else:
			N2 += 1
			neg += ' ' + review[1:]
	

	P1 = (1.0 * N1)/N
	P2 = (1.0 * N2)/N

	puProb = []
	nuProb = []
	pbProb = []	
	nbProb = []	
	pcount = []
	ncount = []
	
	totalCountInPositive = 0
	totalCountInNegative = 0

	for word in univocabulary:
		pcount.append(1)
		ncount.append(1)

		totalCountInPositive += pos.count(word) + 1
		totalCountInNegative += neg.count(word) + 1
	for word in bivocabulary:
		w1 = word.split()[0]
		w2 = word.split()[1]
		
		if pos.count(word) == 0:
			pcount[univocabulary.index(w1)] += 1
			pcount[univocabulary.index(w2)] += 1
			pbProb.append(0)
		else:
			positiveCount = pos.count(word)
			pbProb.append( (1.0 * positiveCount)/pos.count(w1) )
		
		if neg.count(word) == 0:
			ncount[univocabulary.index(w1)] += 1
			ncount[univocabulary.index(w2)] += 1
			nbProb.append(0)
		else:
			negativeCount = neg.count(word) 
			nbProb.append( (1.0 * negativeCount)/neg.count(w1) )


	for i in range(len(univocabulary)):
		puProb.append((1.0 * pcount[i])/totalCountInPositive)
		nuProb.append((1.0 * ncount[i])/totalCountInNegative)
	return (P1, P2, puProb, nuProb, pbProb, nbProb)

def createParts(reviews_list):
	reviews = [[],[],[],[],[],[],[],[],[],[]]
	for i in range(len(reviews_list)):
		reviews[int(i/80)].append(reviews_list[i])
	return reviews

def getReviews(reviews_list):
	review_value = []
	for review in reviews_list:
		review_value.append(review[0])
	return review_value

def testing(test_list, univocabulary, bivocabulary, P1, P2, upp, unp, bpp, bnp):
	result_value = []
	for test in test_list:
		test = test.split()
		if univocabulary.count(test[0]) == 0:
			sum_of_pprob = 0
			sum_of_nprob = 0
		else:
			sum_of_pprob = math.log1p(upp[univocabulary.index(test[0])])
			sum_of_nprob = math.log1p(unp[univocabulary.index(test[0])])
		for i in range(len(test)-1):
			word = test[i]+" "+test[i+1]
			if bivocabulary.count(word):
				index = bivocabulary.index(word)
				sum_of_pprob += math.log1p(bpp[index])
				sum_of_nprob += math.log1p(bnp[index])
			else:
				if univocabulary.count(test[i+1]):
					index = univocabulary.index(test[i+1])
					sum_of_pprob += math.log1p(upp[index])
					sum_of_nprob += math.log1p(unp[index])

		positiveProbability = sum_of_pprob + math.log1p(P1)
		negativeProbability = sum_of_nprob + math.log1p(P2)
		if positiveProbability >= negativeProbability:
			result_value.append('+')
		else:
			result_value.append('-')
	return result_value

def getAccuracy(actual, result):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == result[i]:
			correct += 1
	return (1.0 * correct)/len(actual)	

if __name__ == '__main__':
	data = open("cleaned_data.txt", "r")
	file1 = open("vocab-unigram.txt", "r")
	file2 = open("vocab-bigram.txt", "r")

	reviews = createParts(data.read().splitlines())
	univocabulary = file1.read().splitlines()
	bivocabulary = file2.read().splitlines()

	accuracy = 0
	for i in range(10):
		actual_values = []
		test_set = []
		for review in reviews[i]:
			test_set.append(review[1:])
			actual_values.append(review[0])
		
		training_set = []
		for j in range(10):
			if i != j:
				training_set.extend(reviews[j])
		
		P1, P2, upp, unp, bpp, bnp = training(training_set, univocabulary, bivocabulary)
		result_values = testing(test_set, univocabulary, bivocabulary, P1, P2, upp, unp, bpp, bnp)
		current_accuracy = getAccuracy(actual_values, result_values)
		print(current_accuracy)

		accuracy += current_accuracy

	print("Accuracy: ", accuracy/10)

