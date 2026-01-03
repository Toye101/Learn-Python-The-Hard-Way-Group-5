# Traceback (most recent call last): 
#2     Cell In[1], line 8, in <module> 
#3       average_passengers_per_car = car_pool_capacity / passenge
#4   NameError: name 'car_pool_capacity' is not defined
# that means line 8== average_passengers_per_car = car_pool_capacity / passenge    means python doesn't understand what car_pool_capacity is cause our variable was carpool_capacity wich is a typo error 
# if 4 was used instead of 4.0 nothing will happen cause itthe datatype was not spesified
# we are saying the variable cars is contains the number 100
cars = 100 
# we are saying the variable space_in_a_car is contains the number(float) 4.0
space_in_a_car = 4
# we are saying the variable drivers is contains the number 30
drivers =30
# we are saying the variable passengers is contains the number 90
passengers = 90 
cars_not_driven = cars - drivers 
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car 
average_passengers_per_car = passengers / cars_driven 

print("There are", cars, "cars available.") 
print("There are only", drivers, "drivers available.") 
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport" ,carpool_capacity ,"people today.")
print( "We can transport" , carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.") 
print("We need to put about", average_passengers_per_car,"in each car.")

