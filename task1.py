'''
1. Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range
'''
def find_num (x,y):
    odd_num = []
    even_num=[]
    for num in range(x,y+1):
        if num % 2==0:
            even_num.append(num)
        else :
            odd_num.append(num)
    print("even numbers is :", even_num) 
    print("odd numbers is :", odd_num)     
find_num(1,20)     