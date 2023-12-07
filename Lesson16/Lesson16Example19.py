#A dictionary can contain dictionaries, this is called nested dictionaries
carPark = {
    "car1":{
        "brand":"Dodge",
        "model": "Charger"
        },
    "car2":{
        "brand": "Ford",
        "model": "Mustang"
        }    
    }

print(carPark["car1"]["brand"])
print(carPark["car1"]["model"])
print(carPark["car2"]["brand"])
print(carPark["car2"]["model"])

# for car in carPark:
#     for carIn in carPark[car]:
#         print(carPark[car][carIn])