'''Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y'''
def divided_numbers(x,y):
    numbers =[]
    for i in range (1,101):
        if i % x==0 and i % y==0:
            numbers.append(i)

        else:
            continue
    print('numbers is :',numbers)    
divided_numbers(3,7)    