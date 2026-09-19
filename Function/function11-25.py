# 11. Maximum of three numbers
def max_three(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)


# 12. Count vowels in a string
def vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count = count + 1
    print("Vowels:", count)


# 13. Reverse a string
def reverse(s):
    print(s[::-1])


# 14. Check palindrome
def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


# 15. Sum of all elements in a list
def list_sum(a):
    total = 0
    for i in a:
        total = total + i
    print("Sum:", total)


# 16. Largest element in a list
def largest(a):
    big = a[0]
    for i in a:
        if i > big:
            big = i
    print("Largest:", big)


# 17. Remove duplicate elements
def remove_duplicate(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(b)


# 18. Count element in a list
def count_element(a, x):
    count = 0
    for i in a:
        if i == x:
            count = count + 1
    print("Count:", count)


# 19. Check prime number
def prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print("Prime")
    else:
        print("Not Prime")


# 20. Prime numbers between two numbers
def prime_between(a, b):
    for n in range(a, b + 1):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count = count + 1
        if count == 2:
            print(n)


# 21. Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c


# 22. Second-largest number
def second_largest(a):
    a = list(set(a))
    a.remove(max(a))
    print("Second Largest:", max(a))


# 23. Sort list without sort()
def my_sort(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)


# 24. Merge two lists and remove duplicates
def merge(a, b):
    c = a + b
    d = []

    for i in c:
        if i not in d:
            d.append(i)

    print(d)





# Calling functions

max_three(10, 20, 15)

vowels("hello")

reverse("Python")

palindrome("madam")

list_sum([10, 20, 30])

largest([10, 50, 20, 40])

remove_duplicate([1, 2, 2, 3, 3, 4])

count_element([1, 2, 2, 3, 2], 2)

prime(7)

prime_between(10, 30)

fibonacci(7)

second_largest([10, 50, 30, 20])

my_sort([5, 2, 8, 1, 3])

merge([1, 2, 3], [2, 3, 4])


