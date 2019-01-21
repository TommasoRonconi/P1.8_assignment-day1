import sys
import numpy as np

"""
Handle command line arguments
"""

# selected function index:
which = int( sys.argv[1] )-1
print("You selected function ", sys.argv[1])

"""
Function definition:
"""

# first function: y = x
def func1 ( xval ) :
    return xval

# first function: y = x
def func2 ( xval ) :
    return np.sin(xval)

# first function: y = x
def func3 ( xval ) :
    return np.cos(xval)

# first function: y = x
def func4 ( xval ) :
    return np.tan(xval)

# fill-in the functions list (update when adding functions!)
func_list = [func1, func2, func3, func4]

# define function used:
def func ( xval ) :
    return func_list[which]( xval )

"""
Fill lists:
"""

xval = np.linspace(-5.0, 5.0, num=101, endpoint=True)
print( "xval = ", xval )
yval = func( xval )
print( "yval = ", yval )

"""
Plot lists:
"""

import matplotlib.pyplot as plt

fig = plt.figure( figsize=( 12, 8 ) )
ax = fig.add_subplot( 1, 1, 1 )

ax.plot( xval, yval )
plt.show()
