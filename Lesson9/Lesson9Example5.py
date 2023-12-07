#and is a logical operator, and is used 
#to combine conditional statements
#and gives true only of all conditions are true
purchaseAmount1 = 5001
brandName = "New Balance"
if purchaseAmount1>5000 and brandName == "Nike":
    print("Your discount is 25%")
    
elif purchaseAmount1>5000:
    print("Your discount is 10%")
    
else:
    print("Your discount is 5%")
    
