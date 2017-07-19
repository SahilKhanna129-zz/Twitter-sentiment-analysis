import sys
import json

def hw(sent_file, tweet_file):
    score = getScore(sent_file)
    count = 0
    for line in tweet_file:
        count += 1
        tweet = json.loads(line)
        sentimentScore = 0
        if 'text' in tweet.keys():
            words = tweet[u'text'].split()
            for word in words:
                word = word.lower().strip(',''.''?''!')
                if word in score.keys():
                    sentimentScore += score[word]
                else:
                    sentimentScore += 0
            print sentimentScore

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
