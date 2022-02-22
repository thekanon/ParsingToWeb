import time
import datetime
f = open('house.txt', mode='rt', encoding='utf-8')
data = "===\n"
while True:
    currentLine = f.readline()
    if currentLine.find("===") != -1 :
        print(data[0:-1])
        data="\n"
        time.sleep(3)
    else:
        data+=currentLine
        
