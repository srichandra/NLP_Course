# write a python program to find len of list 
list1=[1,2,3,4,5,6,7]
print(f'length of list is {len(list1)}')

# write a python program to find len of dict
dct={'a':1,'b':2,'c':3}
print(f'length of dictionary is {len(dct)}')


# write a python program to find len of tuple 
tuple1 = ("apple", "banana", "cherry")
print(f'length of tuple is {len(tuple1)}')

# write a python program to round a number to integer 
a=1.7
print(f'rounded integer is {round(a)}')

# write a python to check if a number if even or odd
a=3
if(a%2==0):
	print(f'The number is even')
else:
	print(f'The number is odd')

# write a python to print square root of a number
num = 8 
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

# write a python to print a square of a number
a=3
print(f'square of given number is {a**2}')

# write a python to print a cube of a number
a=3
print(f'square of given number is {a*a*a}')

# write a program to find and print the largest among two numbers
num1 = 10
num2 = 12
if (num1 >= num2):
	print(f'largest:{num1}')
else:
   print(f'largest:{num2}')

# write a program to swap two variables
x = 5
y = 10
temp = x
x = y
y = temp
print(f'The value of x after swapping: {x}')
print(f'The value of y after swapping: {y}')

# write a program to convert kilometers to miles
kilometers = 2
conv_fac = 0.621371
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

# write a program to find the area of triangle
a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

# write a program to find the semi-perimeter of triangle
a = 5
b = 6
c = 7
s = (a + b + c) / 2
print('The semi-perimeter of the triangle is %0.2f' %s)

# write a program to convert temperature in celsius to fahrenheit
celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

#write a program to check if year is a leap year or not
year = 2000
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#write a program tcheck if a number is prime or not
num = 407
if num > 1:
  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")

#write a program to find the factorial of a number
num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


#write a program to check if the number is an Armstrong number or not
num = 100
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


#write a program to find sum of natural numbers up to num

num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

#write a programto convert decimal into binary number systems
dec = 344
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")

#write a programto convert decimal into octal number systems
dec = 344
print("The decimal value of", dec, "is:")
print(oct(dec), "in octal.")

#write a program to convert decimal into hexadecimal number systems
dec = 344
print("The decimal value of", dec, "is:")
print(hex(dec), "in hexadecimal.")


#write a program to find the ASCII value of the given character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


#write a function  to find H.C.F of two numbers
def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf




#write a function to find the L.C.M. of two input number
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm



#write a function to find the factors of a number

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

#write a program to add two matrices 
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)


#write a program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]


for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


#write a program to check if a string is palindrome or not

my_str = 'aIbohPhoBiA'

my_str = my_str.casefold()

rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


#write a program to remove punctuations from a string

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)


#write a program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
   print(word)


#write a program to  perform union operation on sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};
print("Union of E and N is",E | N)

#write a program to  perform intersection operation on sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};
print("Intersection of E and N is",E & N)

#write a program to  perform difference operation on sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};
print("Difference of E and N is",E - N)

#write a program to  perform ymmetric difference operation on sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};
print("Symmetric difference of E and N is",E ^ N)

#write a program to count the number of each vowels
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?'
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)


#write a function to find sum of cubes of first n natural numbers 
def sumOfSeries(n): 
    sum = 0
    for i in range(1, n+1): 
        sum +=i*i*i  
    return sum

#write a function to find nth Fibonacci number   
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 


#write a function to find position of n'th multiple of a mumber k in Fibonacci Series  
def findPosition(k, n): 
    f1 = 0
    f2 = 1
    i =2;  
    while i!=0: 
        f3 = f1 + f2; 
        f1 = f2; 
        f2 = f3; 
        if f2%k == 0: 
            return n*i 
        i+=1    
    return

#write a function to find maximum in arr[] of size n 
def largest(arr,n): 
   
    max = arr[0] 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max

#write a function to check if given array is Monotonic 
def isMonotonic(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 


#write a function to swap first and last element of a list   
def swapList(newList): 
    size = len(newList)  
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp    
    return newList 


#write a program to find sum of a list
list1 = [11, 5, 17, 18, 23] 
total=0
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)

#write a function to multiply all values in the list
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x 
    return result 

#write a program to find smallest number in a list   
list1 = [10, 20, 4, 45, 99] 
list1.sort() 
print("Smallest element is:", *list1[:1]) 

#write a program to find largest number in a list   
list1 = [10, 20, 4, 45, 99] 
list1.sort() 
print("Largest element is:", list1[-1]) 

#write a function to find N largest elements from given list of integers 
  
def Nmaxelements(list1, N): 
    final_list = [] 
    for i in range(0, N):  
        max1 = 0      
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1)          
    print(final_list) 


#write a program to print Even Numbers in a List 
list1 = [10, 21, 4, 45, 66, 93] 
for num in list1: 
    if num % 2 == 0: 
       print(num, end = " ") 

#write a program to print odd Numbers in a List 
list1 = [10, 21, 4, 45, 66, 93] 
for num in list1: 
    if num % 2 != 0: 
       print(num, end = " ") 

#write a program to print negative Numbers in a List 
list1 = [11, -21, 0, 45, 66, -93] 
for num in list1: 
    if num < 0: 
       print(num, end = " ") 

#write a program to print positive Numbers in a List 
list1 = [11, -21, 0, 45, 66, -93] 
for num in list1: 
    if num >= 0: 
       print(num, end = " ") 

#write a program to print positive Numbers in given range   
start, end = -4, 19
for num in range(start, end + 1): 
    if num >= 0: 
        print(num, end = " ") 

#write a program to print negative Numbers in given range   
start, end = -4, 19
for num in range(start, end + 1): 
    if num < 0: 
        print(num, end = " ") 

#write a program to print Even Numbers in given range  
start, end = 4, 19
for num in range(start, end + 1): 
    if num % 2 == 0: 
        print(num, end = " ")

#write a program to print odd Numbers in given range 
start, end = 4, 19
for num in range(start, end + 1): 
    if num % 2 != 0: 
        print(num, end = " ") 

#write a program to remove multiple elements from a list  
list1 = [11, 5, 17, 18, 23, 50]   
for ele in list1: 
    if ele % 2 == 0: 
        list1.remove(ele) 
print("New list after removing all even numbers: ", list1) 

#write a function to find sum of  all items in a Dictionary 
def returnSum(myDict):     
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i]    
    return sum

#write a program to convert tuple into dictionary   
def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 