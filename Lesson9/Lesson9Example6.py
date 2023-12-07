#or is a logical operator, and is used 
#to combine conditional statements
#or gives false if all condtions are false
purchaseAmount1 = 4501
brandName = "New Balance"
if purchaseAmount1>5000 or brandName == "Nike":
    print("Your discount is 25%")
    
elif purchaseAmount1>4500:
    print("Your discount is 10%")
    
else:
    print("Your discount is 5%")
    

