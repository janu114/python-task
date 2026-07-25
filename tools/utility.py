def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def find_min(a, b):
    return min(a, b)

def find_max(a, b):
    return max(a, b)

def average(a, b):
    return (a + b) / 2

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def pounds_to_kg(p):
    return p * 0.453592

def kg_to_pounds(k):
    return k * 2.20462

def palindrome(s):
    return s == s[::-1]