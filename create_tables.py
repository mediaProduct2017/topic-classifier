"""
This module creates the tables in the postgresql that will store the
data from Reddit (subreddits, submissions and comments).
"""

from db_connect import db, cur

cur.execute("""
            CREATE TABLE main_subreddits
            (
            id VARCHAR(255) NOT NULL,
            name TEXT NOT NULL,
            title TEXT NOT NULL, 
            created INT NOT NULL
            )
            """)

cur.execute("""
            CREATE TABLE main_submissions
            (
            id VARCHAR(255) NOT NULL,
            subreddit_id VARCHAR(255) NOT NULL,
            content TEXT
            )
            """)

cur.execute("""
            CREATE TABLE main_comments
            (
            id VARCHAR(255) NOT NULL,
            subreddit_id VARCHAR(255) NOT NULL,
            submission_id VARCHAR(255) NOT NULL,
            content TEXT
            )
            """)

db.commit()
cur.close()
db.close()
