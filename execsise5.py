#f means format
#To round a float you use round(float e.g 1.7566)
name = 'Zed A. Shaw' 
age = 35 # not a lie 
height = 74 # inches 
height_cm = height*2.54
weight = 180 # lbs  
weight_kg = weight*0.45
eyes = 'Blue' 
teeth = 'White' 
hair = 'Brown'    
# Adding {} showspython that the object inside the braces i a variable and your to present that vairables value
print(f"Let's talk about {name}.") 
print(f"He's {height} inches or {height_cm} centimerters tall.") 
print(f"He's {weight} pounds or {weight_kg} kilograms heavy.") 
print("Actually that's not too heavy.") 
print(f"He's got {eyes} eyes and {hair} hair ")
print(f"He's got {eyes} eyes and {hair} hair." ) 
print(f"His teeth are usually {teeth} depending on the day.")
# this line is tricky, try to get it exactly right 
total = age + height + weight 
print(f"If I add {age}, {height}, and {weight} I get {total}")