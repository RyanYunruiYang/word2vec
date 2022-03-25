# So, I had found a statistically significant correlation in my experimental data.
# The predicted values went down for both trials with larger inputs, as well as trials
# later on in the class block. So, I was unsure if these lower values were closer for
# further from the real answer. In order to be neutral, I chose a positive and a negative word:
# experience and fatigue, and created a variable called experience-fatigue, defined as 
# 1/2 (triallen/maxlen + trialnum/totalnumtrial). But, I've always wondered if there's 
# a word that averages the two sentiments. That's what this code is meant to do.

# I downloaded a already trained implementation of word2vec, where each word has a 
# 25-dimension vector. It's trained so that the cos(theta) between any two vectors
# is the similarity score. (kinda, this is abuse of notation or something)
# and then based on this I make a distance function. (1-cos(theta)).
# then i defined the midpoint, inspired by the barycenter, to be the word that minimizes
# d(m,a)^6 + d(m,b)^6.



import gensim
import math
from gensim import downloader

def method1(x,y, power):
	return (1-x)**power + (1-y)**power

def method2(x,y):
	return (1/(x+1.01)-1/2)**2 + (1/(y+1.01)-1/2)**2
#Defining the distance function is wacky:
#https://arxiv.org/pdf/2107.04071.pdf

def avg(word1, word2, method): 
	# n = 
	minvals = [model.index_to_key[i] for i in range(3)]

	distances = []
	print("trying its best 1")
	for i in range(len(model)):
		word = model.index_to_key[i]
		if(method==1):
			power = 6
			dist = method1(model.similarity(word1,word), model.similarity(word2,word), power)
		if(method==2):
			dist = method2(model.similarity(word1,word), model.similarity(word2,word))
		if(method==3):
			dist = max(1-model.similarity(word1,word), 1-model.similarity(word2,word))
		distances.append([word, dist])

	distances = sorted(distances, key = lambda x: x[1])
	return [distances[i][0] for i in range(5)]

				
		# if(dist < nth):
		# 	index = i
		# 	minval = dist
	# return index


model = gensim.downloader.load('glove-twitter-25') #fuck it
print("done downloading")

def main():
	print(len(model))

	print(model.index_to_key[0])
	#similarity score = cos theta
	# testing_set = [['mom','dad'],['experience', 'fatigue'],['red','blue'], ['reap','read'], ['amber','bronze'],['king','queen']]
	testing_set = [['tired', 'experienced']]

	# --> possible
	for pair in testing_set:
		print("the average of " + pair[0] +" and " + pair[1] + " is: ")
		print(avg(pair[0],pair[1],3)) #possible
		print("\n")
		# print(model.index_to_key[avg(pair[0],pair[1],2)]) #possible


if __name__ == "__main__":
	main()

