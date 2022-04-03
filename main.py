from generate_tweet import all_data
import random

def create_tweet(data):
    random_element = random.randrange(0, len(data), 1)
    tweet_data = data[random_element]
    tweet_text = f'''In {tweet_data['year']}, out of 100.000 men living in {tweet_data['country']}, {tweet_data['male']} killed themselves. {tweet_data['female']} women did the same. 
    Do not become a statistic. If you're feeling down, reach out. See some resources below.\n'''
    return tweet_text

for i in range (0, 10):
    print(create_tweet(all_data))