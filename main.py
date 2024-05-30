import mysql.connector
from tabulate import tabulate

mysql_connection=mysql.connector.connect(
    host="localhost",
    user="<mysql-user-name>",
    password="<mysql_user_name_password>",
    database="<database-name>"
)

def select():
    responce=mysql_connection.cursor() 
    query="select * from user"
    responce.execute(query)
    all_datas=responce.fetchall() # --> all datas 
    #responce.fetchmany(2) -- straing 2 datas 
    #responce.fetchone() --> frist row data
    return tabulate(all_datas,headers=["ID","NAME","AGE","CITY"])

def insert(name,age,city):

    responce=mysql_connection.cursor()
    query="insert into user (name,age,city) values (%s,%s,%s)"
    arugument_passing_column=(name,age,city)
    responce.execute(query,arugument_passing_column)
    mysql_connection.commit()
    
    return "insert successfully".upper()

def update(name,age,city,id):

    responce=mysql_connection.cursor()
    query="update user set name=%s,age=%s,city=%s where id=%s"
    arugument_passing_column=(name,age,city,id)
    responce.execute(query,arugument_passing_column)
    mysql_connection.commit()
    
    return "update successfully".upper()


def delete(id):
    responce=mysql_connection.cursor()
    query="delete from user where id=%s"
    arugument_passing_column=(id,)
    responce.execute(query,arugument_passing_column)
    mysql_connection.commit()

    return "delete successfully".upper()

print("DATABASES CONNECTION IN MYSQL")

while True:
    print("\n1.SELECT QUERT")
    print("2.INSERT QUERY")
    print("3.UPDATE QUERY")
    print("4.DELETE QUERY\n")

    choice=input("Enter The Choice :").lower()

    if choice == "1":
        print(select())

    elif choice == "2":
        Name=input("Enter The Name :")
        Age=input("Enter The Age :")
        City=input("Enter The City :")
        print(insert(name=Name,age=Age,city=City))

    elif  choice == "3":
        ID=input("Enter The ID :")
        Name=input("Enter The Name :")
        Age=input("Enter The Age :")
        City=input("Enter The City :")
        print(update(id=ID,name=Name,city=City,age=Age))
    elif choice == "4":
        ID=input("Enter The ID :")
        print(delete(id=ID))

    elif choice in ["exit","bye","quit","0"]:
        break

    else:
        print("Invalide the choice ! You Try Agine")