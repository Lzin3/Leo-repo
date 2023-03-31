#the numbers loop starting at 1 ending at 100
num = 1
while num <= 100:
    #showing the square of each number
    square = num ** 2
    print(f"{num} squared is {square}")
    #if above 2000 end
    if square > 2000:
        break
    num += 1
