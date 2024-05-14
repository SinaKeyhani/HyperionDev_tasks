
print('PATTERNS\n')
print('Example one')
print('Left sided pyramid')

symbol = "*"
rows = int(input('Enter your number for the pyramid height: \t'))
for i in range(1,rows+1):
    if i <= rows:
        print (symbol * i)
    


print('\nExample two')
print('Right Sided Pyramid')

symbol = "*"
rows = int(input('Enter your number for the pyramid height: \t'))

for i in range(1,rows+1):
    if i <= rows:
        print(" " *(rows - i), end ="") # This is for the spaces
        print (symbol * i)





print('\nExample three')
print('Pyramid')

rows = int(input('Enter your number for the pyramid height: \t'))

for i in range(rows):
    print(" " * (rows - i -1), end="")
    print("*" *(2*i+1))


print('\nExample four')
print('Invert pyramid')

rows = int(input('Enter your number for the pyramid height: \t'))
for i in range(rows, 0 , -1):   
    print(" " * (rows - i), end="")
    print("*" *(2*i-1))


print('\nExample five')
print('half pyramid')


for i in range(1,10):
    if i<= 5:
        print("*" * i)

    else:
        print("*"*(10-i))



    





        



