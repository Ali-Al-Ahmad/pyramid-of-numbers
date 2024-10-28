# Pyramid of Numbers
x  = int(input("Enter x: "))

# range starts from (1 to x+1) to include 1 and number entered as x
for i in range(1,x+1):
    
    #  loop on each line starting from 1 to i as position of line
    for j in range(1,i+1):
        print(j, end=" ")
        
    # jump to new line after finishing the inner loop for each line
    print()
