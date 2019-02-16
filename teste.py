import time
import datetime
a=str(datetime.datetime.now())
f = open("data_luzes.txt","a")
f.write(a)
f.write(",\n")
print(a)
