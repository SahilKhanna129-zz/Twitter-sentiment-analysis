import sys
import json

def hw(sent_file, tweet_file):
    score = getScore(sent_file)
    happiest_place = ""
    happiest_score = 0
    states = stateFullname()
    for line in tweet_file:
        tweet = json.loads(line)
        sentimentScore = getSentimentScore(tweet, score)
        if happiest_score < sentimentScore:
                
            if tweet.has_key('user') and tweet['user'] is not None:
                if tweet['user'].has_key('location') and tweet['user']['location'] is not None:
                    name = tweet['user']['location']
                    location = name.split()
                    for i in location:
                        if states.has_key(i):
                            happiest_place = i
                            happiest_score = sentimentScore
            
    print happiest_place
        
            
def getSentimentScore(tweet, score): 
    sentimentScore = 0
    if 'text' in tweet.keys():
        words = tweet[u'text'].split()
        for word in words:
            word = word.lower().strip(',''.''?''!')
            if score.has_key(word):
                sentimentScore += score[word]
            else:
                sentimentScore += 0
        return sentimentScore
    return 0

def lines(fp):
    print str(len(fp.readlines()))

def stateFullname():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}
    return states

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #sent_file = open("C:/Users/skhan/Documents/DataScience/datasci_course_materials/TwitterSentimentAnalysis/AFINN-111.txt")
    #tweet_file = open("C:/Users/skhan/Documents/DataScience/datasci_course_materials/TwitterSentimentAnalysis/output.txt")
    hw(sent_file, tweet_file)

def getScore(sent_file):
    afinnfile = sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    return scores
    
if __name__ == '__main__':
    main()
