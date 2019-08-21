#LIST in Python


colleges = ['bsc','bms','bbi','mca']

print(colleges[0])

colleges[2]="b.tec"

print(colleges)
print(colleges[1:3])

'''for insert any list in the list '''
list2 = ['kumar','vishwas', 'satyansh','pandey']
print(list2)
'''for inserting the value in the list'''
list2.append('kumar vishwas')
print(list2)
'''for inderting any value in the fix place'''
list2.insert(3,'satyansh pandey')
print(list2)
'''for removing any value in the list '''
list2.remove('pandey')
print(list2)

'''for adding more values in the lists '''
print(list2+['student','class'])

'''for find thelength of the list in the '''
print(len(list2))
print(list2)

'''for find the maximum length of the string by the table orderd '''
print(max(list2))
'''for find the minimum length of the string by the table orderd '''
print(min(list2))






print("!Thanks Python....")