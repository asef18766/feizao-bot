from os import getenv
import psycopg2

DATABASE_URL = getenv("DATABASE_URL" , "error")
conn:psycopg2.extensions.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True
cursor:psycopg2.extensions.cursor = conn.cursor()
