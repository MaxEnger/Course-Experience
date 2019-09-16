#Distance Function
#IDCE 302
#Max Enger
#Time 10 mins

import math

#Creating a function to simplify the distance equation
def dist(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    dsq = (dx**2) + (dy**2)
    print "dx is:", dx
    print "dy is:", dy
    print "dsq is:", dsq
    result = math.sqrt(dsq)
    return 'The result is:', result
    
#Inputing values into the function to test accuracy
print dist(1,2,4,6)
#print "The result is:", result
