import time
Timestamp = int(time.strftime("%H"))
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if(4<=Timestamp<12):
    print("Good Morning Sir, its", timestamp)
elif(12>=Timestamp<17):
    print("Good Afternoon Sir, its", timestamp)
else:
    print("Good Evening Sir, its", timestamp)