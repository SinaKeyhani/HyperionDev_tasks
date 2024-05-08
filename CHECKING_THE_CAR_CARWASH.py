# CHECKING THE CAR CARWASH 

# 3rd project - if statement : 

# in this task you need to check if the carwash is busy or not. 

clean_car_red = True
clean_car_blue = True
clean_car_green = True
num_of_car = 0
busy = False

print("Welcome to the car wash")

redCheck = input("Is the Red car Dirty? (Yes or No)").capitalize() #Note input is case sensitive here
if redCheck == "Yes":
	clean_car_red = False

blueCheck = input("Is the Blue car Dirty? (Yes or No)").capitalize() #Note input is case sensitive here
if blueCheck == "Yes":
	clean_car_blue = False

greenCheck = input("Is the Green car Dirty? (Yes or No)").capitalize() #Note input is case sensitive here
if greenCheck == "Yes":
	clean_car_green = False

if clean_car_red == False:
	print("Red car really needs a cleaning")
	num_of_car += 1

if clean_car_blue == False:
	print("Blue car really needs a cleaning")
	num_of_car += 1

if clean_car_green == False:
	print("Green car really needs a cleaning")
	num_of_car += 1
	print(num_of_car)

if num_of_car == 3:
	busy = True

if busy == True:
	print("The car wash was was packed today")

else:
	print('The car wash was was not packed today')




