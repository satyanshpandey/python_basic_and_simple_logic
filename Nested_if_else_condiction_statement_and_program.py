'''
        :- It may happen many times that you want to check the condiction after getting
            true result of the frist condiction.
        :- In such types of the scenarios you can use the nested if construct.

    '''

num=int(input("enter the number for checking is divisible or not"))
if(num%2==0):
    if(num%3==0):
        print("the number is divisible by 3 and 2")
    else:
        print("the number is divisible by 2 not 3")
else:
    if(num%3==0):
        print("number is divisible by 3 not 2")
    else:
        print("number not divisible 2 and also 3")


