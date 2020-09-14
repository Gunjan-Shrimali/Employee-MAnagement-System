import sqlite3
#back end

def EmployeeData():
      con = sqlite3.connect("Employee.db")
      cur = con.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE(id INTEGER PRIMARY KEY,\
      Firstname text,Surname text,Address text,Gender text,Mobile text,NINumber text,\
      stdLoan text, Tax text,Pension text,Deductions text,NetPay text,GrossPay text)")
      #cursor().close()
      #cur.execute("DROP TABLE EMPLOYEE")
      con.commit()
      con.close()

def addEmployeerec(Reference,Firstname,Surname,Address,Gender,Mobile,NINumber,stdLoan,Tax,Pension,Deductions,NetPay,GrossPay):
      con = sqlite3.connect("Employee.db")
      cur = con.cursor()
      cur.execute("INSERT INTO EMPLOYEE VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",\
                  (Reference,Firstname,Surname,Address,Gender,Mobile,NINumber,stdLoan,Tax,Pension,Deductions,NetPay,GrossPay))
      #cursor().close()
      con.commit()
      con.close()

def viewData():
      con = sqlite3.connect("Employee.db")
      cur = con.cursor()
      cur.execute("SELECT * FROM Employee")
      con.close()
      return rows


def deleteRec(id):
      con = sqlite3.connect("Employee.db")
      cur = con.cursor()
      cur.execute("DELETE * FROM Employee WHERE id=?",(id))
      rows=cur.fetchall()
      con.commit()
      con.close()

def searchData(Reference ="",Firstname="",Surname="",Address="",Gender="",Mobile="",NINumber="",stdLoan="",Tax="",Pension="",Deductions="",NetPay="",GrossPay=""):
      con = sqlite3.connect("Employee.db")
      cur = con.cursor()
      cur.execute("SELECT * FROM Employee WHERE Reference=? OR Firstname=? OR Surname=? OR Address=? OR Gender=? OR Mobile=? OR NINumber=? OR stdLoan=? OR Tax=? OR Pension=? OR Deductions=? OR NetPay=? OR GrossPay=?",\
                  (Reference,Firstname,Surname,Address,Gender,Mobile,NINumber,stdLoan,Tax,Pension,Deductions,NetPay,GrossPay))
      rows=cur.fetchall()
      con.close()
      return rows

def dataUpdate(Reference ="",Firstname="",Surname="",Address="",Gender="",Mobile="",NINumber="",stdLoan="",Tax="",Pension="",Deductions="",NetPay="",GrossPay=""):
      con = sqlite3.connect("Employee.db")
      cur = con.cursor()
      cur.execute("UPDATE Employee SET Reference=?,Firstname=?, Surname=?, Address=? ,Gender=?, Mobile=?,NINumber=?,stdLoan=?, Tax=? ,Pension=? , Deductions=?, NetPay=? ,GrossPay=?",\
                  (Reference,Firstname,Surname,Address,Gender,Mobile,NINumber,stdLoan,Tax,Pension,Deductions,NetPay,GrossPay,id))
      con.commit()
      con.close()

EmployeeData()
