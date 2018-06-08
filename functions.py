
def wages():
    
    Hoursworkedinweek = float(hoursworked.get())
    wageperhour = float(hourlyrate.get())
    pay = wageperhour * Hoursworkedinweek
    paydue = "$" ,str('%.2f' %(pay))
    payable.set(paydue)
    
    taxa = pay*0.2
    Taxable = "$" ,str('%.2f' %(taxa))
    tax.set(Taxable)
    
    netpaya = pay - taxa
    Netpays = "$" ,str('%.2f' %(netpaya))
    netpay.set(Netpays)
    
    if Hoursworkedinweek> 40:
        overtimehours = (Hoursworkedinweek - 40) + wageperhour *1.5
        overtimeh = "$" ,str('%.2f' %(overtimehours))
        overtime.set(overtimeh)
        
    elif Hoursworkedinweek<40:
        overtimepay = (Hoursworkedinweek-40) + wageperhour *1.5
        overtimeh = "$", str('%.2f' %(overtimepay))
        overtime.set(overtimeh)
    return

def exit():
    qexit = messagebox.askyesno("Salary management system", "Do you want to exit?")
    if qexit > 0:
        root.destroy()
    return

def Reset():
    Name.set("")
    Address.set("")
    Employer.set("")
    Ninumber.set("")
    hoursworked.set("")
    hourlyrate.set("")
    tax.set("")
    overtime.set("")
    grosspay.set("")
    netpay.set("")
    payable.set("")
    txtsalary.delete("1.0",END)
    return
    
def info():
    txtsalary.insert(END,"\t\tSalary\n\n")
    txtsalary.insert(END,"Name: \t\t" + Name.get() + "\n\n")
    txtsalary.insert(END,"Address: \t\t" + Address.get() + "\n\n")
    txtsalary.insert(END,"Employer: \t\t" + Employer.get() + "\n\n")
    txtsalary.insert(END,"Ninumber: \t\t" + Ninumber.get() + "\n\n")
    txtsalary.insert(END,"Hours Worked: \t\t" + hoursworked.get() + "\n\n")
    txtsalary.insert(END,"NET PAY\t\t" + netpay.get() + "\n\n")
    txtsalary.insert(END,"Hourly Rate\t\t" + hourlyrate.get() +"\n\n")
    txtsalary.insert(END,"Tax Payable: \t\t" + tax.get() + "\n\n")
    txtsalary.insert(END,"Payable \t\t" + payable.get() + "\n\n")
    return

