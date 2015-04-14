import sys
import json
import string
import operator



def lines(fp):
	nlines = str(len(fp.readlines()))
	return nlines

def parse_tweet_file(lp):
	tweets = {}
	
	tweets = json.loads(lp)
	
	entities = dict(tweets.get('entities',""))
	#entities = dict(entities)
	
	hashtagstring = ""
	
	for key in entities:
		if key == 'hashtags':
			hashtags = entities.get(key,"")
		
			#print hashtags
		
			for individualhashtags in hashtags:
				hashtags2 = individualhashtags
				
				for key2 in hashtags2:
					if key2 == 'text':
						hashtags3 = hashtags2.get(key2,"")
						hashtagstring = hashtagstring + hashtags3

	hashtagstring = hashtagstring.lower()					
	#print hashtagstring
	return hashtagstring
				

def main():
	#sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[1])
	#hw()
	#lines(sent_file)
	nlines = lines(tweet_file)
	#print nlines
	

	#scores = {} # initialize an empty dictionary

	#for line in sent_file:
	#	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	#	scores[term] = int(score)  # Convert the score to an integer.	
		
	number = {}

	tweet_file = open(sys.argv[1])
	for line in tweet_file:
		
		tweetsphrase = parse_tweet_file(line)
		
		for word in tweetsphrase.split():
			number[word] = 0
						
		
		
	tweet_file = open(sys.argv[1])
	for line in tweet_file:
		
		tweetsphrase = parse_tweet_file(line)
		
		for word in tweetsphrase.split():
			number[word] = number[word] + tweetsphrase.count(word)	
			
	
	
#	print number
	
	sorted_number = sorted(number.iteritems(), key=operator.itemgetter(1), reverse=True)
	
#	print sorted_number
	
	index = 0
	
	for word in sorted_number:
		if index < 10:
			index = index + 1
			print word[0], word[1]
			
	

	
if __name__ == '__main__':
	main()

