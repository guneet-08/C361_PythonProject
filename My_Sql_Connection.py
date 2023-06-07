import mysql.connector
#testing code
# creating a connection 
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Cohort361"
)

# creating a cursor to traverse in the connection
cursor = connection.cursor()

# let's first simply create a sample table
create_table_query = """
CREATE TABLE IF NOT EXISTS 
table_name(
id int auto_increment primary key,
column1 varchar(255),
column2 int
);
"""

# cursor.execute will simply run that query
cursor.execute(create_table_query)
print("Table Created Succesfully")

# inserting into the created table
insert_query = """
INSERT INTO table_name(column1, column2) 
VALUES(%s,%s);
"""

data = ("Value1",87)
cursor.execute(insert_query, data)

# commit the changes made in the end
connection.commit()

# selecting the data from the created table
select_query = """
SELECT * FROM table_name;
"""
cursor.execute(select_query)

rows = cursor.fetchall()

for row in rows:
    print(row)

# let's add a few more values:

data = [("Value2",99),("Value3",15),("Value4",95),("Value5",56)]
cursor.executemany(insert_query, data)

connection.commit()

# let's print now
cursor.execute(select_query)

rows = cursor.fetchall()

for row in rows:
    print(row)

# now to fianlly close the connection and release 
# the memory we have to use the following:

cursor.close()
connection.close()