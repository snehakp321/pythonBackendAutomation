import mysql.connector
from utilities.configurations import getConnection

# host, db, user,pwd
# two db are created - APIDevelop, PythonAutomation
# conn = mysql.connector.connect(host='localhost',database='PythonAutomation',user='root',password='test@123')


conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute("select * from CustomerInfo")
row = cursor.fetchone() # fetches first/ one record- row is a tuple
print(row[3]) # will print location

# return sum of all records

rows= cursor.fetchall()
print(rows) # returns list of tuples

summation=0
for i in rows:
    summation += i[2]
print(summation)
assert summation == 261 # validation

# update
updatequery ="update customerInfo set Location = %s where CourseName = %s"
data = ("UK","Jmeter")
cursor.execute(updatequery,data) # cursor - streamline between query and db
conn.commit() # we should commit the updated value in db level using connection

#delete
deletequery="delete from customerInfo where courseName = %s"
data ="WebServices"
cursor.execute(deletequery,data)
conn.commit()

conn.close() # if not it will lead to connection memory leakage.