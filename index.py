from tkinter import *
from tkinter.messagebox import showinfo
import mysql.connector
import time
import random

class Main():
    def __init__(self):
        self.root = Tk()
        self.root.title('Automated Teller Machine')
        # self.root.iconbitmap("icons8_Python.ico")
        self.mainFrame = Frame(self.root, bg='blue', width=500, height=500)
        self.mainFrame.grid()
        self.root.geometry('500x500')
        self.sex = StringVar()
        self.connection()
        self.indexPage()

        self.root.mainloop()


    def connection(self):
        self.mycon = mysql.connector.connect(database='bank', passwd='', user='root')
        self.mycursor = self.mycon.cursor()

    def indexPage(self):
        self.frame1 = Frame(self.mainFrame, bg='blue', width=500, height=500)
        self.frame1.grid()
        Label(self.frame1, bg='blue', text='Welcome to Python Bank\nPlease proceed...', fg='yellow').place(relx=0.5, rely=0.4, anchor='center')
        Button(self.frame1, text='Register', bg='yellow', fg='blue', command=self.register).place(relx=0.435, rely=0.54)
        Button(self.frame1, text='Login', bg='yellow', fg='blue', command=self.login).place(relx=0.45, rely=0.45)
        

    def login(self):
        # self.frame1.destroy()
        self.newFrame = Toplevel(bg='blue')
        Label(self.newFrame, bg='blue', text='Please enter your account number here:').grid(row=0, column=0)
        self.acNo = Entry(self.newFrame, bg='blue', fg='yellow')
        self.acNo.grid(row=0, column=1)
        # Label(self.newFrame,bg='blue', text='Please provide your pin here:').grid(row=1, column=0)
        # self.pn = Entry(self.newFrame, bg='blue', fg='yellow')
        # self.pn.grid(row=1, column=1)
        Button(self.newFrame, bg='yellow', fg='blue', text='Login', command=self.log).grid(row=2, columnspan=2)

    def log(self):
        self.accNo = self.acNo.get()
        # self.pin = self.pn.get()
        query = 'SELECT * FROM customers WHERE Account_Number = %s'
        val = (self.accNo,)
        check = (query, val)
        self.mycursor.execute(query, val)
        self.record = self.mycursor.fetchall()
        if self.record:
            self.logged()
        else:
            showinfo("Wrong Account Number", "Please enter the correct details")
            self.log()

    def logged(self):
        self.newFrame.destroy()
        self.frame1.destroy()
        self._new_ = Frame(self.mainFrame, bg='blue', width=500, height=500)
        self._new_.pack()
        self.b1 = Button(self._new_, bg='blue', text='>>>', width=10, height=4)
        self.b1.grid(row=0, column=0)
        self.b2 = Button(self._new_, bg='blue', text='>>>', width=10, height=4)
        self.b2.grid(row=1, column=0)
        self.b3 = Button(self._new_, bg='blue', text='>>>', width=10, height=4)
        self.b3.grid(row=2, column=0)
        self.b4 = Button(self._new_, bg='blue', text='>>>', width=10, height=4)
        self.b4.grid(row=3, column=0)

        self.big = Text(self._new_, bg='blue', fg='yellow', font=(22), width=36, height=17)
        self.big.grid(row=0, rowspan=4, column=1,columnspan=4)

        self.b5 = Button(self._new_, bg='blue', text='>>>', width=10, height=4)
        self.b5.grid(row=0, column=5)
        self.b6 = Button(self._new_, bg='blue', text='>>>', width=10, height=4)
        self.b6.grid(row=1, column=5)
        self.b7 = Button(self._new_, bg='blue', text='>>>', width=10, height=4)
        self.b7.grid(row=2, column=5)
        self.b8 = Button(self._new_, bg='blue', text='>>>', width=10, height=4)
        self.b8.grid(row=3, column=5)

        self.small = Entry(self._new_, bg='blue', fg='yellow', show='*', borderwidth=0, text="")
        self.small.grid(row=4, column=2, columnspan=3, ipady=5)

        Button(self._new_, bg='yellow', text='9', width=6, height=2, command=lambda:self.writeText("9")).grid(row=5, column=1)
        Button(self._new_, bg='yellow', text='8', width=6, height=2, command=lambda:self.writeText("8")).grid(row=5, column=2)
        Button(self._new_, bg='yellow', text='7', width=6, height=2, command=lambda:self.writeText("7")).grid(row=5, column=3)
        Button(self._new_, bg='red', text='Cancel', width=6, height=2).grid(row=5, column=4)

        Button(self._new_, bg='yellow', text='6', width=6, height=2, command=lambda:self.writeText("6")).grid(row=6, column=1)
        Button(self._new_, bg='yellow', text='5', width=6, height=2, command=lambda:self.writeText("5")).grid(row=6, column=2)
        Button(self._new_, bg='yellow', text='4', width=6, height=2, command=lambda:self.writeText("4")).grid(row=6, column=3)
        Button(self._new_, bg='orange', text='Delete', width=6, height=2).grid(row=6, column=4)

        Button(self._new_, bg='yellow', text='3', width=6, height=2, command=lambda:self.writeText("3")).grid(row=7, column=1)
        Button(self._new_, bg='yellow', text='2', width=6, height=2, command=lambda:self.writeText("2")).grid(row=7, column=2)
        Button(self._new_, bg='yellow', text='1', width=6, height=2, command=lambda:self.writeText("1")).grid(row=7, column=3)
        Button(self._new_, bg='yellow', text='0', width=6, height=2, command=lambda:self.writeText("0")).grid(row=7, column=4)
        self.proceed = Button(self._new_, bg='green', text='Proceed', width=8, height=2, command=lambda: self.tryLog())
        self.proceed.grid(row=8, column=2, columnspan=2)

    def tryLog(self):
        userPin = self.small.get()
        query = 'SELECT * FROM customers WHERE Account_Number = %s AND Account_Pin = %s'
        val = (self.accNo, userPin)
        check = (query, val)
        self.mycursor.execute(query, val)
        self.record = self.mycursor.fetchall()
        if self.record:
            self.transact()
        else:
            showinfo("Wrong Pin", "Please enter the correct pin")
            self.log()

    def transact(self):
        # print(self.record)
        self.small.delete(0, END)
        self.big.insert(0.0, "Welcome, Dear {}".format(self.record[0][1]))
        self.b1.config(text='Change Pin', command=self.changePin)
        self.b5.config(text='Pay Bill', command=self.pay_bill)
        self.b6.config(text='Deposit', command=self.deposit)
        self.b7.config(text='Withdraw', command=self.withdraw)
        self.b8.config(text='Transfer', command=self.transfer)

    def changePin(self):
        pass

    def transfer(self):
        self.big.delete(0.0, END)
        self.big.insert(0.0, "Enter Reciever's account Number")
        self.proceed.config(command=self.validateNumber)
        # self.small.config(show='p')

    def validateNumber(self):
        pass

    def withdraw(self):
        pass

    def deposit(self):
        self.big.delete(0.0, END)
        self.big.insert(0.0, "How much do you want to deposit")
        self.b1.config(text='500', command=lambda:addMoney(500))
        self.b2.config(text='1000', command=lambda:addMoney(1000))
        self.b3.config(text='2000', command=lambda:addMoney(2000))
        self.b4.config(text="5000", command=lambda:addMoney(5000))
        self.b5.config(text="10000", command=lambda:addMoney(10000))
        self.b6.config(text="20000", command=lambda:addMoney(20000))
        self.b7.config(text="Others", command=lambda:addMoney(self.newSmall.get()))
        self.newSmall = Entry(self._new_, bg='blue', fg='yellow', borderwidth=0, text="")
        self.small.grid(row=4, column=2, columnspan=3, ipady=5)

    def writeTextAgain(self, txt):
        onSCreen = self.newSmall.get()
        self.newSmall.delete(0, END)
        self.newSmall.insert(0, onSCreen + txt)

    def addMoney(self, amount):
        userBal = self.record[0][7] + amount
        query = 'UPDATE Customers SET Amount= %s WHERE Account_Number = %s'
        val = (userBal, self.record[0][0])
        mycursor.execute(query, val)
        mycon.commit()
        self.root.after(2)
        showinfo("Success", "You have successfully deposited {} and your new account balance is {}".format(amount, userBal))

    def pay_bill(self):
        pass


    def writeText(self, txt):
        onSCreen = self.small.get()
        self.small.delete(0, END)
        self.small.insert(0, onSCreen + txt)

    def register(self):
        self.newFrame = Toplevel(bg='blue')
        self.newFrame.title('Register')
        Label(self.newFrame, text='First Name', fg='white', bg='blue').grid(row=0, column=0)
        self.fName = Entry(self.newFrame, bg='blue', fg='yellow', width=30)
        self.fName.grid(row=0, column=1)
        Label(self.newFrame, text='Last Name', fg='white', bg='blue').grid(row=1, column=0)
        self.lName = Entry(self.newFrame, bg='blue', fg='yellow', width=30)
        self.lName.grid(row=1, column=1)
        Radiobutton(self.newFrame, bg='blue', fg='black', text='Male', variable=self.sex, value='Male', tristatevalue=0).grid(row=2, column=0)
        Radiobutton(self.newFrame, bg='blue', fg='black', text='Female', variable=self.sex, value='Female', tristatevalue=0).grid(row=2, column=1)
        Label(self.newFrame, text='Phone Number', fg='white', bg='blue').grid(row=3, column=0)
        self.phoneNum = Entry(self.newFrame, fg='yellow', bg='blue', width=30)
        self.phoneNum.grid(row=3, column=1)
        Label(self.newFrame, text='Home Address', fg='white', bg='blue').grid(row=4, column=0)
        self.address = Entry(self.newFrame, fg='yellow', bg='blue', width=30)
        self.address.grid(row=4, column=1)
        Label(self.newFrame, text='Pin', fg='white', bg='blue').grid(row=5, column=0)
        self.pin = Entry(self.newFrame, fg='yellow', bg='blue', width=30)
        self.pin.grid(row=5, column=1)
        Button(self.newFrame, text='Submit', fg='blue', bg='yellow', command=self.reg).grid(row=6, columnspan=2)

    def reg(self):
        self.accountNo = self.acctNo()
        self.amount = 0
        # print(self.accountNo)
        self.query = 'INSERT INTO customers(Account_Number, First_Name, Last_Name, Sex, Phone_Number, Address, Account_Pin, Amount) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        self.val = (self.accountNo, self.fName.get(), self.lName.get(), self.sex.get(), self.phoneNum.get(), self.address.get(), self.pin.get(), self.amount)
        self.mycursor.execute(self.query, self.val)
        self.mycon.commit()
        self.newFrame.destroy()
        

    def acctNo(self):
        a = random.randint(1000000,9000000)
        b  = "101" + str(a)
        checkQuery = 'SELECT * FROM Customers WHERE Account_Number=%s'
        checkVal = (b,)
        self.mycursor.execute(checkQuery, checkVal)
        found = self.mycursor.fetchall()
        if found:
            self.acctNo()
        # print(b)
        return b


Main()