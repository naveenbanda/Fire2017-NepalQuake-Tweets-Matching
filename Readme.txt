This folder contains, apart from this Readme.txt file, two folders named "microblogs-crawl-directory" and “development-set-directory”. 

* The folder "microblogs-crawl-directory" contains:

(1) a text file "NepalQuake-code-mixed-training-tweetids.txt" containing 20K tweetids, i.e., identifiers of tweets / microblogs posted in Twitter during the Nepal earthquake in April 2015.

(2) a Python script "crawl_tweets.py" along with the libraries that are required by this script.

The script should be executable on any standard Linux machine having Python 2.x installed and having Internet connection. On running the script, the tweets corresponding to the tweetids in the above text file will be downloaded using the Twitter API. This crawling process should require around 3--4 hours. However, the download may need more time if multiple groups are attempting to download the tweets in parallel. 


The downloaded tweets will be written into a file named "NepalQuake-code-mixed-training-tweets.jsonl" which will be created in the same directory where the script is located. Each line in this file will be a json-encoded tweet, where json (JavaScript Object Notation) is an open standard format that uses human-readable text to transmit data objects consisting of attribute–value pairs. 

The attributes for a tweet, as returned by the Twitter API, are described at https://dev.twitter.com/overview/api/tweets. Specifically, the value corresponding to the "text" attribute gives the textual content of the tweet, and the value corresponding to the "id" attribute gives the integer tweetid of the tweet.

Json parsers are available in all popular programming languages, and such a parser can be used to decode each line of this file individually, to get the attribute-value pairs for a tweet.

You can refer to http://www.json.org/ for more details on json, and for knowing about json parsers in various programming languages.


* The folder “development-set-directory” contains the following three files:

(1) NepalQuake-need-tweetids-development-set.txt - the tweetids of the need-tweets among the 20K tweets in the training set

(2) NepalQuake-availability-tweetids-development-set.txt - the tweetids of the  availability-tweets among the 20K tweets in the training set

(3) NepalQuake-sample-need-availability-matched-tweetids-development-set.txt — contains some of the correct matchings of need-tweets and availability-tweets. 
Format of each line is <Need-tweet id>:<Availability-tweet id1>, <Availability-tweet id2>,…,<Availability-tweet id5>, where the availability-tweets mentioned in a line are all correct matchings for the need-tweet whose id is mentioned at the beginning of the same line.



=====

Note that multiple people often post the same text in Twitter, e.g., by retweeting or copying someone else's tweet. We have attempted to remove such duplicate tweets as far as possible, still there might be some duplicates (i.e., multiple tweets containing the same or nearly same text, but different tweetids) in the tweet file. For such cases, if a certain tweet is relevant to a particular topic, all duplicates of that tweet will be considered relevant to that topic as well.

===== 

Note that, with time, some tweets may have got deleted. If you fail to download many of the tweets, we can provide you directly with the json objects corresponding to the tweets in the training data. For this, please contact the Track Organizers at fire2017irmidis@gmail.com. 


