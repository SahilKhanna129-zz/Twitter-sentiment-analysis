import sys
import json
import re

def hw(tweet_file):
    termFrequency = {}
    total_words = 0
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            words = tweet[u'text'].split()
            total_words += len(words)
            for word in words:
                word = word.lower()
                word = re.compile('[^a-zA-Z]').sub('',word)
                if termFrequency.has_key(word):
                    termFrequency[word] = termFrequency[word] + 1
                else:
                    termFrequency[word] = 1
    count = 0
    for key in termFrequency:
        if count is 0:
            count += 1
            continue
        print key + " " + str(float(termFrequency[key])/total_words)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
