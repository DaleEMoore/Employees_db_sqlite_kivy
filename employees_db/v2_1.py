import random
import sys
import datetime
import sqlite3

class Employee():
    def __init__(self, FName='', LName='', Age=0, Position='', Address='', Salary=''):
        self.FName = FName
        self.LName = LName
        self.Age = Age
        self.Position = Position
        self.Address = Address
        self.Salary = Salary

    def show_employee(self):
        print("{} {}  {}  ".format(self.FName,self.LName,self.Age))
        print("{}  {}  ".format(self.Position,self.Address))
        print("{}zl".format(self.Salary))



class Database():

    def __init__(self,database_name):
        self.db_conn = sqlite3.connect("{}.db".format(database_name))

        print("Database created")

        self.db_conn.execute("DROP TABLE IF EXISTS Employees")
        self.db_conn.commit()
        try:
            self.db_conn.execute(
                "CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, "
                "Age INTEGER NOT NULL, Address TEXT, Salary REAL, Position TEXT);")
            self.db_conn.commit()
            print("Table created")
        except sqlite3.OperationalError:
            print("Table couldn't be created!")


    def add_employee(self):
        try:
            employee = Employee()
            employee.FName=input("Enter first name: ")
            employee.LName=input("Enter last name: ")
            employee.Age=int(input("Enter age: "))
            employee.Address=input("Enter address: ")
            employee.Salary=input("Enter salary: ")
            employee.Position=input("Enter position: ")

            self.db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, Position) VALUES (?, ?, ?, ?, ?, ?)",
                                 (employee.FName, employee.LName, employee.Age, employee.Address, employee.Salary, employee.Position))
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("Employee can not be added")

    def delete_employee(self, ID):
        try:
            self.db_conn.execute("DELETE FROM Employees WHERE ID=?", (ID, ))
            self.db_conn.commit()
            print("Employee deleted")

        except sqlite3.OperationalError:
            print("Data couldn't be Deleted")

    def show_employees(self):
        try:
            theCursor = self.db_conn.cursor()
            result = theCursor.execute("SELECT ID, FName, LName, Age, Address, Salary, Position FROM Employees")
            for row in result:
                print("ID : ", row[0])
                print("FName : {}".format(row[1]),)
                print("LName : ", row[2])
                print("Age : ", row[3],)
                print("Address : ", row[4])
                print("Salary : ", row[5],"zl",)
                print("Position : ", row[6])

        except sqlite3.OperationalError:
            print("Table doesn't exist")
        except:
            print("Couldn't retrieve data from database")

    def show_ID(self):
        try:
            with self.db_conn:
                self.db_conn.row_factory = sqlite3.Row
                theCursor = self.db_conn.cursor()
                theCursor.execute("SELECT * FROM Employees")
                rows = theCursor.fetchall()
                i =1
                for row in rows:
                    print("{}: {} {}".format(i, row["FName"], row["LName"]))
                    i+=1
        except sqlite3.OperationalError:
            print("Data cant't be opened!")

    def get_version(self):
        theCursor = self.db_conn.cursor()
        theCursor.execute("SELECT SQLITE_VERSION()")
        print("SQLite Version: ", theCursor.fetchone())

    def close_database(self):
        print("Database closed")
        self.db_conn.close()








def main():
    d = Database("test")
    d.add_employee()
    d.show_ID()
    d.delete_employee(1)
    d.close_database()




main()

