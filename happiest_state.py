import sys
import json
import string
import operator



def lines(fp):
	nlines = str(len(fp.readlines()))
	return nlines
	

def determine_location(tweets):
	
	user = dict(tweets.get('user',""))
		
	hashtagstring = ""
	
	for key in user:
	
		if key == 'location':
			location = user.get(key,"")
			location = location.lower()
		
			return location




def determine_sentiment(tweets, scores):

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
	
	#print sentiment
	return sentiment

 

def parse_sent_file(sent_file):
	scores = {} # initialize an empty dictionary

	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.	
	return scores

 
def parse_tweet_file(tweet_file, scores):

	us_states = {'alabama':'AL','alaska':'AK','american samoa':'AS','arizona':'AZ','arkansas':'AR','california':'CA','colorado':'CO','conneticut':'CT','delaware':'DE','district of columbia':'DC','florida':'FL','georgia':'GA','guam':'GU','hawaii':'HI','idaho':'ID','illinois':'IL','indiana':'IN','iowa':'IA','kansas':'KS','kentucky':'KY','louisiana':'LA','maine':'ME','maryland':'MD','massachusetts':'MA','michigan':'MI','minnesota':'MN','mississippi':'MS','missouri':'MO','montana':'MN','national':'NA','nebraska':'NE','nevada':'NV','new hampshire':'NH','new jersey':'NJ','new mexico':'NM','new york':'NY','north carolina':'NC','north dakota':'ND','northern mariana islands':'MP','ohio':'OH','oklahoma':'OK','oregon':'OR','pennsylvania':'PA','puerto rico':'PR','rhode island':'RI','south carolina':'SC','south dakota':'SD','tennessee':'TN','texas':'TX','utah':'UT','vermont':'VT','virgin islands':'VI','virginia':'VA','washington':'WA','west virginia':'WV','wisconsin':'WI','wyoming':'WY'}

	state_sentiment = {}
	state_ntweets = {}
	state_avg_sentiment = {}
	
	for state in us_states:
		state_sentiment[state] = 0
		state_ntweets[state] = 0

	for line in tweet_file:
		tweets = {}
	
		tweets = json.loads(line)
	
		location = determine_location(tweets)
	
		sentiment = determine_sentiment(tweets, scores)
	
		for state in us_states:
			if location == state:		
				state_sentiment[state] = state_sentiment[state] + sentiment
				state_ntweets[state] = state_ntweets[state] + 1
	
	for state in us_states:
		if state_ntweets[state] != 0:
			state_avg_sentiment[state] = float(state_sentiment[state])/float(state_ntweets[state])
		elif state_ntweets[state] == 0:
			state_avg_sentiment[state] = 0#float(0)
		
		#print us_states[state], state_sentiment[state], state_ntweets[state], state_avg_sentiment[state]
			
	
	sorted_state_avg_sentiment = sorted(state_avg_sentiment.iteritems(), key=operator.itemgetter(1), reverse=True)
	
	
	index = 0
	#print 'STATES FROM HAPPIEST TO LEAST HAPPY'
	for word in sorted_state_avg_sentiment:
		if index < 1: #len(us_states):
			index = index + 1
			print us_states[word[0]]#, word[1]





def main():
	
	sent_file = open(sys.argv[1])
	scores = parse_sent_file(sent_file)
		
	tweet_file = open(sys.argv[2])	
	nlines = lines(tweet_file)


	tweet_file = open(sys.argv[2])	
	parse_tweet_file(tweet_file, scores)
		
	
				



if __name__ == '__main__':
	main()

