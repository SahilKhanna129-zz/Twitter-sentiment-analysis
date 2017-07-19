import sys
import json
import re

def hw(sent_file, tweet_file):
    score = getScore(sent_file)
    termScore = {}
    for line in tweet_file:
        tweet = json.loads(line)
        sentimentScore = getSentimentScore(tweet, score)
        if 'text' in tweet.keys():
            words = tweet[u'text'].split()
            for word in words:
                word = word.lower().strip(',''.''?''!''#''"')
                word = re.compile('[^a-zA-Z]').sub('',word)
                if word is "": continue
                if ~score.has_key(word):
                    if termScore.has_key(word):
                        termScore[word] = (termScore[word] + sentimentScore)/2
                    else:
                        termScore[word] = sentimentScore
    count = 0
    for key in termScore:
        if count is 0:
            count += 1
            continue
        print key + " " + str(termScore[key])

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

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
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
