nth = int(input("Enter the nth number to find the sum! "))

sum = 0
for num in range(1, nth + 1):
    sum = sum + num
print("Sum:" ,sum)