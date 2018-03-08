from clifford.g3 import
from numpy import e,pi
a = e1 + 2*e2 + 3*e3 # vector
R = e**(pi/4*e12)    # rotor
R*a*~R    # rotate the vecto
