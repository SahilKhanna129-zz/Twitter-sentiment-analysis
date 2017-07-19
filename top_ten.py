import sys
import json
import operator

def hw(tweet_file):
    termFrequency = {}
    total_words = 0
    for line in tweet_file:
        tweet = json.loads(line)
        if tweet.has_key('entities') and tweet['entities'] is not None:
            entities = tweet['entities']
            if entities.has_key('hashtags') and entities['hashtags'] is not None:
                hashtags = entities['hashtags']
                for hashtag in hashtags:
                    word = hashtag['text']
                    if termFrequency.has_key(word):
                        termFrequency[word] = termFrequency[word] + 1
                    else:
                        termFrequency[word] = 1
    count = 0
    
    sorted_hashvalues = sorted(termFrequency.items(), key=operator.itemgetter(1))
    
    for i in range(0, 10):
        key, freq = sorted_hashvalues[i]
        print key + " " + str(freq)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    #tweet_file = open("C:/Users/skhan/Documents/DataScience/datasci_course_materials/TwitterSentimentAnalysis/output.txt")
    hw(tweet_file)

if __name__ == '__main__':
    main()
