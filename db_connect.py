"""
This module connects to the postgresql database on Amazon RDS. 
"""

import psycopg2
import os

import db_up
# db_up.py contains user and password of the database

dbname = 'mypsql'
host = 'mypsql.cjnyfwqsuidc.us-west-1.rds.amazonaws.com'
port = '5432'

user = os.environ["PSQL_USERNAME"]
password = os.environ["PSQL_PASSWORD"]

db = psycopg2.connect(
    database=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

cur = db.cursor()
