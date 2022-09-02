import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

# sorting the list

ages.sort()
print("list after sorting:", ages)

# Min and Max

minimum = min(ages)
maximum = max(ages)
print("Minimum value in list : " , minimum ,"     ", "Maximum value in list : " , maximum)

# Adding min and max to list

ages.append(minimum)
ages.append(maximum)
print("Adding min and max to list:", ages)

# finding the median age

st = statistics.median(ages)
print("median is :", st)

# average

s = sum(ages)
l = len(ages)
ave = s/l
print("Average of list is : ", ave)

#Range

ran = maximum - minimum
print("range of list is: ", ran)


# --------------------------- 2 --------------------------------




