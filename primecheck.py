#This code is meant to find all the prime numbers between 1 and n.
n = 50       ##Number to check up to
mid = int((n+1)/2)    #Optimizing the division part of the search, Look into sqrt(n)+1

for y in range(2,n):     #looping through the numbers between 2 and n
    for i in range(2,mid):       #getting the numbers to divide the search by
        if y % i  == 0 and y!=i:    ##checking to see if the remainder of n/i is 0
            # print("Not prime", n, i, y) #Checking to see if it is prime or not and then printing, uncomment during debugging only
            break       #If it is divisable by anything, then go to next number
    else:
       print(y)     #printing the prime numbers
