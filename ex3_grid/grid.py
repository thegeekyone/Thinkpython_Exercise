"""
    ThinkPython2 Solution for Chapter 3 Functions

    Question:
        Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Hint: to print more than one value on a line,
you can print a comma-separated sequence of values:
print('+', '-')
By default, print advances to the next line,
but you can override that behavior and put a space at the end, like this:
print('+', end=' ')
print('-')
The output of these statements is '+ -'.
A print statement with no argument ends the current line and goes to the next line.

Write a function that draws a similar grid with four rows and four columns.

"""



def print_horizontal(n):
    print('+', n*'-', end=' ')

def do_twice(f, i):
    f(i)
    f(i)

def print_vertical(n):
    for i in range (n):
        print("|",n*" ","|",n*" ","|")

def print_result(num):
    do_twice(print_horizontal, num)
    print('+')
    print_vertical(num)
    do_twice(print_horizontal, num)
    print('+')
    print_vertical(num)
    do_twice(print_horizontal, num)
    print('+')

while True:
    try:
        x = int(input("Please enter your number: ")) #type 4 if you want to make a 4x4 grid or any other number
    except ValueError:
        print("Sorry, Your input is invaild please enter your number again: ")
        continue
    if x < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        break


print_result(x)
