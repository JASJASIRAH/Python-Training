import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="jassu123",
database="python"
)
cursor = mydb.cursor()
cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("jassu", "Bangalore")
cursor.execute(sql, val)
mydb.commit()
print(cursor.rowcount, "record inserted.")
cursor.execute("SELECT * FROM customers")
myresult = cursor.fetchall()
print(myresult)
print("Name | Address")
for x in myresult:
    print(x[0] +" | " + x[1])
    print(type(x))
mydb.close()

