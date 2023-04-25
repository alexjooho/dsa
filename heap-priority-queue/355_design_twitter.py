# neetcode solution:
# use a hashmap for tweets where key is userId and value is a list of their tweets with each tweet
# being in the format [time, tweetId]
# uses a heap for finding the 10 most recent tweets
# a lot more realistic for an actual app

# keep track of a count to represent time. We subtract 1 from it every time a count is made because
# we are using a minheap and this lets the most recent tweet be at the top of heap

# to find the 10 most recent tweets, we add the most recent tweet from every user that the user follows
# to the heap. When we add them to the heap, we include: [time, tweetId, followeeId, index - 1]
# we keep popping from the heap while there are tweets in the heap and we haven't gotten 10 tweets yet
# each time we pop, we add the next most recent tweet from the user if the user has more tweets
# this way, we are always searching for the most recent tweet out of the tweets we haven't checked

# Time Complexity: O(k + 10 log k + 10 log k) => O(k) where k is the number of people the user follows
# k to heapify the most recent tweet of k users, 10 log k for the 10 times we pop, and 10 log k for
# the 10 times we push

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        # decrement count

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        # we have to add the user to his/her own follow set because we want to include their tweets
        # it will not add multiple times since it is a set
        for followeeId in self.followMap[userId]:
            # start by getting the most recent tweet of everyone the user is following (including themselves)
            if followeeId in self.tweetMap:
                # make sure that followee even has a tweet
                index = len(self.tweetMap[followeeId]) - 1
                # we want to get the last (most recent) tweet
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
                # NOTE: we are just appending for now instead of heappushing, but we heapify later
                # when we push to the heap, we are including the followeeId so if it gets popped
                # we will know who's next most recent tweet to add
                # we also include index - 1 to indicate the index of their next most recent tweet
                # so that if it is >= 0, we know that they still have more tweets
        heapq.heapify(minHeap)
        # we heapify once instead of heappushing each time so that it is just O(k) instead of O(k log k) to make the heap

        while minHeap and len(res) < 10:
            # while there are still tweets and we haven't gotten 10 tweets yet
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            # get all the variables of the most recent tweet and append tweetId to result
            res.append(tweetId)
            if index >= 0:
                # if there is a next most recent tweet, we now add it to the heap so 
                # that it can be compared with all the other users' tweets to see which one
                # is the most recent out of them all
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
            
# NOTE: another idea I had was to add up to 10 of the most recent tweets (if applicable) 
# of each user the user follows and then heapify it and pop 10. 
# But this would be O(10k) instead of O(k) which is slightly worse


# my solution that works (same results on leetcode) but is naive for an actual app:
# time complexity is O(n) where n is the number of ALL tweets
# for an app where there could be many tweets, this is much worse than neetcode's solution
# where it is just O(k) where k is the number of users the user follows

class Twitter:
    # create a class that has a queue for all tweets made
    # the class will also have a hashmap (defaultdict) with keys of user and values being a set with 
    # all the users that user is following

    def __init__(self):
        self.tweets = collections.deque()
        self.users = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # append the tweet to the beginning of the queue
        # the tweet will be [userId, tweetId] so that we can check both later
        self.tweets.appendleft([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        # create a list that represents the newsfeed
        # iterate through the tweets and
        # add tweets from followed people and the user themselves
        # to the list until the tweets are exhausted
        # or there are 10 tweets in the list
        # NOTE: make sure to include tweets from the user themselves

        feed = []
        for user, tweet in self.tweets:
            if user in self.users[userId] or user == userId:
                feed.append(tweet)
                if len(feed) == 10:
                    break
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # add the followee to the follower's set in the hashmap
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove the followee from the follower's set in the hashmap
        # edge case of trying to unfollow someone that they aren't following
        # so we have to check first!
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)