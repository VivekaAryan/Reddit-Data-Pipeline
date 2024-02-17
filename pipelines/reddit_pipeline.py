import pandas as pd

from etls.reddit_etl import connect_reddit, extract_posts
from utils.constants import CLIENT_ID, SECRET

def reddit_pipeline(file_name: str, subreddit: str, time_filter = 'day', limit = None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    
    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    # transformation
    post_df = transform_data(post_df)
    # loading to csv
