Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib as mpl
>>> import matplotlib.pyplot as plt
>>> from scipy import linalg, optimize
>>> from scipy.optimize import minimize
>>> def tc(x):
	return 0

>>> reload(tc)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    reload(tc)
NameError: name 'reload' is not defined
>>> reload(tc(x))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    reload(tc(x))
NameError: name 'reload' is not defined
>>> tc(x)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tc(x)
NameError: name 'x' is not defined
>>> tc
<function tc at 0x060A9AE0>
>>> tc()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    tc()
TypeError: tc() missing 1 required positional argument: 'x'
>>> tc(1)
0
>>> redefine tc(x):
	
SyntaxError: invalid syntax
>>> def tc(x):
	return sum(sum(sum(ceil(sum(q)/V)))*tc)

>>>  def TC(x):
	return sum(sum(sum(ceil(sum(q)/V)))*tc)
SyntaxError: unexpected indent
>>> def TC(x):
	return sum(sum(sum(ceil(sum(q)/V)))*tc)

>>> TC
<function TC at 0x060A9AE0>
>>> def TC(tc,q,V):
    return sum(sum(sum(ceil(sum(q)/V)))*tc)

>>> TC(1,2,3)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    TC(1,2,3)
  File "<pyshell#23>", line 2, in TC
    return sum(sum(sum(ceil(sum(q)/V)))*tc)
NameError: name 'ceil' is not defined
>>> TC
<function TC at 0x0EF776F0>
>>> TC(1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    TC(1)
TypeError: TC() missing 2 required positional arguments: 'q' and 'V'
>>> def TC(tc,q,V):
    return sum(sum(sum(__ceil__(sum(q)/V)))*tc)

>>> TC(1,2,3)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    TC(1,2,3)
  File "<pyshell#28>", line 2, in TC
    return sum(sum(sum(__ceil__(sum(q)/V)))*tc)
NameError: name '__ceil__' is not defined
>>> def TC(tc,q,V):
    return sum(sum(sum(math.ceil(sum(q)/V)))*tc)

>>> TC(1,2.3)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    TC(1,2.3)
TypeError: TC() missing 1 required positional argument: 'V'
>>> TC(1,2,3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    TC(1,2,3)
  File "<pyshell#31>", line 2, in TC
    return sum(sum(sum(math.ceil(sum(q)/V)))*tc)
NameError: name 'math' is not defined
>>> import math
>>> TC(1,2,3)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    TC(1,2,3)
  File "<pyshell#31>", line 2, in TC
    return sum(sum(sum(math.ceil(sum(q)/V)))*tc)
TypeError: 'int' object is not iterable
>>> 
