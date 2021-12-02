import psycopg2
import sqlalchemy
import sqlalchemy

#connect to the db
con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "ramamunagala",
            password = "hell")

#cursor
cur = con.cursor()



#execute query
cur.execute("select staff_id, first_name from staff")

rows = cur.fetchall()

for r in rows:
    print (f"id {r[0]} name {r[1]}")


#commit the transcation
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()