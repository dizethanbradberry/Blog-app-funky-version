import psycopg2
con = psycopg2.connect(database='nidhin') 
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS blogspot")
cur.execute("CREATE TABLE blogspot(id serial,author text,post text,day text,time text,comment text)")
con.commit()
con.close()
