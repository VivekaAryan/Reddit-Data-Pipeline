import praw
from praw import Reddit
import sys

from utils.constants import POST_FIELDS

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    # Initiallization
    try:
        reddit = praw.Reddit(client_id = client_id,
                             client_secret = client_secret,
                             user_agent = user_agent)
        print("Connected to Reddit!")
        return reddit
    
    except Exception as e:
        print(e)
        sys.exit(1) # Exit if the reddit connection cannot be established

def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)

    # extract a list of posts in an array
    posts = subreddit.top(time_filter=time_filter, limit=limit)
    
    posts_lists = []

    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POST_FIELDS}
        posts_lists.append(post)

    return posts_lists

def transform_data(post_df: pd.DataFrame):
    post_df['created_utc'] = pd.datatime()
