class Twitter:

    def __init__(self):
        # self.users: []
        self.followers = {}
        self.followees = {}
        self.tweets = []
        self.userTweets = {}

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append(tweetId)
        if userId in self.userTweets:
            self.userTweets[userId].append(tweetId)
        else:
            self.userTweets[userId] = [tweetId]
        # if not userId in self.followers:
        #     self.followers[userId] = [userId]
        
        if not userId in self.followees:
            self.followees[userId] = [userId]

    def getNewsFeed(self, userId: int) -> List[int]:
        if not userId in self.followees: return []

        feedTweets = []

        for user in self.followees[userId]:
            if user in self.userTweets:
                for tweet in self.userTweets[user]:
                    # print('a', tweet)
                    feedTweets.append(tweet)
        userFeed = []
        index = len(self.tweets) -1
        while len(userFeed)<10 and len(feedTweets)>0 and index>=0:
            # print('b', self.tweets[index], feedTweets)

            if self.tweets[index] in feedTweets:
                feedTweets.remove(self.tweets[index])
                userFeed.append(self.tweets[index])
            index -= 1
        # print('c', userFeed)
        return userFeed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        # if not followerId in self.followers:
        #     self.followers[followerId] = [followerId]
        
        if not followerId in self.followees:
            self.followees[followerId] = [followerId]
        
        # if not followeeId in self.followers:
        #     self.followers[followeeId] = [followeeId]
        
        if not followeeId in self.followees:
            self.followees[followeeId] = [followeeId]

        # self.followers[followeeId].append(followerId)
        if not followeeId in self.followees[followerId]:
            self.followees[followerId].append(followeeId)
        # print("F followees of ", followerId, self.followees[followerId] )


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # self.followers[followeeId].remove(followerId)
        if followeeId in self.followees[followerId] and not followeeId == followerId:
            self.followees[followerId].remove(followeeId)
        # print("U followees of ", followerId, self.followees[followerId] )

        
