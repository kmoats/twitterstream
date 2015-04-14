import sys
import json
import string



def lines(fp):
	nlines = str(len(fp.readlines()))
	return nlines
 

def parse_tweet_file(lp):
	tweets = {}
	
	tweets = json.loads(lp)
		
	tweetstext = tweets.get('text',"")
	tweetstext = tweetstext.encode('utf-8')
	#print tweetstext
		
	tweetstext = tweetstext.lower()
	replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
	tweetstext = tweetstext.translate(replace_punctuation)
	#print tweetstext

	tweetsphrase = tweetstext.split()
	return tweetsphrase

	

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#hw()
	#lines(sent_file)
	nlines = lines(tweet_file)
	#print nlines
	

	scores = {} # initialize an empty dictionary

	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.	
	
	
	tweet_file = open(sys.argv[2])	
	
	tweet_sentiment = {}
	positive_tweets = {}
	negative_tweets = {}
	ratio_tweets = {}
	score_new = {}
	
	for line in tweet_file:
	
		tweet_sentiment[line] = 0
		
		tweetsphrase = parse_tweet_file(line)
		for word in tweetsphrase:
			positive_tweets[word] = 0
			negative_tweets[word] = 0
			score_new[word] = 0
		
	
	tweet_file = open(sys.argv[2])	
	
	for line in tweet_file:
		
		tweetsphrase = parse_tweet_file(line)
		
		
					
		sentiment = 0
		for word in tweetsphrase:
			
			if word in scores:
			
				tweet_sentiment[line] = tweet_sentiment[line] + scores[word]
		#		print word, scores[word]
			
		#	else:
		#		print "sentiment value not assigned: ", word
		
				
		for word in tweetsphrase:
			
			if word not in scores:
				if tweet_sentiment[line] > 0:
					positive_tweets[word] = positive_tweets[word] + 1
				
				if tweet_sentiment[line] < 0:
					negative_tweets[word] = negative_tweets[word] + 1
				
	#	print "TOTAL SENTIMENT", tweet_sentiment[line]
	
	for word in positive_tweets:
	
		if negative_tweets[word] != 0:
			ratio_tweets[word] = float(positive_tweets[word])/float(negative_tweets[word])
			
		elif negative_tweets[word] == 0:
			ratio_tweets[word] = float(0)
	
			
		
		if positive_tweets[word] == 0 and negative_tweets[word] == 0:
			score_new[word] = 0
				
		elif positive_tweets[word] != 0 and negative_tweets[word] == 0:
			score_new[word] = positive_tweets[word]
			if positive_tweets[word] >= 5:
				score_new[word] = 5
		
		elif positive_tweets[word] == 0 and negative_tweets[word] != 0:
			score_new[word] = -1*negative_tweets[word]
			if positive_tweets[word] <= -5:
				score_new[word] = -5
		
		elif positive_tweets[word] != 0 and negative_tweets[word] != 0:
		
			if ratio_tweets[word] < 0.166666:
				score_new[word] = -5
			
			elif ratio_tweets[word] >= 0.166666 and ratio_tweets[word] < 0.2:
				score_new[word] = -4
			
			elif ratio_tweets[word] >= 0.2 and ratio_tweets[word] < 0.25:
				score_new[word] = -3
				
			elif ratio_tweets[word] >= 0.25 and ratio_tweets[word] < 0.333333:
				score_new[word] = -2
				
			elif ratio_tweets[word] >= 0.333333 and ratio_tweets[word] < 0.5:
				score_new[word] = -1
				
			elif ratio_tweets[word] >= 0.5 and ratio_tweets[word] < 2:
				score_new[word] = 0
				
			elif ratio_tweets[word] >= 2 and ratio_tweets[word] < 3:
				score_new[word] = 1
			
			elif ratio_tweets[word] >= 3 and ratio_tweets[word] < 4:
				score_new[word] = 2
				
			elif ratio_tweets[word] >= 4 and ratio_tweets[word] < 5:
				score_new[word] = 3
			
			elif ratio_tweets[word] >= 5 and ratio_tweets[word] < 6:
				score_new[word] = 4
			
			elif ratio_tweets[word] >= 6:
				score_new[word] = 5
				
				
				
		#if ratio_tweets[word] > 1:
		#	print word, positive_tweets[word], negative_tweets[word], ratio_tweets[word], "positive word", score_new[word]
			
		#if ratio_tweets[word] < 1:
		#	print word, positive_tweets[word], negative_tweets[word], ratio_tweets[word], "negative word", score_new[word]

		#if ratio_tweets[word] == 1:
		#	print word, positive_tweets[word], negative_tweets[word], ratio_tweets[word], "neutral word", score_new[word]
		
		print word, score_new[word]

		
				



if __name__ == '__main__':
	main()

