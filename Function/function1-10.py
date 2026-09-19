# 1. Hello World
def hello():
    print("Hello, World!")


# 2. Greeting
def greet(name):
    print("Hello", name)


# 3. Add two numbers
def add(a, b):
    print("Addition:", a + b)


# 4. Square
def square(n):
    print("Square:", n * n)


# 5. Even or Odd
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


# 6. Maximum of two numbers
def maximum(a, b):
    if a > b:
        print("Maximum:", a)
    else:
        print("Maximum:", b)


# 7. Celsius to Fahrenheit
def fahrenheit(c):
    print("Fahrenheit:", (c * 9 / 5) + 32)


# 8. Area of Circle
def circle_area(r):
    print("Area:", 3.14 * r * r)


# 9. Factorial
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print("Factorial:", f)


# 10. Positive, Negative or Zero
def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")


# Calling all functions
hello()
greet("Rohit")
add(10, 20)
square(5)
even_odd(10)
maximum(10, 20)
fahrenheit(25)
circle_area(5)
factorial(5)
check_number(-5)
