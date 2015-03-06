import cx_Oracle
import getpass

user = input("User [%s]:" % getpass.getuser())
if not user:
	user = getpass.getuser()
passw = getpass.getpass("Pass:")

# open up a new connection
con = cx_Oracle.connect(user+"/"+passw+"@gwynne.cs.ualberta.ca:1521/CRS")  # lets see if this works!
# con.autocommit = 1  # un tested I think this is how to change autocommit properties

curs = con.cursor()

# old demo code

# # drop tables if they exist
# statement = "drop table movie"
# curs.execute(statement)
# 
# # create table statements
# statement = "create table movie(title char(20), movie_number integer, primary key(movie_number))"
# curs.execute(statement)
# 
# # insert data into tables
# statement = "insert into movie values('Chicago', 1)"
# curs.execute(statement)
# 
# # make a selection from the data
# query = "select title, movie_number from movie"
# curs.execute(query)
# rows = curs.fetchall()

# close connection and curs

# Drop & Create Tables
print("Dropping / Creating Tables")
f = open("p1_setup.sql.txt")
tables = f.read().replace("\n", "").split(";")
for t in tables:
	# print(t)
	if (len(t) <= 0):
		continue
	curs.execute(t)
f.close()

# Populate tables
print("Populate Tables")
f = open("population.txt")
pop = f.read().replace("\n", "").split(";")
for t in pop:
	# print(t)
	if (len(t) <= 0):
		continue
	curs.execute(t)
f.close()

curs.close()
con.close()

# print the selection
# print(rows)
