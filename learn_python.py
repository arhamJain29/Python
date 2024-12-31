#data types
#int
120
-223

#float
12.0
-221.034

#string
'hello'
"hello"

#bool
true 1
false 0

# Output and printing
print('Hello')
print(4.9)
print('hello', 4.9, end ='\n')

# Variables
Hello = 'swati'
world = 'dhiraj'
Swati_dhiraj = 'maa paa'

# Input Command
input('Name: ')
name = input('Name: ')
age = input('Age: ')

# Print+input command
print('hello', name , 'you are', age , 'years old')

# Arithematic operators
x = 10
y = 3
result = x + y #addition
         x - y #substraction
         x * y #multiplication
         x / y #division
         x ** y #x to the power y
         x // y #return the int value only after division, like if 10 // 3, we will get 3 not 3.333----
         x % y #returns remainder

num = input('number: ') #when we take input it saves as a string
print(int(num) - 5) #to convert the actual string to integer we put int

# String methods
hello = 'hello'
print(type(hello)) #gives type here it returns <class 'str'>
print(hello.upper()) #convert the whole string in upper case 
print(hello.lower()) #convert the whole string in lower case 
print(hello.capitalize()) #convert the first letter to uppercase and also convert the rest of the string into lowercase

print(hello.count('e')) #Returns Number of times the 'e' is present in the string
print(hello.lower().count('e')) #it firsts convert the whole string in Lowercase and then counts the number of times the element is present


# Conditional Operators
x = 'hello'
y = 3
z = 'world'
print(x * y)
print(x + z)

# Comparision
== #equals to
!= #not equals to
>= #greater than equals to
<= #less than equals to
< #less than
> #greater than

x = 'hello'
y = 'hello'

print(x == y) # true
print(x != y) # False

x = 'a'
y = 'b'

print(ord('a')) # use to check the value of an integer
print('a' > 'b') # False as value of 'a' is 97 and 'b' is 98
print('a' < 'b') # true
print(7.5 > 7) # true
print(7.0 == 7) # true


# Chained Condition
x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x+2


# (not > and > or) order of execution/priority
result4 = result1 or result2 #returns true if either result1 or result2 is true and if both are false it will return false
print(result4)

print(not False) #returns opposite i.e. True
print(not (False or True)) #returns false 
print(not (False and True)) #returns true



# if/Else/Elif
x = input('Name: ')

if x == 'tim':
       print('you are great')
elif x == 'swa':
        print('you are amazing')
else:
        print("we dont know you")


# List
x = [4, True ,'hi']
x.append('hello') # add elements to the end of the list
x.extend([4,3,4,222,34]) #take each elements of the list and append it to the list x
x.pop('hi') #pop removes elements from the list
x[0] = 'hello' #changes value of element 1st (4) to hello
print(x) 

# Tuples
x = (0,1,2,3,5,6) #it is immutable(cant make changes to it as we do in list)

# For loops

for i in range(10):
        print(i)

for i in range(1,10,2)  #(start,stop,step)

for i in range(1,20,3):
        print(i)

x =  [3,4,5,6,7,8]
for i in range(len(x)): #print elements of the list using for 
        print(x[i])

x = [3,4,5,6,7,8]
for i, element in enumerate(x): # this will print indices and elements
        print(i, element)



# While Loops
i = 0
while i<10: # while condition == True this loop will run
        print(i)
        i = i+1 # or  i += 1 or i *= 2 or i -= 1 or i /= 2

# (another way to write the above)

i = 0
while True:
        print(i)
        i += 1
        if i<10:
               break


# Slice Operator
x = [3,4,5,6,7,8]
y = ['hi', 'hello', 'hola', 'more']
s = 'hello'

Sliced = x[0:4:1] # [start:stop:step] 
Sliced = x[::] # this means[beginning:end:step by 1]
Sliced = x[::-1] # reverse a list

print(Sliced)


# SETs
x = set()
s = {4,23,2,2} 
s2 = {2,3,5,6,7}
s.add(5)
s.remove(2)
print(s)

print(4 in s) #check if the element 4 is present in set s or not. if present returns True else False

print(s.union(s2)) #union of two sets
print(s.intersection(s2)) #intersection of two sets
print(s.difference(s2)) #difference of two sets


# Dictionaries
x = {'key' : 4}
x['k2'] = 5 # to add another key
x['k3'] = [2,3,4,5,6,7]


print(x)

print('k2' in x) #checking if the key exists
print(x.values()) #returns all the values of the keys
print(x.keys()) #returns all the keys

del x['k2'] # to delete particular key

for key in x:
        print(key, x[key])


# Comprehensions
x = [x for x in range(5)] #puting a for loop inside so that we could get a list of X
x = [[1 for x in range(50)] for x in range(4)]   #complex: puting a loop inside a loop

x = {i:0 for i in range(100) if i % 5 == 0} # creating Dictionaries, with "for loop" and "if condition"

print(x)

 
# Functions 
def func(x,y):
        print('Run' , x , y)
        return x*y, x/y

print(func(4,5)) 


# *Args & **Kwargs
def func(*args, **kwargs):
        pass

x = [1,33,4456,245456]
print(x)
print(*x)

pairs = [(1,2), (1,3)] #using FOR loop in this

for pair in pairs:
        print(*pair)

