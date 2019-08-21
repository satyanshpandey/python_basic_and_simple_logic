'''the elif condiction can make you to check multiple logical expression
For the true and it executes the block of the code if the condiction is true
'''



'''
Note:-
        Pytohn don't give the switch and case condictions like other languages
        instead of switch and case statement we can use if...elif statement to
         create swutch case
'''
#Example:-


money=int(input("Enter amount :- "))
if(money<1000):
    discount=money*0.10
    print("your discount is 10%",discount)
elif(money<2000):
    discount=money*0.20
    print("your discount is 20%", discount)
elif(money<3000):
    discount=money*0.30
    print("your discount is 30%", discount)
print("net payable:- " ,money-discount)




