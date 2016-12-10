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
        x = int(input("Please enter your number: "))
    except ValueError:
        print("Sorry, but I've told you to enter a number not a string: ")
        continue
    if x < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        break


print_result(x)
