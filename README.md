# prefix_twitter_followers
- get list of Twitter followers (any account) and prefix

## reason
Wanted simple (potentially reusable) way to copy+paste list of all follower names to tweets/thread as in [100 Follower Tweet](https://twitter.com/CoderMatching/status/1516423584641597450?s=20&t=JRYUY43xxrgHsv11YOE52g)

## usage
1. Download .CSV file of all follwers, using [Phantombuster's *Twitter Follower Collector*](https://phantombuster.com/automations/twitter/4130/twitter-follower-collector)
    - alternatively use Twitter API directly
2. copy+paste *screenName* colums to empty .txt file
3. run `prefix_followers.py` as follows

    `py prefix_followers.py followers.txt C:\Users\Name\Desktop\addressTwitterFollowers`

## potential limitations
- probably expects a windows path
- doesn't matter whether "\" at the end of third input parameter on command line or not (works both ways)