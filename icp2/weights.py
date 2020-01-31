tot= int(raw_input("Enter number of students"))
i=1
n=1
list=[]
while i<= tot:
    w= int(raw_input('Enter Weight %d' % n))
    n= n+1
    list.insert(i,w)
    i= i+1
print("weights in lb:",list)
list2=[w*0.45359237 for w in list if range(0,tot)]
print("Weights in kg:",list2)
