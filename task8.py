'''Create a function that takes x,y and prints all the number that can be divide by y from x to 100'''
def divide_num(x,y):
    numbers=[]
    for num in range(x,101):
        if num %y==0:
            numbers.append(num)
        else:
            continue    
    print(numbers)
divide_num(1,5)    