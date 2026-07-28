#!/usr/bin/python3

#modulo 3 show Fizz and not number 
#modulo 5 show Buzz
#modulo 3 et 5 show FizzBuzz
#last = abs(number) % 10
#for x in range(97, 123):
#    if x != 113 and x != 101:

def fizzbuzz():
	for i in range(1, 101):
		if i % 15 == 0:
			print("FizzBuzz", end=" ")
		elif i % 5 == 0:
			print("Buzz", end=" ")
		elif i % 3 == 0:
			print("Fizz", end=" ")
		else:
			print(i, end=" ")



#for i in range(1, 101):
#    print("{:02d}".format(i), end=", ")
#print("{:02d}".format(99))

