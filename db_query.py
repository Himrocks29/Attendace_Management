import sqlite3 as lite
import datetime

con = lite.connect('Attendance.db')
cur = con.cursor()
t = datetime.datetime.now()

def tb_query(cl):
    hr = {'9':'I','10':'II','11':'III','12':'IV','1':'V','2':'VI','3':'VII'}
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = datetime.datetime.today().weekday()
    print(days[day])
    cur.execute('SELECT "{}"'.format(hr[cl])+'FROM "TIME_TABLE" WHERE Day = "{}"'.format(days[day]))
    pd = cur.fetchone()[0]
    print("Class: {}".format(pd))
    return [pd]


def attendance(names, period):
    t1 = datetime.datetime.today().date()
    #print(t1)
    print(period)
    reg_no = []
    name_f = []
    for name in names:
        cur.execute("SELECT Rollno FROM STUDENT WHERE Name = '{}'".format(name))
        reg = cur.fetchone()[0]
        reg_no.append(reg)
        name_f.append(name)
    print("in attendance: {}".format(period))
    cur.execute("INSERT INTO SE VALUES('2020-05-27', 201700388, 'KUMAR SATYAM', 'P')")
    '''for i in range(0,len(reg)):
        print("Name: {}\tReg No.: {}".format(name_f[i], reg_no[i]))
        cur.execute("INSERT INTO {} VALUES('{}',{},'{}','P')".format(period,t1,reg[i],name_f[i]))
'''


cl = input("Enter class time: \n")
names = ['KUMAR SATYAM','Himanshu Sharma', 'Prit Pradhan']
pr = tb_query(cl)
val = pr[0]
attendance(names, val)
