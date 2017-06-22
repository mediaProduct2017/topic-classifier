"""
This module does test for db_connect.py. 
"""

from db_connect import db, cur

cur.execute("select * from test")

print cur.fetchall()

cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false")

print cur.fetchall()

query = ("create table from_script ("
         "name text, "
         "species text)")

print query

# cur.execute(query)

cur.execute("select * from from_script")

print cur.fetchall()

# cur.execute("insert into test values('sheep', 'grass')")

# cur.execute(r'\dt')
# not feasible

# cur.execute("create database from_mypsql")
# undoable from script

# db.commit()
cur.close()
db.close()
