fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
Sum = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        Start_POS = line.find("0")
        End_POS = line.find(' ',Start_POS)
        Num = line[20:End_POS]
        Num = float(Num)
        Sum = Sum + Num
        count = count + 1
print("Average spam confidence:",Sum/count)
      
        
        