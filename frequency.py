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
	frequency = {}

	totalwords = 0


	tweet_file = open(sys.argv[1])	
	for line in tweet_file:
		
		tweetsphrase = parse_tweet_file(line)

		for word in tweetsphrase:
		
			totalwords = totalwords + 1
		
			number[word] = 0
	
	#print totalwords
		
		
	tweet_file = open(sys.argv[1])
	for line in tweet_file:
		
		tweetsphrase = parse_tweet_file(line)
				
		for word in tweetsphrase:
		
			number[word] = number[word] + tweetsphrase.count(word)
			
			frequency[word] = float(number[word])/float(totalwords)
			
		#	print word, number[word]
			
		
	for word in number:
		print word, frequency[word]



	
if __name__ == '__main__':
	main()

