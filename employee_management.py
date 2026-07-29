import mysql.connector 
conn= mysql.connector.connect(host="localhost",username="root",password="root2003",database="company_db")
cur=conn.cursor()   
print("connection created")

cur.execute("create table employee_cp(emp_id int auto_increment primary key,name varchar(30),department varchar(30),salary decimal(10,2))")
print("table created")

print("1.Add employee")
print("2.View all employee")
print("3.search employee")
print("4.update employee")
print("5.delete employee")
print("6.count employee")
print("7.exit")

while True:
    choice= int(input("enter your choice:"))
    if choice==1:
        name=input("enter the employee name:")
        department=input("enter the department name:")
        salary=input("enter the salary:")
        query="insert into employee_cp(name,department,salary) values(%s,%s,%s)"
        values=(name,department,salary)
        cur.execute(query,values)
        conn.commit()

    elif choice==2:
        cur.execute("select * from employee_cp")   
        print(cur.fetchall())

    elif choice==3:
        emp_id=int(input("enter the emp_id:"))  
        cur.execute("select * from employee_cp where emp_id=%s",(emp_id,))  
        if cur.fetchall():
            print(cur.fetchall())
        else:
            print("employee doesnot exit") 


    elif choice==4:
        emp_id=int(input("enter the employee id:"))
        cur.execute("select * from employee_cp where emp_id=%s",(emp_id,))  
        if cur.fetchall():
            department=input("enter the new department:")
            salary=int(input("enter the updated salary:"))
            query="update employee_cp set department=%s,salary=%s,where emp_id=%s"
            values=(department,salary,emp_id)
            cur.execute(query,values)
            print("employee data updated")
            conn.commit()
        else:
            print("employee doesnot exit") 

    elif choice==5:
        emp_id=int(input("enter the employee id:"))
        query="delete from employee_cp where emp_id=%s"
        values=(emp_id,)
           
