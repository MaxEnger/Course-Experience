# Max Enger
# Lab 3: Run-Off Conversion
# Time to complete: 20 min
# Description: Converting the run-off on a 50x20ft plot of land in Kenya

#Converting feet to inches
l= 50*12
w= 20*12

#Calculating Area of Plot in inches
plot1_area = l*w

#Calculating number of inches of rainfall in cubic inches of water
r = (plot1_area*1)

#Converting cubic inches to gallons
gal_conv = 231
r_gal = (r / gal_conv)

#Final Outputs
print 'The final outputs for lab 3 are below:'
print 'plot_length is:',l
print 'plot_width is:',w
print 'rainfall_inches is:',r
print 'runoff_gallons is:',r_gal
