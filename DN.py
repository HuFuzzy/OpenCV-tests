import pyodbc
server = 'localhost\sqlexpress'
database = 'teste'
username = 'sa'
password = 'nimp2017'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()

while row:
    print (row[0])
    row = cursor.fetchone()




for row in cursor:
    print('row = %r' % (row,))

for x in range (0,20):
    cursor.execute(("""INSERT INTO tabela(teste)VALUES (?)"""),x)



cnxn.commit()

