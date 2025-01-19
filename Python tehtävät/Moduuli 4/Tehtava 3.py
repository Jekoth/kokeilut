small = None
large = None

while True: #infinity loop
    number = input("Enter a numbers: ")
    if not number: break #if number is not entered stop the loop
    num = int(number) #convert string to int
    small = number if small is None or number < small else small #this line of code searches for smallest number
    large = num if large is None or num > large else large #this line of code searches for largest number

print(f"Smallest: {small}, largest: {large}" if small is not None else "No numbers entered.")
