# Initialising the virables     
# using while loop 
# asking the users to input any number, except -1 
# if user input -1, loop will stop and the average should calculated!
# average = num_1 + num_2 + ... +num_n /n



total =0 
count= 0
num = float(input("please enter any number (-1 to exiting): "))
while num != -1:
    total += num 
    count += 1
    num = float(input("please enter any number (-1 to exiting): "))
    if num ==-1: 
        average = total / count 
        print(average)
        break
    