import sqlite3 

conn=sqlite3.connect('requests.db')
cursor=conn.cursor()

#Create table to store requests for new reuqests/non existant 
cursor.execute('''CREATE TABLE IF NOT EXISTS requests
             (request_ID INTEGER PRIMARY KEY,
              resident_Name TEXT,
              unit_num TEXT,
              description TEXT,
              priority TEXT,
              date TEXT,
              status TEXT)''')

conn.commit()

#Loop through to select from entire database and print the request 
def loop_through(cursor):
    cursor.execute("SELECT * FROM requests")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Request ID: {row[0]}, Resident Name: {row[1]}, Unit Number: {row[2]}, Description: {row[3]}, Priority: {row[4]}, Date: {row[5]}, Status: {row[6]}")


from request import request

r1 = request(1, "John Smith", 101, "Leak in kitchen", "High", "2026-06-23", "Open")

from functions import add_request

add_request(cursor, conn, r1)

from functions import view_requests

view_requests(cursor)

from functions import update_status

update_status(cursor, conn, 1, "Completed")