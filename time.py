import datetime
import time
import recognize
from time import localtime
import sys

t1 = datetime.datetime.now()


print(t1.minute)

#print(timenow.localtime)
def lt():
    while True:
        try:
            t = datetime.datetime.now()
        #if t.minute == 30:
            #t = datetime.datetime.now()
            if t.minute == 16:
            #Sleep functio for 30 minutes during class. 
                print("Half Hour Sleep Time")
                time.sleep(1800)
            elif t.minute in range(45,59):
            #Again call recognizer for exiting attendance. 
                print("Calling Recognizer")
                recognize.recognize()
            #if t.minute == 58:
                #db_query(t.hour, names [])
            elif t.minute in range(00,15):
            #Call Recofnize function for 1st 15 minutes for taking attendance. 
                print("Calling Recognizer Function")
                recognize.recognize()
            #print(t.minute)
            #print("Done Bro")
            else:
                print("Waiting.....")
                #time.sleep(10)
                print(str(t.hour)+":"+str(t.minute)+":"+str(t.second))
                return True
        except KeyboardInterrupt:
            print("Exiting Program\n")
            sys.exit(0)
#print(tr)
while True:
    lt()
