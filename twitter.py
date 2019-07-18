'''
In this program, we print out all the text data from our twitter JSON file.
Please explain the comments to students as you code.
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")
# We use the JSON library to get data from the file as JSON data.
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
# #-------------------------------
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)
#
# pltList = []
# for i in tweets:
# 	blob1 = TextBlob(i)
# 	polar1 = blob1.polarity
# 	pltList.append(polar1)
# print(pltList)
#------------------------------
#another way to do that code ^^^
# for i in range(0,len(listo)):
# 	blob1+TextBlob(listoftweets[i])
# polar1 = blob.polarity
# polarityList.appond(polar1).
#--------------------

# import matplotlib.pyplot asa plt
# plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
# plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two" color='g')
# plt.legend()
# plt.()

#---------------------------------
# print(text)

# for item in text:
# 	long_string += item+''
#
# wordcloud = WordCloud().generate(long_string)

tweetD = " "
for tweet in tweets:
	tweet += " "
	tweetD += tweet
print(tweetD)


wordcloud = WordCloud().generate(tweetD)
plt.imshow(wordcloud, interpolation= 'bilinear')
plt.axis("off")
plt.show()
plt.savefig('alischart.png')

# id.tweet polarity
# texts =[tweets]
# polarityList = [0.0,0.9]
# leest = []
# # tweetData[i['id']]
#
# for i in range(len(tweetData)):
# 	dictionaree = {}
# 	dictionaree["id"] = tweetData[i]['id']
# 	dictionaree["polarity"] = polarityList[i]
# 	dictionaree["tweet"] = texts[i]
# 	leest.append(dictionaree)

#----------------------------------

# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])

# 	return count
#
# 	numA = 0
# 	index = 0
# 	alpha = ""
# 	num = [0] * 26
#
# for tweet in tweetData:
# 	if "text"
# print(avg)
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])

# Encourage students to think about how there are
# often multiple solutions for each problem, and
# how each solution might have strenghts and drawbacks.
