import sys
import json
import string




def lines(fp):
	nlines = str(len(fp.readlines()))
	return nlines
 

	

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
	
	for line in tweet_file:
		tweets = {}
	
		tweets = json.loads(line)
		
		tweetstext = tweets.get('text',"")
		tweetstextu = tweetstext.encode('utf-8')
		
		
		replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
		tweetstextunopunc = tweetstextu.translate(replace_punctuation)
		tweetstextunopunc = tweetstextunopunc.lower()
		
		#print tweetstextu
		#print tweetstextunopunc
				
		sentiment = 0
		for word in tweetstextunopunc.split():
			
			if word in scores:
			
				sentiment = sentiment + scores[word]
			
			#	print word, scores[word]
				
		print sentiment
	
				



if __name__ == '__main__':
	main()

