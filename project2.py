#couning values
all_nums=[]
f = open ("COSC450_P1_Data.txt", "r")
num = 0
for line in f.read().split():
    num += 1
    all_nums.append(line)

f.close()
firstArr =[]
aLenght = int(num/5)
print(aLenght)

f = open ("COSC450_P1_Data.txt", "r")
for line in f.read().split():
  for i in range(1,5):
    for j in range(1,aLenght):
        firstArr[i][j]=line
f.close()
print(firstArr)







