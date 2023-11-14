con=a.connect(host="localhost",user="root",passwd="Ro
wan@2004",database="bank")
def openAcc():
n=input("Enter Name:")
ac=input("Enter Account No: ")
db=input("Enter D.O.B: ")
p=input("Enter Phone: ")
ad=input("Enter Address: ")
ob=int(input("Enter Opening Balance: "))
data1=(n,ac,db,p,ad,ob)
data2=(n,ac,ob)
sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
sql2='insert into amount values(%s,%s,%s)'
c=con.cursor()
c.execute(sql1,data1)
c.execute(sql2,data2)
con.commit()
print("Data entered successfully")
main()
def depoAmo():
am=int(input("Enter Amount: "))
ac=input("Enter Account no: ")
a="select balance from amount where acno=%s"
data=(ac,)
c=con.cursor()
c.execute(a,data)
myresult=c.fetchone()
tam=myresult[0]+am
sql="update amount set balance=%s where acno=%s"
d=(tam,ac)
c.execute(sql,d)
con.commit()
print("Successfully deposited")
main()
def witham():
am=int(input("Enter Amount: "))
ac=input("Enter Account no: ")
a="select balance from amount where acno=%s"
data=(ac,)
c=con.cursor()
c.execute(a,data)
myresult=c.fetchone()
tam=myresult[0]-am
sql="update amount set balance=%s where acno=%s"
d=(tam,ac)
c.execute(sql,d)
con.commit()
print("Amount successfully withdrawn")
main()
def display():
ac=input("Enter account no.:")
a="select * from amount where acno = %s"
data=(ac,)
c=con.cursor()
c.execute(a,data)
myresult=c.fetchone()
for i in myresult:
print(i,end=" ")
print()
main()
def balance():
ac=input("Enter account no.:")
a="select balance from amount where acno=%s"
data=(ac,)
c=con.cursor()
c.execute(a,data)
myresult=c.fetchone()
print("Balance for account: ",ac,"is",myresult[0])
main()
def closeac():
ac=input("Enter account no.:")
sql1="delete from account where acno=%s"
sql2="delete from amount where acno=%s"
data=(ac,)
c=con.cursor()
c.execute(sql1,data)
c.execute(sql2,data)
con.commit()
print("Account successfully closed")
main()
def main():
print("""
********WELCOME TO DUTCH BANK**********
PLEASE CHOOSE AMONG THE FOLLOWING OPTIONS:
1.OPEN NEW ACCOUNT
2.DEPOSIT AMOUNT
3.WITHDRAW AMOUNT
4.BALANCE ENQUIRY
5.DISPLAY CUSTOMER DETAILS
6.CLOSE AN ACCOUNT
""")
choice=input("Enter task no: ")
if(choice=='1'):
openAcc()
elif(choice=='2'):
depoAmo()
elif(choice=='3'):
witham()
elif(choice=='4'):
balance()
elif(choice=='5'):
display()
elif(choice=='6'):
closeac()
else:
print("Wrong choice.....")
main()