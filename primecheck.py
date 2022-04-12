#This code is meant to find all the prime numbers between 1 and n.
import math
import csv

list = []   #array for the prime numbers
n = 10000      ##Number to check up to
mid = int(math.sqrt(n)+1)    #Optimizing the division part of the search, Look into sqrt(n)+1

for y in range(3,n,2):     #looping through the numbers between 3 and n checking odd numbers only
    for i in range(2,mid):       #getting the numbers to divide the search by
        if y % i  == 0 and y!=i:    ##checking to see if the remainder of n/i is 0
            # print("Not prime", n, i, y) #Checking to see if it is prime or not and then printing, uncomment during debugging only
            break       #If it is divisable by anything, then go to next number
    else:
        list.append(y)
print(list)
with open('prime.csv','w',newline='') as csvfile:   #Writing the list to a csv file
    primewriter = csv.writer(csvfile, delimiter = ',')
    primewriter.writerow(list)
