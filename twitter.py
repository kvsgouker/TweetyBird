import tweepy

# authentication info from developer.twitter.com (secret)
# It’s not difficult to get approved but you have to interact a few times with gatekeepers.
APP_NAME = "appname you give to dev.twitter.com"
API_KEY = “blahblah-from-dev.twitter.com”
API_SECRET_KEY = “blahblah-secret-from-dev.twitter.com”
ACCESS_TOKEN = “blahblah-access-token from dev.twitter.com”
ACCESS_SECRET = "blahblah-access-secret from dev.twitter.com"
BEARER_TOKEN = “blahblah-bearer-token-dont-forget-to-get-elevated-rights-if-you-want-to-search from dev.twitter.com”

# constants for test program
TEST_USER = "your screen name"
TEST_USER2 = "BellevueU"



class TwitterAccess:
    api = None

    def __init__(self):
        # This information comes from Developer.Twitter.Com
        self.app_name = APP_NAME
        self.api_key = API_KEY
        self.api_secret_key = API_SECRET_KEY
        self.access_token = ACCESS_TOKEN
        self.access_secret = ACCESS_SECRET
        self.bearer_token = BEARER_TOKEN

    def login(self):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)
        try:
            self.api.verify_credentials()
            print('Successful Authentication')
            return self.api
        except tweepy.errors.Unauthorized:
            # Fail
            print('Failed authentication')
            return None

    def is_available(self):
        return self.api is not None

    def user_report_extended(self, screen_name):

        # fetching the user
        user = self.api.get_user(screen_name=screen_name)

        # printing the information
        print("The id is : " + str(user.id))
        print("The id_str is : " + user.id_str)
        print("The name is : " + user.name)
        print("The screen_name is : " + user.screen_name)
        print("The location is : " + str(user.location))
        print("The profile_location is : " + str(user.profile_location))
        print("The description is : " + user.description)

        print("The url is : " + user.url)
        print("The entities are : " + str(user.entities))
        print("Is the account protected? : " + str(user.protected))

        print("The followers_count is : " + str(user.followers_count))
        print("The friends_count is : " + str(user.friends_count))
        print("The listed_count is : " + str(user.listed_count))
        print("The account was created on : " + str(user.created_at))
        print("The favourites_count is : " + str(user.favourites_count))
        print("The utc_offset is : " + str(user.utc_offset))
        print("The geo_enabled is : " + str(user.geo_enabled))
        print("The verified is : " + str(user.verified))
        print("The statuses_count is : " + str(user.statuses_count))
        print("The lang is : " + str(user.lang))
        print("The status ID is : " + str(user.status.id))
        print("The contributors_enabled is : " + str(user.contributors_enabled))
        print("The is_translator is : " + str(user.is_translator))
        print("The is_translation_enabled is : " + str(user.is_translation_enabled))

        print("The profile_background_color is : " + user.profile_background_color)
        print("The profile_background_image_url is : " + user.profile_background_image_url)
        print("The profile_background_image_url_https is : " + user.profile_background_image_url_https)
        print("The profile_background_tile is : " + str(user.profile_background_tile))
        print("The profile_image_url is : " + user.profile_image_url)
        print("The profile_image_url_https is : " + user.profile_image_url_https)
        print("The profile_banner_url is : " + user.profile_banner_url)
        print("The profile_link_color is : " + user.profile_link_color)
        print("The profile_sidebar_border_color is : " + user.profile_sidebar_border_color)
        print("The profile_sidebar_fill_color is : " + user.profile_sidebar_fill_color)
        print("The profile_text_color is : " + user.profile_text_color)
        print("The profile_use_background_image is : " + str(user.profile_use_background_image))

        print("The has_extended_profile is : " + str(user.has_extended_profile))
        print("The default_profile is : " + str(user.default_profile))
        print("The default_profile_image is : " + str(user.default_profile_image))
        print("Is the authenticated user following the account? : " + str(user.following))

        print("Has the authenticated user requested to follow the account? : " + str(user.follow_request_sent))
        print("Are notifications of the authenticated user turned on for the account? : " + str(user.notifications))
        return user

    def user_report(self, screen_name):
        user = self.api.get_user(screen_name=screen_name)
        # Get user Twitter statistics
        print(f"user.followers_count: {user.followers_count}")
        print(f"user.listed_count: {user.listed_count}")
        print(f"user.statuses_count: {user.statuses_count}")
        # Show followers
        for follower in user.followers():
            print('Follower {0} is User {1}'.format(str(follower.name), str(follower.screen_name)))
        return user

    def follow(self, user_to_follow_name):
        self.api.create_friendship(user_to_follow_name)

    def get_tweets(self, user_to_query, count=10):
        return self.api.user_timeline(screen_name=user_to_query.screen_name, count=count)

    def get_extended_tweets(self, user_to_query, count=10):
        return self.api.user_timeline(screen_name=user_to_query, tweet_mode="extended", count=count)

    def get_tweet_by_id(self, tweet_id):
        return self.api.get_status(tweet_id)

    def like(self, tweet):
        return self.api.create_favorite(id=tweet.id)

    def unlike(self, tweet):
        return self.api.destroy_favorite(id=tweet.id)

    def retweet_status(self, tweet):
        return self.api.retweet(id=tweet.id)

    # status is able to be text or include variables similar to format prints.
    # see: https://www.jcchouinard.com/twitter-api/#Get_Tweets_and_Understand_the_JSON_Response
    # mention = mgouker
    # link = "https://www.michaelgouker.com"
    # status = f"This is a status with a {mention} and a {link}"
    # and to quote a tweet.
    # link = f'https://twitter.com/{author}/status/{tweet_id}'
    def tweet_status(self, status):
        return self.api.update_status(status=status)

    @staticmethod
    def show_tweet(tweet):
        if tweet.text and len(tweet.text) > 0:
            print("Tweet Id: {0}, {1}".format(tweet.id, tweet.text))
        else:
            print("Tweet id: {0".format(tweet.id))


def main():
    twitter = TwitterAccess()
    twitter.login()
    if twitter.is_available():
        user_to_query = TEST_USER2
        user = twitter.user_report(user_to_query)
        tweets = twitter.get_tweets(user)
        for tweet in tweets:
            twitter.show_tweet(tweet)
        tweet_id_test = input("Pick a tweet to like: ")
        tweet = twitter.get_tweet_by_id(tweet_id_test)
        twitter.like(tweet)


main()
