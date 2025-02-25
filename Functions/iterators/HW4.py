import itertools


#Part1 Defining functions
#1 basic function
def add_numbers(n1,n2):
   return n1+n2

add_lambda= lambda N1, N2: N1+N2

print("using basic function: 3+5 =",add_numbers(3,5))
print("using lambda function: 3+5 =",add_lambda(3,5))
#2 flexible function
def join_words(*words):
  return " ".join(words)
join_words_lambda=lambda *words: " ".join(words)

print(join_words("Hello","world","!"))
print(join_words_lambda("Hello","world","!"))
#3 Recursive function
def countdown(n):
    if n<=0:
        return 0
    else:
        print(n)
        countdown(n-1)
print(countdown(5))

#4 Normal function usage

def greet(name):
    return print(" Welcome to Data Science 245",name,"!")
greet("Alice")
#5 function with default arguments
#Write a function repeat_phrase that repeats a phrase a given number of times, with a default of 2.
def repeat_phrase(phrase, n=2):
     while n>0:
       print(phrase)
       n-=1
     return
repeat_phrase("Hi ")
print()
repeat_phrase("Hi ",3)

# 6 Higher-Order Function
#Write a function apply_function that takes a function and a value as arguments and applies the function to the value
def apply_function(func, val):
    return func(val)
print(apply_function(lambda x: x.upper(), "hello"))
# Part 2 Errors and exceptions
# 7 Handling Errors
def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Cannot be divided by zero"
print("a/b = ",safe_divide(15,3))
# 8 Custom Exceptions
def check_age(age):
     if not isinstance(age,int) or age<=0:
        raise ValueError("Age must be a positive integer!")

try:
  check_age(-2)
except ValueError as e:
    print(e)

#9 Handling Multiple Exceptions
def parse_int(value):
  try:
      return print("Value is", int(value))
  except ValueError:
      return print("Conversion failed")

parse_int("2")
parse_int("ab")

#10 Finally Block
def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Cannot be divided by zero"
    finally:
         print("Division attempted")

print(safe_divide(10,5))

# Part 3: Iterators
# 11 Using Built-in Iterators
I=iter([5,4,3,2,1])
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))

#12 Using Generator Expressions
#Use a generator expression to create an iterator that yields uppercase versions of words in a list. Iterate over it using a for loop
strings=["good","Hello","class","NAME"]
strings_iterator=(a.upper() for a in strings)
for i in strings_iterator:
    print(i)

#13 Custom Iterator Class
class countdown:
    def __init__(self,start):
        self.current =start
    def __iter__(self):
        return self
    def __next__(self):
       if self.current<0:
           raise StopIteration
       else:
           n= self.current
           self.current -=1
           return n

numbers= countdown(4)
for i in numbers:
    print(i)

#14 Using itertools
colors=["red", "blue", "green"]
c=itertools.cycle(colors)
for i in range(6):
    print(next(c))

