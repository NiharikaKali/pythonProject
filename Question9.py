import math
Students = int(input("Enter the count of students:"))
weights=[]
weights1=[]
for i in range(Students):
    weights.append(int(input()))
for j in weights:
    a=(math.floor((j/2.2046) * 100 ) )/ 100;
    weights1.append(a)
print("Weights in Kilograms", weights1)