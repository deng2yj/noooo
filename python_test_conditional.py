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












