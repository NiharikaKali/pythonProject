it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#printing the length of it_companies

length_of_it_companies = len(it_companies)
print("Length of the it_companies list", length_of_it_companies)

#adding twitter to the companies

extra = "Twitter"
final_list = list(it_companies)
final_list.append(extra)
print("appended list with twitter", final_list)

#Inserting multiple IT companies at once

multiple_companies= ["Goldman_Sachs", "JP_Morgan", "Flipkart", "Siemens"]
it_companies.update(multiple_companies)
print("List after Inserting multiple IT companies", it_companies)

#Removing on It company

it_companies.remove("IBM")
print(it_companies)
print("List after removing IBM", it_companies)

#What is the difference between remove and discard?
#remove: If the item which is to be removed do not exist, remove() will show an error
#discard: If the item which is to be removed do not exist, discard() will "NOT" show an error

#Join A and B

M = A.union(B)
print("List after joining A and B list", M)

#Find A intersection B

N = A.intersection(B)
print("List after Intersection of A and B", N)

#Is A subset of B

P = A.issubset(B)
print("A is a subset of B?", P)

#Are A and B disjoint sets

X = A.isdisjoint(B)
print("Are A and B disjoint sets?", X)

#Join A with B and B with A

Y = B.union(A)
print("Lists after joining A with B and B with A",M, Y)

#What is the symmetric difference between A and B

Z = A.symmetric_difference(B)
print("Symmetric difference between A and B is", Z)

#Deleting the sets completely

del A,B

#Convert the ages to a set and compare the length of the list and the set

I= set(age)
print("Converting ages to a set and compare length of list and set", len(I)==len(age))
