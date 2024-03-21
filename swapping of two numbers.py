Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> a,b = b,a
>>> print(a,b)
20 10
>>> a=40
>>> b=50
>>> c=a
>>> a=b
>>> b=c
>>> print(a,b)
50 40
>>> a=5
>>> b=6
>>> a=a^b
>>> b=b^a
>>> a=a^b
>>> print(a,b)
6 5
>>> a=2
>>> b=3
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print(a,b)
3 2
