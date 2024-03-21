Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(8/3)
2.6666666666666665
print(int(8/3))
2
#ROUND
print(round(8/3))
3
print(round(8/3,2))
2.67
print(round(8/3,0))
3.0
print(round(8/3,8))
2.66666667
#FLOW DIVISION
print(8 // 3)
2
score = 5
score+=10
print(score)
15
height = 10.0
>>> weight = 55
>>> print("weigh:"+weight +,+ "Height:"+height)
SyntaxError: invalid syntax
>>> print("weigh:"+weight +","+ "Height:"+height)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("weigh:"+weight +","+ "Height:"+height)
TypeError: can only concatenate str (not "int") to str
>>> print("weigh:"+str(weight) +,+ "Height:"+str(height))
SyntaxError: invalid syntax
>>> print("weigh:"+str(weight) +","+ "Height:"+str(height))
weigh:55,Height:10.0
>>> print(F"weigh:"+(weight) +,+ "Height:"+(height))
SyntaxError: invalid syntax
>>> print(F"weigh:"+(weight) +","+ "Height:"+(height))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(F"weigh:"+(weight) +","+ "Height:"+(height))
TypeError: can only concatenate str (not "int") to str
>>> print(F"weigh:"+{weight} +","+ "Height:"+{height})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(F"weigh:"+{weight} +","+ "Height:"+{height})
TypeError: can only concatenate str (not "set") to str
>>> print(F"weight:"{weight} +","+ "Height:"{height})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(f"weigh:"+{weight} +","+ "Height:"+{height})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(f"weigh:"+{weight} +","+ "Height:"+{height})
TypeError: can only concatenate str (not "set") to str
>>> print(f"weigh:"+(weight) +","+ "Height:"+(height))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(f"weigh:"+(weight) +","+ "Height:"+(height))
TypeError: can only concatenate str (not "int") to str
>>> print(f"weigh:(weight),Height:(height))
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"weight:{weight},Height{height})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(F"weight:{weight},Height{height})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"weight:{weight} , Height:{height}")
...       
weight:55 , Height:10.0
