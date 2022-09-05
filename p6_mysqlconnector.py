import mysql.connector as mysql

mydb = mysql.connect(host="localhost",user="vinay",passwd="mysql")

mycur = mydb.cursor()

mycur.execute("select * from vinaydb.student")
# for i in mycur:
#     print(i)

print("#-------------------------------#")

result = mycur.fetchall()
for i in result:
    print(i)

print('#--------------------------------------#')
mycur1 = mydb.cursor()
mycur1.execute("select * from vinaydb.student")
result = mycur1.fetchone()
print(result)

print("#-----------------------------------#")
for i in result:
    print(i)



