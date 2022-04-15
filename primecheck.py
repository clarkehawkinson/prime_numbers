#This code is meant to find all the prime numbers between 1 and n.
import math
import csv
import numpy as np
import time

tic = time.time()
toc = time.time()

list = []     #array for the prime numbers
n = 10**5     ##Number to check up to
mid = int(math.sqrt(n)+1)    #Optimizing the division part of the search, Look into sqrt(n)+1
tic
for y in range(1,n,2):     #looping through the numbers between 1 and n checking odd numbers only
    for i in range(2,mid):       #getting the numbers to divide the search by
        if y % i  == 0 and y!=i:    ##checking to see if the remainder of n/i is 0
            # print("Not prime", n, i, y) #Checking to see if it is prime or not and then printing, uncomment during debugging only
            break       #If it is divisable by anything, then go to next number
    else:
        list.append(y)
toc
print(toc-tic)   #Print the time it took to go through the loop.
space = []      #New array for the difference between the prime numbers
i = 0           #For the loop to find the difference between prime numbers
l = len(list)   #Finding length of the prime difference

for m in range(1,len(list)-1):  #looping through the primes and finding the difference between each of them individually
    sub = list[i+1]-list[i]
    space.append(sub)
    i = i+1

(gap, count) = np.unique(space,return_counts = True)    #counting the number of differences and compiling them to an array
frequency = np.asarray((gap,count)).T       #Transposing the array so it prints out easier to read, [space between, recurring time]
print(frequency)

# with open('prime.csv','w') as csvfile:   #Writing the list to a csv file
#     primewriter = csv.writer(csvfile, delimiter = ',')
#     primewriter.writerow(space)
