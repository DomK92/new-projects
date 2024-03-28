total = 0
user_input = 0
count = 0 

while user_input != -1:
    user_input = int(input("Enter a number (To quit type '-1'): "))
    
    if user_input != -1:
        total += user_input 
        count += 1


average = total / count
print("The average is:", average)
  