import sys

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

# fill-in the functions list (update when adding functions!)
func_list = [func1]

# define function used:
def func ( xval ) :
    return func_list[which]( xval )

"""
Fill lists:
"""
import numpy as np

xval = np.linspace(-5.0, 5.0, num=101, endpoint=True)
print( "xval = ", xval )
yval = func( xval )
print( "yval = ", yval )
