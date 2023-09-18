'''Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y'''
def mul_num(x,y):
    z=()
    for n in range(x,y+1):
        for b in range(1,11):
            result=n*b
            print(f"{n} X {b} = {result}")   

mul_num(3,8)
             