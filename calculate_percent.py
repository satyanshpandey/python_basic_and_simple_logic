'''
    In this program we will see how to calculate the percent
'''



money=int(input("Enter amount:- "))
n=int(input("how many % discount would you want to:- "))
per=n/100
p=per*money
print("your discount is the :- ",p)
print('your percent is:- ',n)
print('you have to pay:-',money-p)
