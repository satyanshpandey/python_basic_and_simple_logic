c = 0
lst2 =[1,1,5,100,-20,-20,6,0,0]
position = 1
ind = len(lst2)

for i in lst2:
    # position = position+1
    if position>=len(lst2):
        break
    elif i == lst2[position]:
        c = c+1
        position+=1
        # print("C-------",c)
        # continue
    elif(i!=lst2[position]):
        print("Not matching ",i," to ",lst2[position])
        position+=1

print("Total match number is:",c)
