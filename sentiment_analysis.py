from twython import Twython
import sys
import re
from textblob import TextBlob
import matplotlib.pyplot as plt

def class_tweet(tweet):
    return (' '.join(re.sub("(@[A-Za-z0-9]+)([^0-9A-Za-z \t])|(\w+:\|\|\s+)",
                            " ",tweet).split()))

def get_tweet_sentiment(tweet):
    analysis = TextBlob(class_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return ('positive')
    elif analysis.sentiment.polarity==0:
        return ('neutral')
    else :
        return ('negative')
consumer_key="##"
consumer_secret="##"
access_token= "##"
access_token_secret= "##"
tw=Twython(consumer_key,consumer_secret,access_token,access_token_secret)
result_dict=tw.search(q='rahulhugsmodi',lang='en',count=30,result_type='popular')
non_bmp_map=result_dict.fromkeys(range(0x10000,sys.maxunicode+1),0xfffd)
print(result_dict)
print("##########Text in tweet#######")
list_tweet = result_dict['statuses']
for tweet in list_tweet:
    print(tweet['text'].translate(non_bmp_map))
    print('\n\n\n\n\n')

sentiments_total={'neutral':0, 'positive' :0,'negative':0}
for record in list_tweet:
    tweet_raw = (record['text'].translate(non_bmp_map))
    sentiment = get_tweet_sentiment(tweet_raw)
    print(sentiment,'==>',record['text'].translate(non_bmp_map))
    sentiments_total[sentiment]=sentiments_total[sentiment]+1
    print("#################################")

print(sentiments_total)

slices = [sentiments_total['neutral'],sentiments_total['positive'],sentiments_total['negative']]
activities = ['neutral','positive','negative']

plt.pie(slices,labels=activities,autopct='%1.1f%%')
plt.legend()
plt.show()

    

