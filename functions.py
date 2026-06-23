
#Functions utilizing sql to add, view, as well as update status of requests 

def add_request(cursor, conn, request):
    query = """
    INSERT INTO requests
    (resident_Name, unit_num, description, priority, date, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    cursor.execute(query, (
        request.resident_Name,
        request.unit_num,
        request.description,
        request.priority,
        request.date,
        request.status
    ))

    conn.commit()
    
def view_requests(cursor):
    cursor.execute("SELECT * FROM requests")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def update_status(cursor, conn, request_ID, updated_status):
    query = """
    UPDATE requests
    SET status = ?
    WHERE request_ID = ?
    """
    cursor.execute(query, (updated_status, request_ID))
    conn.commit()