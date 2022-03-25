# word2vec
For Playing Around with word2vec

So, I had found a statistically significant correlation in my experimental data.
The predicted values went down for both trials with larger inputs, as well as trials
later on in the class block. So, I was unsure if these lower values were closer for
further from the real answer. In order to be neutral, I chose a positive and a negative word:
experience and fatigue, and created a variable called experience-fatigue, defined as 
1/2 (triallen/maxlen + trialnum/totalnumtrial). But, I've always wondered if there's 
a word that averages the two sentiments. That's what this code is meant to do.

I downloaded a already trained implementation of word2vec, where each word has a 
25-dimension vector. It's trained so that the cos(theta) between any two vectors
is the similarity score. (kinda, this is abuse of notation or something)
and then based on this I make a distance function. (1-cos(theta)).
then i defined the midpoint, inspired by the barycenter, to be the word that minimizes
d(m,a)^6 + d(m,b)^6.
