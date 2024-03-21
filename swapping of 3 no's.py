Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=5
b=10
c=20
a,b,c=c,b,a
print(a,b,c)
20 10 5
a=2
b=3
c=4
print(a,b,c)
2 3 4
a=2
b=3
a=b
b=a
c=a
print(a,b)
3 3
a=200

b=300
c=a
d=b
print(a,b)
200 300
print(b,a)
300 200
a=1.0
b=2.0
c=3.0
a,b,c=c,a,b
print(a,b,c)
3.0 1.0 2.0
print(a+","+b+","+c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(a+","+b+","+c)
TypeError: unsupported operand type(s) for +: 'float' and 'str'
a=20
b=30
c=40
print(a,+","+b,+","+c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(a,+","+b,+","+c)
TypeError: bad operand type for unary +: 'str'
print(a b c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(a.b.c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(a.b.c)
AttributeError: 'int' object has no attribute 'b'
print(a ,+","+ b ,+","+ c)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(a ,+","+ b ,+","+ c)
TypeError: bad operand type for unary +: 'str'
a=2
b=3
c=4
temp1 = 2
temp 1 =a
SyntaxError: invalid syntax
temp1 = a
temp2 = b
a=c
b=temp1
c=temp2
print(a,b,c)
4 2 3
a=2.0
b=3.0
a=a+b
b=a-b
a=a-b
print(a,b)
3.0 2.0
a=20.0
b=3503
c=1.20
a=20
b=35
c=120
a=a+b+c
b=a-(b+c)
c=a-(a+c)
a=a-(a+b)
print(a,b,c)
-20 20 -120
a=20
b=35
c=120
SyntaxError: multiple statements found while compiling a single statement
a=20,b=35,c=120
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=20
b=35
c=120
>>> b=a-(b+c)
>>> c=a-(a+c)
>>> a=a-(a+b)
>>> a=a+b+c
>>> print(a,b,c)
-120 -135 -120
>>> a=20
>>> b=35
>>> c=120
>>> temp1 = a
>>> a=temp1+b+c
>>> b=a-(b+C)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    b=a-(b+C)
NameError: name 'C' is not defined. Did you mean: 'c'?
>>> b=a-(b+c)
>>> c=a-(temp1+c)
>>> a=temp1
>>> print(a,b,c)
20 20 35
>>> a=20
>>> b=35
>>> c=120
>>> temp1=a
>>> a=temp1+b+c
>>> b=a-(b+c)
>>> c=a-(temp1+c)
>>> print(a,b,c)
175 20 35
>>>  a=20
... b=35
... c=120
... temp1=a
SyntaxError: unexpected indent
>>> a=20,b=35,c=120,temp1=a
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=20
>>> b=35
>>> c=120
>>> temp1=a
>>> temp2=c
>>> a=temp1+b+c
>>> b=a-(b+c)
>>> c=a-(temp1+c)
>>> a=temp2
>>> print(a,b,c)
120 20 35
