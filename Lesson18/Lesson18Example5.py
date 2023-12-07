#To throw (or raise) an exception, use the raise keyword.
#You can define what kind of error to raise, and the text 
#to print to the user.
quantityParam = 0

if quantityParam<1:
    raise Exception("Quantity can not be less than one.")


