import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
#------------------------------
# print(type(tweetData))
# print(type(tweetData[0]))
# # tweetFile.close()
#
# print(tweetData[0]['favorite_count'])
#
# favoriteCount, numberOfFavoriteCounts = 0,0
#
# for i in range(len(tweetData)):
#
# 	if "favorite_count" in tweetData[i]:
# 		favoriteCount += tweetData[i]["favorite_count"]
# 		numberOfFavoriteCounts += 1
#
# avg= favoriteCount  / numberOfFavoriteCounts
# print(avg)
#-----------------------------
# tweetData[]
# tweetData[0]["text"]
# for tweet in tweetData:
# 	if "text" in tweet:
# 		text = tweet["text"]
# 		for index in range(26):
# 			print(index)
#------------------------------
tweets = []
for i in range(0,len(tweetData)):
	word = tweetData[i]["text"]
	tweets.append(word)

# print(tweets)
#------------------------------
# def counter(string, letter):
# 	counter = 0
# 	for let in string:
# 		if let.lower() == letter:
# 			counter += 1
# 	return counter
#
# tweetstring = ""
# for tweet in tweets:
# 	tweet = tweet + " "
# 	tweetstring += tweet
# print(tweetstring)
#
# counter(tweetstring, "a")
# alpha = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
# letters = sorted(alpha)
#
# occurrences = []
# for letter in letters:
# 	occurrences.append(counter(tweetstring, letter))
# print(occurrences)
# print(min(occurrences), max(occurrences))
# plt.hist(occurrences)
# plt.axis([min(occurrences), max(occurrences), 0, 10])
# plt.show()
#------------------------------------------------
def wordcount(stringoftweet, string1):

	counter = 0
	string1 = string1.lower()
	wordlist = stringoftweet.split(' ')
	for item in wordlist:
		if item == string1:
			counter += 1
	return counter

wordcountlist = []
for item in tweets:
	wordoccurrences = wordcount(item, "the")
	wordcountlist.append(wordoccurrences)

	n, bins, patches = plt.hist(wordcountlist, 50)
	plt.axis([min(wordcountlist), max(wordcountlist), 0, 10])
	plt.grid(True)
	plt.show()
#-----------------------------------------------
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)
#
# pltList = []
# for i in tweets:
# 	blob1 = TextBlob(i)
# 	polar1 = blob1.polarity
# 	pltList.append(polar1)
# print(pltList)
# #------------------------------
# print(pltList)
# print(min(pltList), max(pltList))
# n, bins, patches = plt.hist(pltList)
# plt.axis([-0.55, 1.05, 0, 50])
# plt.show()
#'''
# wordcloud = WordCloud().generate(long_string)
# #generates wordcloud
# tweetD = " "
# for tweet in tweets:
# 	tweet += " "
# 	tweetD += tweet
# print(tweetD)
#---------------------------------
# wordcloud = WordCloud(height = 1000, width = 1000 ).generate(tweetD)
# plt.imshow(wordcloud, interpolation= 'bilinear')
# plt.axis("off")
# plt.show()
# plt.savefig('alischart.png')
# '''
