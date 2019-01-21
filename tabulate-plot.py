import sys
import numpy as np

"""
Handle command line arguments
"""

def helper( message ) :
        print(message)
        print("This program runs as\n\n$ python", sys.argv[0], "which_function\n\nwhere 'which_function' is an integer selecting the function to run.\n")
        print("Functions allowed are:")
        print("1) y = x")
        print("2) y = x**2")
        print("3) y = x**3")
        print("4) y = sin(x)")
        print("5) y = cos(x)")
        print("6) y = tan(x)")
        print()
        exit()
        pass

if ( len(sys.argv) != 2 ) :
    helper("Wrong number of arguments!")

if ( int(sys.argv[1]) < 0 or int(sys.argv[1]) > 6 ) :
    helper("Wrong arguments!")

# selected function index:
which = int( sys.argv[1] )-1
print("You selected function ", sys.argv[1])

"""
Function definition:
"""

# first function: y = x
def func1 ( xval ) :
    return xval

# first function: y = x**2
def func2 ( xval ) :
    return xval*xval

# first function: y = x**3
def func3 ( xval ) :
    return xval*xval*xval

# first function: y = sin(x)
def func4 ( xval ) :
    return np.sin(xval)

# first function: y = cos(x)
def func5 ( xval ) :
    return np.cos(xval)

# first function: y = tan(x)
def func6 ( xval ) :
    return np.tan(xval)

# fill-in the functions list (update when adding functions!)
func_list = [func1, func2, func3, func4, func5, func6]

# define function used:
def func ( xval ) :
    return func_list[which]( xval )

"""
Fill lists:
"""

xval = np.linspace(-3.0, 3.0, num=101, endpoint=True)
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
