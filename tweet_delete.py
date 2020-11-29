######################################################################
# tweet_delete.py                                                    #
# Deletes al list of tweets in the specified date range with a       #
#  like count lower than specified                                   #
#                                                                    #
# REQUIRES:                                                          #
#                                                                    #
#   'tweet.js' file extracted from your Twitter Data Archive         #
#     obtained here: https://twitter.com/settings/your_twitter_data  #
#                                                                    #
#   API credentials created by registering an app:                   #
#        https://developer.twitter.com/en/apps                       #
#                                                                    #
######################################################################

import time
from datetime import datetime
import twitter
from dateutil.parser import parse
import json

# API Creds
CONSUMER_KEY = "XXXXXXXXXX"
CONSUMER_SECRET = "XXXXXXXXXX"
ACCESS_TOKEN_KEY = "XXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXX"

api = twitter.Api(consumer_key = CONSUMER_KEY,
                  consumer_secret = CONSUMER_SECRET,
                  access_token_key = ACCESS_TOKEN_KEY,
                  access_token_secret = ACCESS_TOKEN_SECRET)


# Deletion Function
def deleteTweet(tweetId):
   try:
     print("Deleting #{0})".format(tweetId))
     api.DestroyStatus(tweetId)
     print("Done")

   except Exception as err:
      print("Exception: %s\n" % err)

tweetData = None
with open('tweet.js') as json_file:
    tweetData = json.load(json_file)

# Date ranges (UTC)
rangeStart = datetime.strptime('Sep 10 00:00:00 +0000 2012','%b %d %H:%M:%S %z %Y')
rangeEnd = datetime.strptime('Nov 29 00:00:00 +0000 2019','%b %d %H:%M:%S %z %Y')

# Create a list of all tweets to be deleted, but save anything with ample likes ("favorites")
deleteList = []
for element in tweetData["data"]:
  likes = element["tweet"]["favorite_count"]
  postTime = datetime.strptime(element["tweet"]["created_at"],'%a %b %d %H:%M:%S %z %Y')
  if (postTime>= rangeStart and postTime<= rangeEnd and int(likes) < 30):
    deleteList.append(element["tweet"]["id_str"])

# (Crappy saftey check): Uncomment the code below to actually delete tweets:
#for id in deleteList:
#  deleteTweet(id)