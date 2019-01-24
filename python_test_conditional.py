x = 5

if x < 0:
	print("x is smaller than 0.")
elif x > 10:
	print("x is bigger than 10.")
else:
	print("x is between 0 and 10")

########
#y=int(input("enter value of y:"))
y=10
if y<0:
	print("y is small.")
elif y >= 0:
	print("y is big.")
else:
	print("error")

##########

animals = ['cat','dog','turtle','bird']

print(animals)

for x in animals:
	print(x)
	print(len(x))

#numbers = [1,2,3,4,5,6,7,8,9,10]

numbers = range(1,11)
for i in numbers:
	print(i**2)



def complicated_function():
	pass

##in R
#  complicated_function <- function(){
	
# }



def fib(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b =b, a+b
	return result

print(fib(2000))


print("\n")
print("\n")
print("\n")

a = 10/3
b = 3.3333333

if (a > b):
	print("hahaha")



print("\n")
print("\n")
print("\n")

stack=[1,2,3]

stack.append(5)

print(stack)

#stack.pop()

print(stack.pop())
print(stack.pop())
print(stack)


results = []
for i in range(10):
	results.append(i**2)

print(results)

results = list(map(lambda i:i**2, range(10)))

#lambda is the function without a name, temporary function 
#map is like apply function in R
#same as:
#def square(i):
#return i**2
print(results)

results = [i**2 for i in range(10)]
#short form of the last method
print(results)


fruit = {'apple','apple','banana','orange','pear','pinaapple','blueberry',
'peach'}
print(fruit)
#difference between the array and the set
#in the array, the sequence is remembered. while in the set, the sequence 
#does not matter. and in the set, it only record the unique identification 
#of the elements. even if you have two apples in the set, python will only 
#print one. good property to use to get rid of repeated items

tech = {'apple','blueberry'}
print(fruit-tech)








