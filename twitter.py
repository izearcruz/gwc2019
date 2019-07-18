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
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)

pltList = []
for i in tweets:
	blob1 = TextBlob(i)
	polar1 = blob1.polarity
	pltList.append(polar1)
print(pltList)
#------------------------------
print(pltList)
print(min(pltList), max(pltList))
n, bins, patches = plt.hist(pltList)
plt.axis([-0.55, 1.05, 0, 50])
# plt.show()
plt.savefig("izear.png")



# plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
# plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two" color='g')
# plt.legend()
# plt.()

#------------------------------
# print(text)

# for item in text:
# 	long_string += item+''
#'''
# wordcloud = WordCloud().generate(long_string)
# #generates wordcloud
# tweetD = " "
# for tweet in tweets:
# 	tweet += " "
# 	tweetD += tweet
# print(tweetD)
#
# wordcloud = WordCloud(height = 1000, width = 1000 ).generate(tweetD)
# plt.imshow(wordcloud, interpolation= 'bilinear')
# plt.axis("off")
# plt.show()
# plt.savefig('alischart.png')
# '''
