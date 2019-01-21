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
        print("2) y = exp(x)")
        print("3) y = sqrt(|x|)")
        print()
        exit()
        pass

if ( len(sys.argv) != 2 ) :
    helper("Wrong number of arguments!")

if ( int(sys.argv[1]) < 0 or int(sys.argv[1]) > 3 ) :
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

# first function: y = exp(x)
def func2 ( xval ) :
    return np.exp(xval)

# first function: y = sqrt( |x| )
def func3 ( xval ) :
    return np.sqrt(np.fabs(xval))

# fill-in the functions list (update when adding functions!)
func_list = [func1, func2, func3]

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
