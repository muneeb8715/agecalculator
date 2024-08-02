def Agecalculator(yb,mb,db):
    import datetime
    today=datetime.datetime.now().date()
    dob=datetime.date(yb,mb,db)
    age=int((today-dob).days/365.25)
    print(age)


yr=int(input("Enter Year if Birth : "))
mon=int(input("Enter Month of Year : "))
date=int(input("Enter date of Birth : "))

Agecalculator(1999,3,14)