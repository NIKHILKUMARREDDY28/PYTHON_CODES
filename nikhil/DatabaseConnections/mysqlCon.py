import mysql.connector as sqc
con = sqc.connect(host="localhost",user="root",password="Matt@0302",database = "media")
cur = con.cursor()
cur.execute(""" SELECT * FROM POSTS""")
posts = cur.fetchall()
for _ in posts:
    print(_)